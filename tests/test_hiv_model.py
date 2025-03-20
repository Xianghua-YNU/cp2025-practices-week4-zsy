import unittest
import numpy as np
from src.hiv_model_student import HIVModel, load_hiv_data

class TestHIVModel(unittest.TestCase):
    def test_viral_load(self):
        model = HIVModel(A=1000, alpha=0.1, B=500, beta=0.05)
        time = np.linspace(0, 10, 100)
        result = model.viral_load(time)
        self.assertEqual(len(result), 100)

    def test_data_loading(self):
        time, response = load_hiv_data('data/HIVseries.csv')
        self.assertIsNotNone(time)
        self.assertIsNotNone(response)

if __name__ == "__main__":
    unittest.main()
