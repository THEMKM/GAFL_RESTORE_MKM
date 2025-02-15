import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
def load_data(file_path):
    data = pd.read_stata(file_path)
    return data

# Explore the data
def explore_data(data):
    print("Data Head:")
    print(data.head())
    print("\nData Info:")
    print(data.info())
    print("\nData Description:")
    print(data.describe())
    
    # Plotting pairplot to understand relationships
    sns.pairplot(data)
    plt.show()

# Extract important information
def extract_important_info(data):
    # Example: Extracting columns with high correlation
    correlation_matrix = data.corr()
    high_corr_columns = correlation_matrix[correlation_matrix > 0.8].index.tolist()
    important_data = data[high_corr_columns]
    return important_data

if __name__ == "__main__":
    raw_data_folder = 'Data\\raw'  # Using relative path
    for file_name in os.listdir(raw_data_folder):
        if file_name.endswith('.dta'):
            file_path = os.path.join(raw_data_folder, file_name)
            print(f"Processing file: {file_name}")
            data = load_data(file_path)
            explore_data(data)
            important_data = extract_important_info(data)
            print("Important Data:")
            print(important_data.head())
