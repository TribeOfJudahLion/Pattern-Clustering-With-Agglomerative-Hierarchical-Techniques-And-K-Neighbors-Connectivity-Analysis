<br/>
<p align="center">
  <h3 align="center">Unlock the Mysteries of Complex Patterns: Master Clustering with Agglomerative Hierarchical Techniques</h3>

  <p align="center">
    Dive into the Depths of Data with K-Neighbors Connectivity Analysis!
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Scenario

**Context**: A research team is working on a biological study examining the growth patterns of a certain type of bacteria. The bacteria exhibit a unique growth pattern that resembles complex mathematical shapes such as spirals, rose curves, and hypotrochoids under a microscope. The team needs to classify the bacteria based on the similarity of these growth patterns to better understand the different bacterial strains.

**Challenge**: The growth patterns are not uniform due to varying environmental factors, which introduces noise in the visual data. The team needs an algorithmic solution to accurately cluster the bacteria despite the noise and complexity of the patterns.

**Data Characteristics**:
- The growth patterns are captured in a two-dimensional space, with each point representing the position of a bacterial colony.
- The noise in the data represents the random variations in the growth patterns due to environmental factors.

### Solution Using the Provided Code

**Step 1: Data Preparation**
- The team decides to simulate the bacterial growth patterns mathematically using the provided code to generate spirals, rose curves, and hypotrochoids.
- They introduce a controlled amount of noise to the simulated data to represent environmental variations.

**Step 2: Clustering without Connectivity**
- Initially, the team uses the `perform_clustering` function without connectivity to cluster the bacteria based solely on the spatial proximity of the growth patterns.
- They visualize the results and notice that the clustering is not accurate due to the lack of consideration for the inherent shapes of the growth patterns.

**Step 3: Clustering with K-Neighbors Connectivity**
- To improve the clustering accuracy, they use the `kneighbors_graph` to create a connectivity graph that captures the local structure of the data.
- They then run the `perform_clustering` function with the K-Neighbors connectivity, which now takes into account the shape of the growth patterns when clustering.

**Step 4: Analysis and Interpretation**
- The team compares the clustering results with and without connectivity. They find that using the K-Neighbors graph results in clusters that align more closely with the actual shapes of the bacterial growth patterns.
- This approach allows them to differentiate between different bacterial strains more effectively, despite the noise in the data.

**Step 5: Practical Application**
- With the successful clustering of the simulated data, the team proceeds to apply the algorithm to real microscopic images of the bacteria.
- They use image processing techniques to extract the growth patterns from the images and then apply the same clustering technique to classify the bacterial strains.

**Conclusion**: By leveraging hierarchical agglomerative clustering with and without connectivity constraints, the team is able to classify the bacteria based on their growth patterns accurately. This methodology can potentially be used to study various other biological and ecological phenomena that exhibit complex patterns.

This Python script demonstrates the use of hierarchical agglomerative clustering on different datasets, showcasing how connectivity affects the clustering results. 

1. **Importing Libraries**: The script imports necessary libraries: `numpy` for numerical operations, `matplotlib.pyplot` for plotting, `AgglomerativeClustering` for clustering, and `kneighbors_graph` for creating a k-neighbors graph.

2. **Function `add_noise`**: 
   - Purpose: To add random noise to a dataset.
   - Parameters: `x`, `y` (data points), `amplitude` (noise amplitude).
   - Functionality: Concatenates `x` and `y`, then adds Gaussian noise to the data.

3. **Function `get_spiral`**:
   - Purpose: Generate a spiral-shaped dataset.
   - Parameters: `t` (angle), `noise_amplitude` (noise level).
   - Functionality: Computes x and y coordinates for a spiral, then adds noise using `add_noise`.

4. **Function `get_rose`**:
   - Purpose: Create a rose (rhodonea curve) shaped dataset.
   - Parameters: Similar to `get_spiral`.
   - Functionality: Computes a rose pattern with a parameter `k` determining the number of petals, then adds noise.

5. **Function `get_hypotrochoid`**:
   - Purpose: Generate a hypotrochoid-shaped dataset.
   - Parameters: `t`, `noise_amplitude`.
   - Functionality: Uses parameters `a`, `b`, `h` to define the hypotrochoid shape, then adds noise.

