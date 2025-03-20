# test/test_millikan.py
import unittest
import numpy as np
from src.millikan_fit_student import load_data, calculate_parameters, calculate_planck_constant

class TestMillikanFit(unittest.TestCase):
    def test_load_data(self):
        x, y = load_data('data/millikan.txt')
        self.assertIsNotNone(x)
        self.assertIsNotNone(y)

    def test_calculate_parameters(self):
        x = np.array([1, 2, 3, 4, 5])
        y = np.array([2, 4, 6, 8, 10])  # 修改 y 使其长度与 x 相同
        m, c, Ex, Ey, Exx, Exy = calculate_parameters(x, y)
        self.assertAlmostEqual(m, 2.0)
        self.assertAlmostEqual(c, 0.0)

    def test_calculate_planck_constant(self):
        m = 6.62607015e-34  # 普朗克常量的实际值
        h = calculate_planck_constant(m)
        self.assertAlmostEqual(h, 6.62607015e-34)

if __name__ == "__main__":
    unittest.main()
