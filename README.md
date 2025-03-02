# Databench 🚀

**Databench** is a demo application designed to showcase the usage of three powerful Python libraries for data processing: **Pandas**, **Dask**, and **Polars**. This demo compares the performance of each library by performing the same transformation on a synthetic dataset and displaying the results side by side.

## Features
- **Synthetic Data Generation**: Generates a sample dataset using the **Faker** library.
- **Library Comparison**: Runs data processing with **Pandas**, **Dask**, and **Polars**, and displays the results side by side.
- **Performance Comparison**: Displays execution times for each library, highlighting their performance on the same task.

## Prerequisites

Make sure you have the following installed:

- Python >= 3.8
- pip (Python package installer)
- uv (pip install uv)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/databench.git
   cd databench
   ```

2. Install the dependencies 
    ```bash
    uv sync
    ```

## Run the system
```bash
uv run streamlit run main.py
```

## Usage
1.	Configure the Dataset:  
Use the sidebar to select the number of rows you want to generate for your dataset.

2.	Processing:  
The app will process the dataset using Pandas, Dask, and Polars, and display the results of a transformation: calculating the average salary grouped by the first letter of each name.

3.	View Results:  
The results will be shown side by side, including the execution time for each library.

