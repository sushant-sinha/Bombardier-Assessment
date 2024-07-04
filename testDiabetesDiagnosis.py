import unittest
import pandas as pd
import numpy as np
from diabetesDiagnosis import fill_missing_values, calculate_average_glucose, diagnose_diabetes, normalize_data, calculate_mean_excluding_outliers

class testDiabetesDiagnosis(unittest.TestCase):

    # Sample data for testing
    def setUp(self):
        self.data = pd.DataFrame({
            'glucose_mg/dl_t1': [100, 150, 200, np.nan, np.inf, -100],
            'glucose_mg/dl_t2': [110, 160, 210, 180, -np.inf, 160],
            'glucose_mg/dl_t3': [120, 170, 220, 190, 302, 165],
            'cancerPresent': [1, 'False', 'True', 0, 'True', 'False'],
            'atrophy_present': [1, 0, 10, 1, 1, 0]
        })

    # Ensure missing values, 'inf', and negative values are handled correctly
    def test_fill_missing_values(self):
        df = fill_missing_values(self.data.copy())
        self.assertFalse(df['glucose_mg/dl_t1'].isnull().any())
        self.assertFalse(df['glucose_mg/dl_t2'].isnull().any())
        self.assertFalse(df['glucose_mg/dl_t3'].isnull().any())
        self.assertFalse(df['cancerPresent'].isnull().any())
        self.assertFalse(df['atrophy_present'].isnull().any())
        self.assertTrue((df['glucose_mg/dl_t1'] >= 0).all())
        self.assertTrue((df['glucose_mg/dl_t2'] >= 0).all())
        self.assertTrue((df['glucose_mg/dl_t3'] >= 0).all())

    # Test calculation of mean excluding outliers
    def test_calculate_mean_excluding_outliers(self):
        series = pd.Series([100, 150, 200, 250, 10000])
        mean_value = calculate_mean_excluding_outliers(series)
        self.assertAlmostEqual(mean_value, 175)

    # Calculate and test average glucose values
    def test_calculate_average_glucose(self):
        df = calculate_average_glucose(self.data.copy())
        expected_averages = [110, 160, 210, 152.5, 189, 137.5]
        self.assertTrue(np.allclose(df['average_glucose'], expected_averages))

    # Test diabetes diagnosis
    def test_diagnose_diabetes(self):
        df = self.data.copy()
        df['average_glucose'] = [110, 160, 210, 185, 210, 150]
        df['diabetes_diagnosis'] = df['average_glucose'].apply(diagnose_diabetes)
        expected_diagnosis = ['normal', 'prediabetes', 'diabetes', 'prediabetes', 'diabetes', 'prediabetes']
        self.assertEqual(list(df['diabetes_diagnosis']), expected_diagnosis)

    # Test normalization of 'cancerPresent' and 'atrophy_present' columns
    def test_normalize_data(self):
        df = normalize_data(self.data.copy())
        self.assertEqual(df['cancerPresent'].dtype, bool)
        self.assertEqual(df['atrophy_present'].dtype, int)

if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
