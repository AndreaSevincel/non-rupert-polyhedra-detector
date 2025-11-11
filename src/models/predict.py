from sklearn.externals import joblib
import numpy as np

class PolyhedronPredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def preprocess_input(self, polyhedron_data):
        # Assuming polyhedron_data is a numpy array or can be converted to one
        return np.array(polyhedron_data).reshape(1, -1)

    def predict(self, polyhedron_data):
        processed_data = self.preprocess_input(polyhedron_data)
        prediction = self.model.predict(processed_data)
        return prediction[0]

if __name__ == "__main__":
    # Example usage
    model_path = 'path/to/your/trained/model.pkl'  # Update with the actual model path
    predictor = PolyhedronPredictor(model_path)
    
    # Replace with actual polyhedron data for prediction
    polyhedron_data = [/* feature values */]
    result = predictor.predict(polyhedron_data)
    print(f'The polyhedron is {"non-Rupert" if result == 1 else "Rupert"}')