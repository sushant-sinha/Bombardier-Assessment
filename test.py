import unittest
import pandas as pd
import numpy as np

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