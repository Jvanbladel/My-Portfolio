import os
import json
import time
from datetime import datetime, timedelta
import requests
from pprint import pprint
from geopy.geocoders import ArcGIS

WEATHER_API_KEY = "aa0e7653d143db0cf797636d6f381086"


def get_location_data(location):
    nom = ArcGIS()
    print(nom.geocode(location))
    return nom.geocode(location)


def parse_location_data(data):
    location_name = data[0]
    long = data[1][1]
    lat = data[1][0]
    return location_name, lat, long


def get_location_name(location):
    try:
        # If JSON file doesn't exist or the data is outdated, make an API call
        location_data = get_location_data(location)
        location_name, lat, long = parse_location_data(location_data)
        return location_name
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while fetching weather data.")
        return "Invalid"


def get_weather(location):
    # Create a directory to store JSON files if it doesn't exist
    if not os.path.exists("weather_data"):
        os.makedirs("weather_data")

    # Check if a JSON file with the location data already exists
    location_file_path = os.path.join("weather_data", location + ".json")

    if os.path.exists(location_file_path):
        with open(location_file_path, "r") as f:
            data = json.load(f)

        # Check if the data is 24 hours old or older
        last_updated_str = data.get("last_updated", None)
        if last_updated_str:
            last_updated = datetime.fromisoformat(last_updated_str)
            if datetime.now() - last_updated >= timedelta(days=1):
                print("Data is 24 hours old. Fetching fresh data from API.")
            else:
                print("Retrieving weather data from the JSON file.")
                return data

    try:
        # If JSON file doesn't exist or the data is outdated, make an API call
        location_data = get_location_data(location)
        location_name, lat, long = parse_location_data(location_data)
        url = "https://api.openweathermap.org/data/3.0/onecall?lat={}&lon={}&appid={}".format(
            lat, long, WEATHER_API_KEY
        )
        res = requests.get(url)

        if res.status_code == 200:
            data = res.json()

            # Save the API response to the JSON file
            data["last_updated"] = datetime.now().isoformat()
            with open(location_file_path, "w") as f:
                json.dump(data, f)

            return data
        else:
            print("Error: Failed to retrieve data from the API.")
    except Exception as e:
        print(f"Error: {e}")
        print("An error occurred while fetching weather data.")
        return None
