import pandas as pd
import unittest
from unittest.mock import patch
import lib  # Assuming the provided code is saved in a file named main.py
import matplotlib.pyplot as plt


class TestDataFunctions(unittest.TestCase):

    def setUp(self):
        # Load dataset for testing purposes
        self.data = lib.load_data('data.csv')

    def test_load_data(self):
        self.assertIsInstance(self.data, pd.DataFrame)
        self.assertGreater(len(self.data), 0)

    def test_display_dataset_head(self):
        head = lib.display_dataset_head(self.data)
        self.assertIsInstance(head, pd.DataFrame)
        self.assertEqual(len(head), 5)  # Default of head() is 5 rows

    def test_display_basic_statistics(self):
        stats = lib.display_basic_statistics(self.data)
        # Check if basic statistics includes the median
        self.assertIn('median', stats.index)
        # Further assertions can be made based on the expected content of data.csv

    @patch.object(plt, 'show')
    def test_create_visualization(self, mock_show):
        # Mocking plt.show() to avoid displaying the plot during testing
        lib.create_visualization(self.data)
        mock_show.assert_called_once()


if __name__ == "__main__":
    unittest.main()
