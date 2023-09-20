# File that shares the common code between the script and notebook
import pandas as pd
import matplotlib.pyplot as plt


def load_data(filename):
    return pd.read_csv(filename)


def display_dataset_head(data):
    print("Dataset Head:")
    print(data.head())
    print("\n")


def display_basic_statistics(data):
    print("Basic Descriptive Statistics:")
    print(data.describe())
    print("\n")


def generate_summary_statistics(data):
    print("Mean:\n", data.mean())
    print("\nMedian:\n", data.median())
    print("\nStandard Deviation:\n", data.std())
    print("\n")


def create_visualization(data):
    # Plotting Salary distribution as an example
    data['Salary'].plot(kind='bar')
    plt.title('Salary Distribution')
    plt.xlabel('Index')
    plt.ylabel('Salary')
    plt.show()