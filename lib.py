"""
File that shares the common code between the script and notebook
"""
import pandas as pd
import matplotlib.pyplot as plt


def load_data(filename):
    return pd.read_csv(filename)


def display_dataset_head(data):
    return data.head()


def display_basic_statistics(data):
    description = data.describe().round(2)
    description.loc['median'] = data.median()
    return description


def create_visualization(data):
    # Plotting Salary distribution as an example
    data['Salary'].plot(kind='bar')
    plt.title('Salary Distribution')
    plt.xlabel('Index')
    plt.ylabel('Salary')
    plt.show()