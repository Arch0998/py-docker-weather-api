import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    URL = "http://api.weatherapi.com/v1/"
    FILTERING = "Paris"

    result = requests.get(URL + f"current.json?key={API_KEY}&q={FILTERING}")

    print(result.json())


if __name__ == "__main__":
    get_weather()
