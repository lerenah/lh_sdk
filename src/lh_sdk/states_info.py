from pathlib import Path
import json
from typing import List

THIS_DIR = Path(__file__).parent

CITIES_JSON_FPATH = THIS_DIR / 'cities.json'

def is_city_capitol_of_state(city: str, state: str) -> bool:
    cities_json_contents = CITIES_JSON_FPATH.read_text()
    cities_matched = json.loads(cities_json_contents)
    matching_cities: List[dict] = [city for city in cities_matched[state]]
    return city in matching_cities

if __name__ == '__main__':
    print(is_city_capitol_of_state('Sacramento', 'CA'))  # True
    # with open(CITIES_JSON_FPATH) as f:
    #     cities = json.load(f)
    # return city in cities[state]