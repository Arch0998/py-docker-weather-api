import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.environ.get("API_KEY")


def get_weather() -> None:
    url = "http://api.weatherapi.com/v1/"
    filtering = "Paris"

    result = requests.get(url + f"current.json?key={API_KEY}&q={filtering}")

    print(result.json())


if __name__ == "__main__":
    get_weather()
