from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def plot_polyhedron(vertices, faces, title='Polyhedron'):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Create a 3D polygon for each face
    for face in faces:
        poly3d = [[vertices[vertice] for vertice in face]]
        ax.add_collection3d(plt.Polygon(poly3d, alpha=0.5, edgecolor='k'))

    # Set limits and labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Set aspect ratio
    ax.set_box_aspect([1,1,1])  # Equal aspect ratio
    ax.set_title(title)
    
    plt.show()

def plot_performance_metrics(metrics, title='Model Performance'):
    epochs = range(1, len(metrics['loss']) + 1)
    
    plt.figure()
    plt.plot(epochs, metrics['loss'], label='Loss')
    plt.plot(epochs, metrics['accuracy'], label='Accuracy')
    
    plt.title(title)
    plt.xlabel('Epochs')
    plt.ylabel('Metrics')
    plt.legend()
    plt.show()