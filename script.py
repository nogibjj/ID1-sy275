"""
App entry point: Python Script file which perform the descriptive statistics
                on the data by Pandas and Matplotlib

# Note: This script assumes that all columns in data.csv are numeric.
# If there are non-numeric columns, you'd need to handle
    or exclude them when computing these statistics.
"""

import lib


def main():
    data = lib.load_data('data.csv')

    print("Dataset Head:")
    print(lib.display_dataset_head(data))
    print("\n")

    print("Basic Descriptive Statistics:")
    print(lib.display_basic_statistics(data))
    print("\n")

    lib.create_visualization(data)


if __name__ == "__main__":
    main()

