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
    description = data.describe().round(2)
    description.loc['median'] = data.median()
    print(description)
    print("\n")


def create_visualization(data):
    # Plotting Salary distribution as an example
    data['Salary'].plot(kind='bar')
    plt.title('Salary Distribution')
    plt.xlabel('Index')
    plt.ylabel('Salary')
    plt.show()