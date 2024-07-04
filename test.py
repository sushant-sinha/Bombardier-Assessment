import unittest
import pandas as pd
import numpy as np
from soln import fill_missing_values, calculate_average_glucose, diagnose_diabetes, normalize_data, calculate_mean_excluding_outliers

class testDiabetesDiagnosisSteps(unittest.TestCase):

    # Sample data for testing
    def setUp(self):
        self.data = pd.DataFrame({
            'glucose_mg/dl_t1': [100, 150, 200, np.nan, np.inf, -100],
            'glucose_mg/dl_t2': [110, 160, 210, 180, -np.inf, 160],
            'glucose_mg/dl_t3': [120, 170, 220, 190, 302, 165],
            'cancerPresent': [1, 'False', 'True', 0, 'True', 'False'],
            'atrophy_present': [1, 0, 10, 1, 1, 0]
        })

    # Calculate and test average glucose values
    def test_calculate_average_glucose(self):
        df = calculate_average_glucose(self.data.copy())
        expected_averages = [110, 160, 210, 152.5, 189, 137.5]
        self.assertTrue(np.allclose(df['average_glucose'], expected_averages))

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