6. **Function `perform_clustering`**:
   - Purpose: Perform and plot hierarchical agglomerative clustering.
   - Parameters: `X` (dataset), `connectivity` (graph connectivity), `title` (plot title), `num_clusters` (number of clusters), `linkage` (clustering method).
   - Functionality: Initializes `AgglomerativeClustering`, fits the model to the data, and then plots the clusters with different markers for visual distinction.

7. **Main Execution Block**:
   - Generates a sample spiral dataset.
   - Performs clustering twice, once without any connectivity (`None`) and once using a K-Neighbors graph for connectivity.
   - Visualizes the results using `matplotlib`.

8. **Clustering Techniques**:
   - **Without Connectivity**: Clusters based solely on the proximity of data points.
   - **With K-Neighbors Connectivity**: Uses the k-nearest neighbors to create a connectivity graph, influencing the clustering by considering local neighborhood structure.

9. **Visualization**:
   - The script plots the results of both clustering approaches, highlighting the impact of considering local connectivity in clustering.

10. **Usage**:
   - This script can be used to analyze how different data shapes (like spirals, roses, hypotrochoids) are clustered with and without considering the local neighborhood of points.
   - It's particularly useful for understanding the effects of connectivity in hierarchical agglomerative clustering.

Each plot represents the results of clustering with and without the use of connectivity constraints.

### K-Neighbors Connectivity Plot
In this plot, the clustering algorithm used the K-Neighbors graph to incorporate local neighborhood information into the clustering process. Here's what we can infer:

- **Clusters**: There are three distinct clusters, each marked with different shapes and colors (orange squares, blue circles, and green diamonds).
- **Shape**: The clusters follow the spiral pattern of the dataset closely, which suggests that incorporating the K-Neighbors graph has allowed the algorithm to respect the local structure of the data.
- **Boundaries**: The transition between clusters appears smooth, with each cluster occupying a contiguous segment of the spiral. This contiguity is likely due to the algorithm considering the connectivity information, which prevents it from making abrupt changes in cluster assignments over neighboring points.

### No Connectivity Plot
This plot represents clustering without considering the local structure explicitly; the algorithm only uses the distances between points to form clusters.

- **Clusters**: As with the previous plot, there are three clusters differentiated by shape and color.
- **Shape**: The clusters are less contiguous along the spiral compared to the first plot. This suggests that without the local structure information, the algorithm is more prone to assign neighboring points to different clusters based solely on distance.
- **Boundaries**: The boundaries between clusters are less smooth, and there's more intermixing of clusters along the spiral. This indicates that without connectivity constraints, the algorithm is less effective at capturing the underlying pattern of the data.

### Comparative Analysis
- **Effectiveness**: The clustering with K-Neighbors connectivity appears more effective for this spiral dataset as it respects the inherent structure of the data.
- **Algorithm Behavior**: Without connectivity, the algorithm tends to create clusters based on the global distribution of points, which can result in less accurate clustering for data with complex shapes.

These results are valuable in understanding the importance of choosing the right clustering approach for a given dataset, especially when the dataset has a complex structure that simple distance-based clustering might not capture effectively.

## Built With

The clustering analysis tool is constructed using several state-of-the-art libraries and frameworks within the Python ecosystem. Below is a detailed breakdown of the components used:

- **NumPy (Numerical Python)**: 
  - **Function**: Serves as the backbone for numerical computations in Python, providing support for a wide array of mathematical operations and a powerful N-dimensional array object.
  - **Usage**: In our code, NumPy is used for generating datasets, performing mathematical operations, and handling arrays. For instance, it is used to concatenate arrays and perform operations like cosine and sine for generating spiral, rose, and hypotrochoid datasets.

- **Matplotlib**:
  - **Function**: A plotting library for Python and its numerical mathematics extension, NumPy. It provides an object-oriented API for embedding plots into applications.
  - **Usage**: In this project, Matplotlib is employed to visualize the datasets and the results of the clustering algorithms, aiding in the interpretation of the underlying patterns in the data.

