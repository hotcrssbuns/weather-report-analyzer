import pandas as pd
from datetime import datetime

# Constants
CITIES = [
    "New York",
    "Los Angeles",
    "Chicago",
    "Houston",
    "Phoenix",
    "Philadelphia",
    "San Antonio",
    "San Diego",
    "Dallas",
    "San Jose",
]


# Utility Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def kmh_to_mph(kmh):
    return kmh * 0.621371


# Analysis Functions
def load_weather_data():
    """Load the weather data from CSV file"""
    return pd.read_csv("data/weather_data.csv")


def get_city_stats(weather_data, city):
    """Calculate average weather statistics for a given city"""
    city_data = weather_data[weather_data["Location"] == city]

    max_temp_index = city_data["Temperature_C"].idxmax()
    min_temp_index = city_data["Temperature_C"].idxmin()

    max_date = datetime.strptime(
        city_data.loc[max_temp_index, "Date_Time"], "%Y-%m-%d %H:%M:%S"
    )
    min_date = datetime.strptime(
        city_data.loc[min_temp_index, "Date_Time"], "%Y-%m-%d %H:%M:%S"
    )

    return {
        "average_temp": city_data["Temperature_C"].mean(),
        "average_humidity": city_data["Humidity_pct"].mean(),
        "average_precipitation": city_data["Precipitation_mm"].mean(),
        "average_windspeed": city_data["Wind_Speed_kmh"].mean(),
        "max_temp": city_data["Temperature_C"].max(),
        "max_temp_date": max_date,
        "min_temp": city_data["Temperature_C"].min(),
        "min_temp_date": min_date,
    }


def calculate_city_averages(df):
    """Calculate average temperatures for all cities"""
    return df.groupby("Location")[["Temperature_C"]].mean()


def calculate_rainy_days(df): ...
