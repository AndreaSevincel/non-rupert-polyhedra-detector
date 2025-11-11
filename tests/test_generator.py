import unittest
from src.dataset.generator import generate_polyhedra_dataset

class TestPolyhedraGenerator(unittest.TestCase):

    def test_generate_polyhedra(self):
        dataset = generate_polyhedra_dataset(num_polyhedra=10)
        self.assertEqual(len(dataset), 10)
        for polyhedron in dataset:
            self.assertIn('vertices', polyhedron)
            self.assertIn('faces', polyhedron)
            self.assertIn('edges', polyhedron)
            self.assertGreater(len(polyhedron['vertices']), 0)
            self.assertGreater(len(polyhedron['faces']), 0)
            self.assertGreater(len(polyhedron['edges']), 0)

    def test_generate_specific_polyhedron(self):
        polyhedron = generate_polyhedra_dataset(num_polyhedra=1, polyhedron_type='tetrahedron')[0]
        self.assertEqual(len(polyhedron['vertices']), 4)
        self.assertEqual(len(polyhedron['faces']), 4)
        self.assertEqual(len(polyhedron['edges']), 6)

if __name__ == '__main__':
    unittest.main()