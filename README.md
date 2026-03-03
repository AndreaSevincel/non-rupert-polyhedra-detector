On august 27th 2025, I have seen a new paper that finally found a convex polyhedron that is non-rupert, the Noperthedron.
While there is no analytic way to find the set of non-Rupert convex polyhedra, I wanted to find a heuristic/ML way to at least predict approximately.

# Non-Rupert Polyhedra Detector

This project aims to develop an automated, data-driven computational pipeline to discover novel "nopert" (non-Rupert) polyhedra.
Randomly generating shapes and testing them algorithmically is computationally unfeasible. Therefore, my project aims to automate this discovery using 3D Geometric Deep Learning.

## Project Structure

- **src/**: This is the first approach I have though of, but perhaps MeshCNN could be the improvement i need
  - **dataset/**: 
    - `generator.ipynb`: generated 3000 polyhedra according to our needs (certain sphericity, certain nieuwland). The final .pt file is 37mb so github does not let me share
  - **models/**: 
    - `cvae_3.ipynb`: Code to train the machine learning model with the .pt dataset created before. Used CVAE and Pointnet++ as the encoder.
    - `cvae_weights.pth`: the final weights after 100 epochs
  - **visualization/**: 
    - `plotter.py`: Functions for visualizing the dataset and model predictions.
  - **evaluate/**:
    - `final.ipynb`: this notebook must definitively prove if those guesses are topologically valid non-Rupert objects. it loads the trained weights and demands a shape with impossible boundary parameters: a Nieuwland constant of 0.985 and a Sphericity of 0.960.


- **tests/**: 
  - `test_generator.py`: Unit tests for the dataset generator functions.
  - `test_rupert_checker.py`: Unit tests for the Rupert checker algorithm.
  - `test_model.py`: Unit tests for model training and prediction functions.

- **papers/**: 
  - `references.md`: References to scientific papers related to non-Rupert convex polyhedra.

- **requirements.txt**: Lists the Python dependencies required for the project.

- **setup.py**: Used for packaging the project.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```
## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.
