## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\




import csv
import requests
from io import StringIO

def get_csv_data(pastebin_url):
    try:
        response = requests.get(pastebin_url)
        if response.status_code == 200:
            csv_data = response.text
            csv_reader = csv.DictReader(StringIO(csv_data), delimiter=';')
            data = [row for row in csv_reader]
            return data
        else:
            print("Failed to retrieve data from the URL.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return None

def get_country_full_name(slug):
    for country in countries_data:
        if country['slug'] == slug:
            return country.get('name', 'Country Name not found')
    return "Country not found"

def display_country_info(country_name, value, world_rank, region, info_type):
    print(f"\n[ - Country: {country_name} - ]\n")
    print(f"Country Information ({info_type}):")
    print(f"{info_type.capitalize()}: {value}")
    print(f"World Rank: {world_rank}")
    print(f"Region: {region}\n")

area_data_url = "https://pastebin.com/raw/cJEEN14b"
population_data_url = "https://pastebin.com/raw/NhpYZyUT"
countries_data = get_csv_data(area_data_url)
population_data = get_csv_data(population_data_url)

if countries_data and population_data:
    while True:
        print("Options:")
        print("[1] Area")
        print("[2] Population")
        print("[3] Exit")

        user_choice = input("\nEnter your choice: ")

        if user_choice == '1':
            print("\nSelect a country:\n")
            for idx, country in enumerate(countries_data, 1):
                print(f"[{idx}] {country['slug']}")

            selected_idx = input("\nEnter the number of the country: ")
            if selected_idx.isdigit() and 1 <= int(selected_idx) <= len(countries_data):
                selected_slug = countries_data[int(selected_idx) - 1]['slug']
                selected_country_name = get_country_full_name(selected_slug)
                selected_area_value = countries_data[int(selected_idx) - 1]['value']
                selected_world_rank = countries_data[int(selected_idx) - 1]['ranking']
                selected_region = countries_data[int(selected_idx) - 1]['region']
                display_country_info(selected_country_name, selected_area_value, selected_world_rank, selected_region, "area")
            else:
                print("Invalid selection. Please choose a valid number.\n")
        elif user_choice == '2':
            print("\nSelect a country:\n")
            for idx, country in enumerate(population_data, 1):
                print(f"[{idx}] {country['slug']}")

            selected_idx = input("\nEnter the number of the country: ")
            if selected_idx.isdigit() and 1 <= int(selected_idx) <= len(population_data):
                selected_slug = population_data[int(selected_idx) - 1]['slug']
                selected_country_name = get_country_full_name(selected_slug)
                selected_population = population_data[int(selected_idx) - 1]['value']
                selected_world_rank = population_data[int(selected_idx) - 1]['ranking']
                selected_region = population_data[int(selected_idx) - 1]['region']
                display_country_info(selected_country_name, selected_population, selected_world_rank, selected_region, "population")
            else:
                print("Invalid selection. Please choose a valid number.\n")
        elif user_choice == '3':
            print("Exiting the CIA World Factbook. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")





## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\
## /-- Made by https://github.com/BotEverything (If you are going to distribute this please credit me :D) --\