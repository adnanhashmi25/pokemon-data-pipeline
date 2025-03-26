import requests
import pandas as pd
from datetime import datetime
import csv
import logging
import os

# Detect if running inside Docker
IN_DOCKER = os.path.exists("/.dockerenv")  

# Set save path dynamically
LOCAL_PATH = "pokemon_data.csv"
DOCKER_PATH = "/opt/airflow/dags/pokemon_data.csv"
SAVE_PATH = DOCKER_PATH if IN_DOCKER else LOCAL_PATH  

# Define the API endpoint
base_url = "https://pokeapi.co/api/v2/"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_pokemon_info(name):
    """Fetches Pokémon details from the API."""
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Failed to retrieve {name}. Status Code: {response.status_code}")
        return None

def get_last_pokemon_id():
    """Reads the last processed Pokémon ID from a file."""
    if os.path.exists("last_run.txt"):
        with open("last_run.txt", "r") as file:
            return int(file.read().strip())  # ✅ Now we store an integer (Pokémon ID)
    return 0  # Default to 0 if no previous run

def save_last_pokemon_id(last_id):
    """Saves the latest processed Pokémon ID to a file."""
    with open("last_run.txt", "w") as file:
        file.write(str(last_id))  # ✅ Save the latest Pokémon ID as an integer

def run_etl(pokemon_list):
    """Extracts Pokémon data incrementally and saves it to CSV."""
    logging.info("Starting Pokémon ETL process...")

    last_pokemon_id = get_last_pokemon_id()
    new_data = []
    highest_id = last_pokemon_id  # Track the highest ID processed in this run

    for pokemon in pokemon_list:
        pokemon_info = get_pokemon_info(pokemon)
        if pokemon_info:
            poke_id = pokemon_info.get('id', 0)

            # Skip Pokémon that were already fetched
            if poke_id <= last_pokemon_id:
                continue

            pokemon_data = {
                'name': pokemon_info.get('name', 'N/A'),
                'ID': poke_id,
                'height': pokemon_info.get('height', 0),
                'weight': pokemon_info.get('weight', 0),
            }
            new_data.append(pokemon_data)

            # Track the highest ID fetched
            if poke_id > highest_id:
                highest_id = poke_id

    if new_data:
        df = pd.DataFrame(new_data)
        df.to_csv(SAVE_PATH, mode='a', index=False, header=not os.path.exists(SAVE_PATH))  # Append instead of overwriting
        save_last_pokemon_id(highest_id)  # ✅ Save the last Pokémon ID processed
        logging.info(f"✅ Pokemon data saved successfully as '{SAVE_PATH}'.")

    else:
        logging.warning("⚠ No new Pokémon data was collected.")

if __name__ == "__main__":
    p_list = []
    with open('pokemon_list.csv', 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            p_list.append(row[0])

    run_etl(p_list)
