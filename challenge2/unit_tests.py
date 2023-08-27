import unittest

class TestYourFunctions(unittest.TestCase):

    def test_initial_conditions(self):
        state, c1, c2, end_time, result = intial_conditions(22, 0.1, 0.01, 400)
        self.assertEqual(state, 22)
        self.assertEqual(c1, 0.1)
        self.assertEqual(c2, 0.01)
        self.assertEqual(end_time, 400)
        self.assertEqual(result, [])

    def test_observe(self):
        result = []
        observe(result, 10)
        self.assertEqual(result, [10])

    def test_update_system(self):
        x_state, y_state = update_system(20, 30, 0.1, 0.01, 0.2)
        self.assertEqual(x_state, 18.0)
        self.assertEqual(y_state, 28.4)


if name == 'main':
    unittest.main()
