import pandas as pd
import numpy as np
from prophet import Prophet

def load_data(file_path):
    # Load data from a CSV file
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    # Perform data preprocessing (e.g., column renaming, data type conversion)
    data["date"] = pd.to_datetime(data["date"], format='%Y-%m-%d')
    data['year'] = data['date'].dt.year
    data["month"] = data["date"].dt.month
    return data

def forecast_weather(data):
    # Forecast weather using the Facebook Prophet model
    model = Prophet()
    forecast_data = data.rename(columns={"date": "ds", "meantemp": "y"})
    model.fit(forecast_data)
    forecasts = model.make_future_dataframe(periods=365)
    predictions = model.predict(forecasts)
    return predictions

if __name__ == "__main__":
    data = load_data("DailyDelhiClimateTrain.csv")
    processed_data = preprocess_data(data)
    predictions = forecast_weather(processed_data)
    print(predictions.head())  # For example, print the forecasted data
