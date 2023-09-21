import unittest
from unittest.mock import patch, Mock
import script  # Assuming the provided code is in a file named script.py
import pandas as pd


class TestLibFunctions(unittest.TestCase):
    # Test if data loading function returns expected output format
    def test_load_data(self):
        data = script.lib.load_data('data.csv')
        self.assertIsInstance(data, pd.DataFrame)
        self.assertGreater(len(data), 0)


    # This is a mock test for demonstration. Replace it with your actual testing logic.
    def test_display_dataset_head(self):
        result = script.lib.display_dataset_head(script.lib.load_data('data.csv'))
        self.assertIsNotNone(result)

class TestScript(unittest.TestCase):

    @patch('script.lib.load_data')
    @patch('script.lib.display_dataset_head')
    @patch('script.lib.display_basic_statistics')
    @patch('script.lib.create_visualization')
    def test_main_function(self, mock_create_visualization,
                           mock_display_basic_statistics,
                           mock_display_dataset_head,
                           mock_load_data):
        # Mocking the return values
        mock_data = Mock()
        mock_load_data.return_value = mock_data
        mock_display_dataset_head.return_value = "Head"
        mock_display_basic_statistics.return_value = "Statistics"

        with patch('script.print') as mock_print:
            script.main()

        # Assert functions were called
        mock_load_data.assert_called_once_with('data.csv')
        mock_display_dataset_head.assert_called_once_with(mock_data)
        mock_display_basic_statistics.assert_called_once_with(mock_data)
        mock_create_visualization.assert_called_once_with(mock_data)

        # Check that the print function was called with the expected values
        mock_print.assert_any_call("Dataset Head:")
        mock_print.assert_any_call("Head")
        mock_print.assert_any_call("\n")
        mock_print.assert_any_call("Basic Descriptive Statistics:")
        mock_print.assert_any_call("Statistics")
        mock_print.assert_any_call("\n")

if __name__ == '__main__':
    unittest.main()
