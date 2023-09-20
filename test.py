import unittest
import enum
from corruptionModel import CorruptionEnum, Factor, CorruptionModel
import enum

from main import calculate_corruption, update_factor

# Import your classes and functions here

class TestCorruptionModel(unittest.TestCase):
    def setUp(self):
        self.factors = {
            CorruptionEnum.GOVERNANCE_EFFECT: Factor(value=0.6, weight=0.1, update_delta=0.005, update_function=update_factor),
            CorruptionEnum.ECONOMIC_DEVELOPMENT_EFFECT: Factor(value=0.5, weight=0.05, update_delta=0.003, update_function=update_factor),
            CorruptionEnum.MEDIA_EXPOSURE_EFFECT: Factor(value=0.4, weight=0.03, update_delta=-0.001, update_function=update_factor),
            CorruptionEnum.LAW_ENFORCEMENT_EFFECT: Factor(value=0.7, weight=0.08, update_delta=0.002, update_function=update_factor),
        }
        self.iterations = 10000
        self.initial_corruption = 0.3
        self.corruption_decay = 0.02

        self.modelHandler = CorruptionModel(
            factors=self.factors,
            iterations=self.iterations,
            initial_corruption=self.initial_corruption,
            corruption_decay=self.corruption_decay,
            calculate_corruption=calculate_corruption
        )

    def test_initialization(self):
        self.assertEqual(self.modelHandler.corruption, self.initial_corruption)
        self.assertEqual(self.modelHandler.corruption_decay, self.corruption_decay)
        self.assertEqual(self.modelHandler.iterations, self.iterations)
        self.assertEqual(len(self.modelHandler.factors), len(self.factors))

    def test_update_factor(self):
        self.assertEqual(update_factor(0.5, 0.1), 0.6)
        self.assertEqual(update_factor(0.3, -0.05), 0.25)

    def test_calculate_corruption(self):
        corruption = self.modelHandler.corruption
        result = self.modelHandler.calculate_corruption(
            corruption, self.corruption_decay, self.factors)
        self.assertIsInstance(result, float)

    def test_observe(self):
        new_corruption = 0.4
        self.modelHandler.observe(new_corruption)
        self.assertEqual(self.modelHandler.corruption, new_corruption)

    def test_get_corruption(self):
        self.assertEqual(self.modelHandler.get_corruption(), self.initial_corruption)

    def test_model(self):
        self.assertIsNone(self.modelHandler.model())  # Function prints, so it doesn't return anything

if __name__ == '__main__':
    unittest.main()
