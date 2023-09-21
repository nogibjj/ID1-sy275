import pandas as pd
import unittest
from unittest.mock import patch

import lib  # Adjusted for the correct module name


class TestDataFunctions(unittest.TestCase):

    def test_load_data(self):
        # Test if data loading function returns a dataframe
        data = lib.load_data('data.csv')
        self.assertIsInstance(data, pd.DataFrame)

    @patch("builtins.print")
    def test_display_dataset_head(self, mock_print):
        # Mock data for test
        data = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

        lib.display_dataset_head(data)

        # Check if print was called (for title, data head, and newline)
        self.assertEqual(mock_print.call_count, 3)

    @patch("builtins.print")
    def test_display_basic_statistics(self, mock_print):
        # Mock data for test
        data = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

        lib.display_basic_statistics(data)

        # Check if print was called
        self.assertEqual(mock_print.call_count, 3)

    @patch("matplotlib.pyplot.show")
    def test_create_visualization(self, mock_show):
        # Mock data for test
        data = pd.DataFrame({'Salary': [50000, 60000, 70000, 80000, 90000]})

        lib.create_visualization(data)

        # Check if show was called to display the plot
        mock_show.assert_called_once()


if __name__ == '__main__':
    unittest.main()