- **Scikit-learn (sklearn)**:
  - **Function**: A machine learning library for Python, featuring various classification, regression, and clustering algorithms, including support vector machines, random forests, gradient boosting, k-means, and DBSCAN, and is designed to interoperate with NumPy and Matplotlib.
  - **Usage**: Within our tool, Scikit-learn's `AgglomerativeClustering` is utilized to perform hierarchical clustering on the datasets. The `kneighbors_graph` function from the same library is used to create a k-neighbors connectivity graph, which influences how the clustering is performed by taking into account the local neighborhood structure of the data.

- **Development Environment**:
  - **Python**: The entire tool is written in Python, chosen for its simplicity and the powerful ecosystem of data science libraries it supports.
  - **Integrated Development Environment (IDE)**: Although not specified, the development of this tool likely took place in an IDE or text editor that supports Python programming, such as PyCharm, Jupyter Notebook, or Visual Studio Code.

- **Version Control**:
  - **Git**: To manage the development process, track changes, and collaborate with other developers, Git is the de facto standard for version control.
  - **GitHub**: Hosting the code on GitHub allows for issue tracking, documentation, and release management.

When listing the tool on GitHub, each "Built With" entry would typically be accompanied by the version of the library or tool used to ensure reproducibility and compatibility for other developers who may want to run or contribute to the project. It is also common to provide links to the project pages or documentation for these tools, so that users can find more information or download them.

## Getting Started

This section will guide you through setting up your system to run the clustering analysis tool. Follow these steps to get a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites

Before you begin, ensure you have the following software installed on your computer:

- **Python**: The project is developed using Python. If you don't have Python installed, download and install it from the official [Python website](https://www.python.org/). This project is compatible with Python 3.6 and above.
- **pip**: pip is the package installer for Python. You can check if you have pip installed by running `pip --version` in your console.

#### Installation

1. **Clone the repository**:
   - Use the following command to clone the project repository to your local machine:
   ```sh
   git clone https://github.com/your-username/your-repository-name.git
   ```
   Replace `your-username` and `your-repository-name` with your GitHub username and the repository name, respectively.

2. **Set up a virtual environment (optional but recommended)**:
   - Navigate to the project directory:
   ```sh
   cd your-repository-name
   ```
   - Create a virtual environment to manage the project's dependencies separately from your system's Python installation:
   ```sh
   python -m venv venv
   ```
   - Activate the virtual environment:
     - On Windows:
     ```sh
     venv\Scripts\activate
     ```
     - On Unix or MacOS:
     ```sh
     source venv/bin/activate
     ```

3. **Install the required packages**:
   - Install all the required packages using `pip`:
   ```sh
   pip install numpy matplotlib scikit-learn
   ```

#### Running the Tool

After you have installed all the required software and packages, you can run the tool using the following steps:

1. **Run the Python script**:
   - Ensure you are in the project directory and your virtual environment is activated.
   - Run the script by typing:
   ```sh
   python clustering_tool.py
   ```
   Replace `clustering_tool.py` with the actual name of the Python script if it is different.

2. **View the Results**:
   - The script will generate plots showing the results of the clustering. These will display in new windows or inline if you're using an IDE like Jupyter Notebook.

3. **Deactivate the Virtual Environment**:
   - Once you're done, you can deactivate the virtual environment by simply running:
   ```sh
   deactivate
   ```

#### Troubleshooting

- If you encounter any errors related to package installations, ensure your pip installer is up to date using `pip install --upgrade pip`.
- If the plots do not display, check that you have a GUI backend installed for Matplotlib.

#### Contributing

If you wish to contribute to this project, please read the `CONTRIBUTING.md` file (if provided by the repository owner) for guidelines on how to make contributions.

With these instructions, you should be able to set up and run the clustering analysis tool smoothly. For any additional help or clarification, refer to the project's `README.md` or open an issue in the GitHub repository.

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/TribeOfJudahLion/Pattern-Clustering-With-Agglomerative-Hierarchical-Techniques-And-K-Neighbors-Connectivity-Analysis/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/TribeOfJudahLion/Pattern-Clustering-With-Agglomerative-Hierarchical-Techniques-And-K-Neighbors-Connectivity-Analysis/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/TribeOfJudahLion/Pattern-Clustering-With-Agglomerative-Hierarchical-Techniques-And-K-Neighbors-Connectivity-Analysis/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
