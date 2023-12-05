import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.neighbors import kneighbors_graph

def add_noise(x, y, amplitude):
    """
    Add noise to the data.
    """
    X = np.concatenate((x, y))
    X += amplitude * np.random.randn(2, X.shape[1])
    return X.T

def get_spiral(t, noise_amplitude=0.5):
    """
    Generate a spiral dataset with noise.
    """
    r = t
    x = r * np.cos(t)
    y = r * np.sin(t)

    return add_noise(x, y, noise_amplitude)

def get_rose(t, noise_amplitude=0.02):
    """
    Generate a rose (rhodonea curve) dataset with noise.
    """
    k = 5
    r = np.cos(k*t) + 0.25
    x = r * np.cos(t)
    y = r * np.sin(t)

    return add_noise(x, y, noise_amplitude)

def get_hypotrochoid(t, noise_amplitude=0):
    """
    Generate a hypotrochoid dataset with noise.
    """
    a, b, h = 10.0, 2.0, 4.0
    x = (a - b) * np.cos(t) + h * np.cos((a - b) / b * t)
    y = (a - b) * np.sin(t) - h * np.sin((a - b) / b * t)

    return add_noise(x, y, 0)

def perform_clustering(X, connectivity, title, num_clusters=3, linkage='ward'):
    """
    Perform and plot agglomerative clustering.
    """
    plt.figure(figsize=(8, 6))
    model = AgglomerativeClustering(linkage=linkage,
                                    connectivity=connectivity,
                                    n_clusters=num_clusters)
    model.fit(X)

    labels = model.labels_
    markers = ['o', 's', 'D']  # More distinguishable markers

    for i, marker in zip(range(num_clusters), markers):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], s=50,
                    marker=marker, label=f'Cluster {i+1}')

    plt.title(title, fontsize=14)
    plt.xlabel('X-axis', fontsize=12)
    plt.ylabel('Y-axis', fontsize=12)
    plt.legend()
    plt.grid(True)

if __name__ == '__main__':
    # Generate sample data
    n_samples = 500
    np.random.seed(2)
    t = 2.5 * np.pi * (1 + 2 * np.random.rand(1, n_samples))
    X = get_spiral(t)

    # No connectivity
    perform_clustering(X, None, 'No Connectivity')

    # K-Neighbors graph connectivity
    kneighbors = 10  # Parameterize for flexibility
    connectivity = kneighbors_graph(X, kneighbors, include_self=False)
    perform_clustering(X, connectivity, 'K-Neighbors Connectivity')

    plt.show()
