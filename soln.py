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

# Replace 'inf' values with NaN
data.replace([np.inf, -np.inf], np.nan, inplace=True)
