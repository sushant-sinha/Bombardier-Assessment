import pandas as pd

# Loading the CSV file, assuming its in the same directory. If not, please update the `file_path`
file_path = 'patient_data.csv'
data = pd.read_csv(file_path, encoding='ISO-8859-1')

# Removing PHI columns: `first_name`, `lastName`, `Email`, `Address`
data = data.drop(columns=['first_name', 'lastName', 'Email', 'Address'])