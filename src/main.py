from weather import CITIES, celsius_to_fahrenheit, get_city_stats, load_weather_data


def main():
    # Load data once at the start
    weather_data = load_weather_data()

    city = input("What city would you like to know more about? ")
    if city in CITIES:
        # Get all stats for the city
        stats = get_city_stats(weather_data, city)
        # Format and display the temperature
        print(f"\n--- Weather Stats for {city} ---")
        print(f"Average Temperature: {stats["average_temp"]:.0f}°F")
        print(f"Average Humidity: {stats["average_humidity"]:.2f}")
        print(f"Average Precipitation: {stats["average_precipitation"]:.2f}")
        print(f"Average Windspeed: {stats["average_windspeed"]:.0f} Kilometers/Hour")
        print(f"Highest Temp: {stats["max_temp"]:.0f}°F")
        print(f"Lowest Temp: {stats["min_temp"]:.0f}°F")
    else:
        print("Invalid city")


if __name__ == "__main__":
    main()
