import unittest
from src.algorithms.rupert_checker import is_non_rupert

class TestRupertChecker(unittest.TestCase):

    def test_non_rupert_polyhedron(self):
        # Example of a known non-Rupert polyhedron
        polyhedron = [...]  # Define the polyhedron vertices and faces
        result = is_non_rupert(polyhedron)
        self.assertTrue(result)

    def test_rupert_polyhedron(self):
        # Example of a known Rupert polyhedron
        polyhedron = [...]  # Define the polyhedron vertices and faces
        result = is_non_rupert(polyhedron)
        self.assertFalse(result)

    def test_invalid_polyhedron(self):
        # Test with an invalid polyhedron representation
        polyhedron = None  # or some invalid structure
        with self.assertRaises(ValueError):
            is_non_rupert(polyhedron)

if __name__ == '__main__':
    unittest.main()