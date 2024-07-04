'''

Take home assessment for Cloud Operations Team Internship(Fall 2024) at Bombardier

Prepared by: Sushant Sinha(sinhasushant04@gmail.com)
Submitted to : Mamaleshwar Kovi Gowri Kumar(Mamaleshwar.kg@aero.bombardier.com)

Below are the CRITICAL assumptions made while creating the 

    1)Data Imputation: for the missing values in the glucose readings, we're replacing the values with the average of the entire column. This route was chosen because we cannot delete that patient's entire row. We need to give a result to the patient.
    
    Else, we could have given a message `incomplete data` in the diabetes_diagnostic column for that patient.

    2) Handling outliers(for patient_id:705): considering the glucose_mg/dl_t2 value for calculating the mean will affect all the data of all the patients which have a missing glucose_mg/dl_t2(because we are using the data imputation). To tackle this, we will ignore these values(outliers) while calculating the mean.

    3) cancerPresent and atrophy_Present have no effect on our diagnosis. It is just for user's reference.

'''

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

# The below piece of code might not be needed if we are guaranteed that `cancerPresent` and `atrophy_present` are always present
# Fill missing values for 'cancerPresent' and 'atrophy_present'
data['cancerPresent'] = data['cancerPresent'].fillna('False').astype(bool)
data['atrophy_present'] = data['atrophy_present'].fillna(0).astype(int)

# Step 3: Normalize Data
# Ensuring 'cancerPresent' is boolean and 'atrophy_present' is integer
data['cancerPresent'] = data['cancerPresent'].astype(bool)
data['atrophy_present'] = data['atrophy_present'].astype(int)

# Step 4: Add a column for average glucose levels
# Adding a new column for `average_glucose`
data['average_glucose'] = data[glucose_columns].mean(axis=1)

# Step 5: Add a column for diabetes diagnosis
def diagnose_diabetes(avg_glucose):
    if avg_glucose < 140:
        return 'normal'
    elif 140 <= avg_glucose <= 199:
        return 'prediabetes'
    else:
        return 'diabetes'

# Creating a new column for diagnosis: `diabetes_diagnosis` and applying the results
data['diabetes_diagnosis'] = data['average_glucose'].apply(diagnose_diabetes)

# Step 6: Store data to a CSV file
# Storing the diagnosis in a CSV file (preferred because the input data was in CSV format)
output_file_path = 'diabetes_diagnosis_data.csv'
data.to_csv(output_file_path, index=False)
