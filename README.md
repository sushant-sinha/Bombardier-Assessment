# Patient Data ETL Pipeline

Developed by [Sushant Sinha](https://github.com/sushant-sinha "Sushant Sinha") as a part of Bombardier Assessment

This repository contains a Python ETL (Extract, Transform, Load) pipeline designed to clean and process patient data from a hospital. The pipeline removes protected health information (PHI), handles missing and invalid values, normalizes data, and stores the cleaned data into a structured format. Additionally, it includes unit tests to ensure data integrity and correctness.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
## Features

- Removes PHI (names, addresses, etc.) from the dataset.
- Handles missing values and invalid data (e.g., `NaN`, `inf`, negative values).
- Normalizes and cleans the data.
- Adds columns for average glucose levels and diabetes diagnosis.
- Excludes outliers when calculating mean values.
- Stores the cleaned data into a CSV file.
- Includes comprehensive unit tests.

## Requirements

- Python 3.6+
- pandas
- numpy
- unittest (for running tests)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sushant-sinha/Bombardier-Assessment.git
    cd Bombardier-Assessment
    ```

2. Install the required dependencies:

    ```bash
    pip install pandas numpy
    ```

## Usage

1. Place your input CSV file (e.g., `patient_data.csv`) in the project directory.

2. Update the file paths in `diabetesDiagnosis.py`:

    ```python
    file_path = 'path_to_your_file/patient_data.csv'
    output_file_path = 'path_to_your_output/diabetes_diagnosis_data.csv'
    ```

3. Run the ETL script:

    ```bash
    python diabetesDiagnosis.py
    ```

4. The processed data will be saved to the specified output file path.

## Testing

1. To run the unit tests, use the following command:

    ```bash
    python testDiabetesDiagnosis.py
    ```

2. The tests will verify the correctness of the ETL functions and ensure data integrity.
