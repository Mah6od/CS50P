import unittest
import pandas as pd
from project import load_data, preprocess_data, forecast_weather

class TestClimateAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load sample data for testing
        cls.sample_data = pd.read_csv("sample_data.csv")

    def test_load_data(self):
        # Test the load_data function
        data = load_data("sample_data.csv")
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(data.shape[0], len(self.sample_data))

    def test_preprocess_data(self):
        # Test the preprocess_data function
        processed_data = preprocess_data(self.sample_data)
        self.assertIsInstance(processed_data, pd.DataFrame)
        self.assertIn("date", processed_data.columns)
        self.assertIn("year", processed_data.columns)
        self.assertIn("month", processed_data.columns)

    def test_forecast_weather(self):
        # Test the forecast_weather function
        predictions = forecast_weather(self.sample_data)
        self.assertIsInstance(predictions, pd.DataFrame)
        self.assertTrue("ds" in predictions.columns and "yhat" in predictions.columns)

if __name__ == '__main__':
    unittest.main()
