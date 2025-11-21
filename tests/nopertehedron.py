import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib
matplotlib.use('Qt5Agg') 

# Rotation around z-axis
def Rz(alpha):
    return np.array([
        [np.cos(alpha), -np.sin(alpha), 0],
        [np.sin(alpha),  np.cos(alpha), 0],
        [0, 0, 1]
    ])

# Define the cyclic group C30
def generate_C30():
    elements = []
    for k in range(15):
        angle = 2 * np.pi * k / 15
        R = Rz(angle)
        elements.append(R)
        elements.append(-R)  # (-1)^ℓ factor
    return elements

# Define the seed points
C1 = np.array([152024884, 0, 210152163]) / 259375205
C2 = np.array([6632738028, 6106948881, 3980949609]) / 1e10
C3 = np.array([8193990033, 5298215096, 1230614493]) / 1e10

def orbit(points, group):
    return np.vstack([g @ p for p in points for g in group])

def generate_nopertehedron():
    C30 = generate_C30()
    vertices = orbit([C1, C2, C3], C30)
    hull = ConvexHull(vertices)
    return vertices, hull

# Visualization
def plot_polyhedron(points, hull):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection="3d")

    faces = [points[s] for s in hull.simplices]
    poly3d = Poly3DCollection(faces, alpha=0.5, facecolor='cyan', edgecolor='k')
    ax.add_collection3d(poly3d)
    ax.scatter(points[:,0], points[:,1], points[:,2], color='r', s=10)

    ax.set_box_aspect([1,1,1])
    plt.title("The Nopertehedron")
    plt.show()

if __name__ == "__main__":
    vertices, hull = generate_nopertehedron()
    print("Number of vertices:", len(vertices))
    plot_polyhedron(vertices, hull)
