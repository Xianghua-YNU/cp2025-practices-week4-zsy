import unittest
import numpy as np
from src.bacteria_model_student import BacteriaModel, load_bacteria_data
#from solutions.bacteria_model_solution import BacteriaModel, load_bacteria_data

class TestBacteriaModel(unittest.TestCase):
    def test_v_model(self):
        model = BacteriaModel(A=1.0, tau=2.0)
        t = np.linspace(0, 10, 100)
        result = model.v_model(t)
        self.assertEqual(len(result), 100)

    def test_w_model(self):
        model = BacteriaModel(A=1.0, tau=2.0)
        t = np.linspace(0, 10, 100)
        result = model.w_model(t)
        self.assertEqual(len(result), 100)

    def test_data_loading(self):
        time, response = load_bacteria_data('data/g149novickA.txt')
        self.assertGreater(len(time), 0)
        self.assertGreater(len(response), 0)

if __name__ == "__main__":
    unittest.main()
