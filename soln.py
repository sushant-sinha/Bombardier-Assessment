import pandas as pd
import numpy as np

# Loading the CSV file, assuming its in the same directory. If not, please update the `file_path`
file_path = 'patient_data.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Removing PHI columns: `first_name`, `lastName`, `Email`, `Address`
data = data.drop(columns=['first_name', 'lastName', 'Email', 'Address'])

# Step 2: Clean the data
# Ensuring all the blood sugar readings are numeric and non-negative
glucose_columns = ['glucose_mg/dl_t1', 'glucose_mg/dl_t2', 'glucose_mg/dl_t3']
data[glucose_columns] = data[glucose_columns].apply(pd.to_numeric, errors='coerce')

# Replacing 'inf' values with NaN
data.replace([np.inf, -np.inf], np.nan, inplace=True)

# Handling outliers using IQR
def calculate_mean_excluding_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    # Determine boundary values for non-outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # Filter out outliers and then calculate mean
    filtered_series = series[(series >= lower_bound) & (series <= upper_bound)]
    return filtered_series.mean()

# Filling the missing blood sugar values with the mean of the column , excluding outliers
for col in glucose_columns:
    mean_value = calculate_mean_excluding_outliers(data[col])
    data[col].fillna(mean_value, inplace=True)
    data[col] = data[col].apply(lambda x: mean_value if x < 0 else x)

def diagnose_diabetes(avg_glucose):
    if avg_glucose < 140:
        return 'normal'
    elif 140 <= avg_glucose <= 199:
        return 'prediabetes'
    else:
        return 'diabetes'
