# Non-Rupert Polyhedra Detector

This project aims to create a dataset of convex polyhedra and develop an algorithm to check if these polyhedra are non-Rupert. Additionally, a machine learning model will be trained to predict the non-Rupert property of polyhedra.

## Project Structure

- **src/**: Contains the main source code for dataset generation, validation, algorithms, models, and visualization.
  - **dataset/**: 
    - `generator.py`: Functions to generate a dataset of convex polyhedra.
    - `validator.py`: Functions to validate the generated polyhedra dataset.
    - `polyhedra_loader.py`: Functionality to load and preprocess the polyhedra dataset.
  - **algorithms/**: 
    - `rupert_checker.py`: Algorithm to check if a polyhedron is non-Rupert.
    - `geometric_utils.py`: Utility functions for geometric calculations.
  - **models/**: 
    - `train.py`: Code to train the machine learning model.
    - `predict.py`: Functionality to make predictions using the trained model.
    - `model_architecture.py`: Defines the architecture of the machine learning model.
  - **visualization/**: 
    - `plotter.py`: Functions for visualizing the dataset and model predictions.

- **data/**: 
  - **raw/**: Directory for storing the raw dataset of convex polyhedra.
  - **processed/**: Directory for storing the processed dataset ready for training.

- **notebooks/**: 
  - `data_exploration.ipynb`: Jupyter notebook for exploring the dataset.
  - `model_evaluation.ipynb`: Jupyter notebook for evaluating the trained model.

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

## Usage

1. **Dataset Generation**: Use `generator.py` to create a dataset of convex polyhedra.
2. **Validation**: Validate the dataset using `validator.py`.
3. **Non-Rupert Check**: Implement the non-Rupert check using `rupert_checker.py`.
4. **Model Training**: Train the machine learning model with `train.py`.
5. **Prediction**: Make predictions using the trained model with `predict.py`.
6. **Visualization**: Visualize results with `plotter.py`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file for details.