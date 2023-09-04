import subprocess
import csv
import requests
from io import StringIO
import os
from colorama import Fore, Style
import time
import webbrowser
import datetime


WEBHOOK_URL = ''

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_screen()
area_data_url = "https://pastebin.com/raw/cJEEN14b"
population_data_url = "https://pastebin.com/raw/NhpYZyUT"
median_age_url = "https://pastebin.com/raw/UJNGHkxJ"
population_growth_rate_url = "https://pastebin.com/raw/E5uQ7wGp"
birth_rate_url = "https://pastebin.com/raw/MFMsMFJL"
death_rate_url = "https://pastebin.com/raw/r4VM8YtZ"

faq = [
    "Q1. How can I contact support?",
    "A1. You can contact our support team by sending an email to support@example.com.",
    "Q2. What are the support hours?",
    "A2. Our support team is available from 9 AM to 5 PM, Monday to Friday.",
    "Q3. Can I submit a support ticket online?",
    "A3. Yes, you can submit a support ticket through our online portal on our website."
]
def get_csv_data(pastebin_url, description):
    print(f"Loading {description}...")
    start_time = time.time()
    try:
        response = requests.get(pastebin_url)
        if response.status_code == 200:
            csv_data = response.text
            csv_reader = csv.DictReader(StringIO(csv_data), delimiter=';')
            data = [row for row in csv_reader]
            print(f"{len(data)} {description} loaded in {time.time() - start_time:.2f} seconds.")
            return data
        else:
            print(f"Failed to retrieve {description} data from the URL.")
    except Exception as e:
        print(f"An error occurred while loading {description}: {str(e)}")
    return None
def download_data(url, description):
    print(f"Downloading {description}...")
    start_time = time.time()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{description} downloaded in {time.time() - start_time:.2f} seconds.")
            return response.text
        else:
            print(f"Failed to retrieve {description} data from the URL.")
    except Exception as e:
        print(f"An error occurred while downloading {description}: {str(e)}")
    return None
current_time = datetime.datetime.now().time()
current_date = datetime.datetime.now().date()
def send_request_to_webhook(request, name, contact):\
    
    embed = {
        "title": "New Request!",
        "description": f"**Request**: {request}\n**Name**: {name}\n**Contact**: {contact}\n**Time**: {current_time}\n**Date**: {current_date}",
        "color": 0xFF5733
    }
    message = {
        "embeds": [embed],
    }
    response = requests.post(WEBHOOK_URL, json=message)
    if response.status_code == 204:
        print("\nRequest sent successfully to the webhook.\n")
    else:
        print(f"\nFailed to send the request to the webhook. Status code: {response.status_code}\n")
def get_version_info(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            version_line = [line for line in content.split('\n') if 'Version' in line]
            if version_line:
                version_info = version_line[0].split(':')[-1].strip()
                return version_info
            else:
                return 'Version information not found.'
        else:
            return 'Failed to retrieve Pastebin content.'
    except Exception as e:
        return f'An error occurred: {str(e)}'
def check_ping(url, description):
    print(f"Pinging ({url})...")
    start_time = time.time()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Ping to {description} successful in {time.time() - start_time:.2f} seconds.")
        else:
            print(f"Ping to {description} failed.")
    except Exception as e:
        print(f"Ping to {description} failed: {str(e)}")
def load_countries_data():
    area_data_url = "https://pastebin.com/raw/cJEEN14b"
    return get_csv_data(area_data_url, "countries data")
def load_population_data():
    population_data_url = "https://pastebin.com/raw/NhpYZyUT"
    return get_csv_data(population_data_url, "population data")
def load_medianage_data():
    median_age_url = "https://pastebin.com/raw/NhpYZyUT"
    return get_csv_data(median_age_url, "median age data")
def load_populationgrowth_data():
    population_growth_rate_url = "https://pastebin.com/raw/NhpYZyUT"
    return get_csv_data(population_growth_rate_url, "population growth data")
def load_birthrate_data():
    birth_rate_url = "https://pastebin.com/raw/NhpYZyUT"
    return get_csv_data(birth_rate_url, "birth rate data")
def load_deathrate_data():
    death_rate_url = "https://pastebin.com/raw/NhpYZyUT"
    return get_csv_data(death_rate_url, "death rate data")
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
def discord_menu():
    clear_screen()
    print("/ -+ Discord +- \\")
    print("\n[1] Copy Discord Invite")
    print("[2] Redirect to Discord Web")
    print("[3] Open Discord App")
def support_menu():
    clear_screen()
    print("/ -+ Support +- \\")
    print("\nFAQ --\n")
    for idx, item in enumerate(faq, start=1):
        print(f"{idx}. {item}\n")
def misc_menu():
    clear_screen()
    print(f'Version: {version}\n')
    print(Fore.LIGHTBLUE_EX + "Misc Options:")
    print(Fore.GREEN + "[1]", Fore.WHITE + "Support")
    print(Fore.GREEN + "[2]", Fore.WHITE + "Discord")
    print(Fore.GREEN + "[3]", Fore.WHITE + "CIA Factbook Website")
    print(Fore.GREEN + "[4]", Fore.WHITE + "Submit Request")
    print(Fore.RED + "[5] Back to Main Menu")
    print(Style.RESET_ALL)
def main_menu():
    clear_screen()
    print(f'Version: {version}\n')
    print(Fore.LIGHTBLUE_EX + "Options:")
    print(Fore.GREEN + "[1]", Fore.WHITE + "Area")
    print(Fore.GREEN + "[2]", Fore.WHITE + "Population")
    print(Fore.GREEN + "[3]", Fore.WHITE + "Median Age")
    print(Fore.GREEN + "[4]", Fore.WHITE + "Population Growth Rate")
    print(Fore.GREEN + "[5]", Fore.WHITE + "Birth Rate")
    print(Fore.GREEN + "[6]", Fore.WHITE + "Death Rate")
    print(Fore.GREEN + "[7]", Fore.WHITE + "Misc")
    print(Fore.RED + "[8] Exit")
    print(Fore.YELLOW + "Soon: Net Migration Rate, Maternal mortality ratio, Infant mortality rate, Life expectancy at birth, total fertility rate.")
    print(Style.RESET_ALL)
countries_data = load_countries_data()
if countries_data is None:
    exit(1)
population_data = load_population_data()
if population_data is None:
    exit(1)
medianage_data = load_medianage_data()
if medianage_data is None:
    exit(1)
populationgrowth_data = load_populationgrowth_data()
if populationgrowth_data is None:
    exit(1)
birthrate_data = load_birthrate_data()
if birthrate_data is None:
    exit(1)
deathrate_data = load_deathrate_data()
if deathrate_data is None:
    exit(1)
check_ping("https://pastebin.com", "Pastebin")
check_ping("https://cia.gov/", "CIA website")
pastebin_url = "https://pastebin.com/raw/HU5L8N8V"
version = get_version_info(pastebin_url)
countries_data = get_csv_data(area_data_url, "countries data")
population_data = get_csv_data(population_data_url, "population data")
medianage_data = get_csv_data(median_age_url,"median age data")
populationgr = get_csv_data(population_growth_rate_url,"population growth data")
birthrate = get_csv_data(birth_rate_url,"birth rate data")
deathrate = get_csv_data(death_rate_url,"death rate data")
if countries_data and population_data and medianage_data and populationgr and birthrate and deathrate:
    while True:
        main_menu()
        user_choice = input("\nEnter your choice: ")
        if user_choice == '1':
            clear_screen()
            print("\nSelect a country:\n")
            for idx, country in enumerate(countries_data, 1):
                print(f"[{idx}] {country['slug']}")
            selected_idx = input("\nEnter the number of the country: ")
            clear_screen()
            if selected_idx.isdigit() and 1 <= int(selected_idx) <= len(countries_data):
                selected_slug = countries_data[int(selected_idx) - 1]['slug']
                selected_country_name = get_country_full_name(selected_slug)
                selected_area_value = countries_data[int(selected_idx) - 1]['value']
                selected_world_rank = countries_data[int(selected_idx) - 1]['ranking']
                selected_region = countries_data[int(selected_idx) - 1]['region']
                display_country_info(selected_country_name, selected_area_value, selected_world_rank, selected_region, "area")
                input("\nPress Enter to return to the main menu...")
            else:
                print("Invalid selection. Please choose a valid number.\n")
        elif user_choice == '2':
            clear_screen()
            print("\nSelect a country:\n")
            for idx, country in enumerate(population_data, 1):
                print(f"[{idx}] {country['slug']}")
            selected_idx = input("\nEnter the number of the country: ")
            clear_screen()
            if selected_idx.isdigit() and 1 <= int(selected_idx) <= len(population_data):
                selected_slug = population_data[int(selected_idx) - 1]['slug']
                selected_country_name = get_country_full_name(selected_slug)
                selected_population = population_data[int(selected_idx) - 1]['value']
                selected_world_rank = population_data[int(selected_idx) - 1]['ranking']
                selected_region = population_data[int(selected_idx) - 1]['region']
                display_country_info(selected_country_name, selected_population, selected_world_rank, selected_region, "population")
                input("\nPress Enter to return to the main menu...")
            else:
                print("Invalid selection. Please choose a valid number.\n")
        elif user_choice == '3':
            clear_screen()
            print("\nSelect a country:\n")
            for idx, country in enumerate(medianage_data, 1):
                print(f"[{idx}] {country['slug']}")
            selected_idx = input("\nEnter the number of the country: ")
            clear_screen()
            if selected_idx.isdigit() and 1 <= int(selected_idx) <= len(medianage_data):
                selected_slug = medianage_data[int(selected_idx) - 1]['slug']
                selected_country_name = get_country_full_name(selected_slug)
                selected_population = medianage_data[int(selected_idx) - 1]['value']
                selected_world_rank = medianage_data[int(selected_idx) - 1]['ranking']
                selected_region = medianage_data[int(selected_idx) - 1]['region']
                display_country_info(selected_country_name, selected_population, selected_world_rank, selected_region, "median age")
                input("\nPress Enter to return to the main menu...")
            else:
                print("Invalid selection. Please choose a valid number.\n")
        elif user_choice == '4':
            clear_screen()
            print("\nSelect a country:\n")
            for idx, country in enumerate(populationgr, 1):
                print(f"[{idx}] {country['slug']}")
            selected_idx = input("\nEnter the number of the country: ")
            clear_screen()
            if selected_idx.isdigit() and 1 <= int(selected_idx) <= len(populationgr):
                selected_slug = populationgr[int(selected_idx) - 1]['slug']
                selected_country_name = get_country_full_name(selected_slug)
                selected_population = populationgr[int(selected_idx) - 1]['value']
                selected_world_rank = populationgr[int(selected_idx) - 1]['ranking']
                selected_region = populationgr[int(selected_idx) - 1]['region']
                display_country_info(selected_country_name, selected_population, selected_world_rank, selected_region, "population growth rate")
                input("\nPress Enter to return to the main menu...")
            else:
                print("Invalid selection. Please choose a valid number.\n")
        elif user_choice == '5':
            clear_screen()
            print("\nSelect a country:\n")
            for idx, country in enumerate(birthrate, 1):
                print(f"[{idx}] {country['slug']}")
            selected_idx = input("\nEnter the number of the country: ")
            clear_screen()
            if selected_idx.isdigit() and 1 <= int(selected_idx) <= len(birthrate):
                selected_slug = birthrate[int(selected_idx) - 1]
                selected_slug = birthrate[int(selected_idx) - 1]['slug']
                selected_country_name = get_country_full_name(selected_slug)
                selected_population = birthrate[int(selected_idx) - 1]['value']
                selected_world_rank = birthrate[int(selected_idx) - 1]['ranking']
                selected_region = birthrate[int(selected_idx) - 1]['region']
                display_country_info(selected_country_name, selected_population, selected_world_rank, selected_region, "birth rate")
                input("\nPress Enter to return to the main menu...")
            else:
                print("Invalid selection. Please choose a valid number.\n")
        elif user_choice == '6':
            clear_screen()
            print("\nSelect a country:\n")
            for idx, country in enumerate(deathrate, 1):
                print(f"[{idx}] {country['slug']}")
            selected_idx = input("\nEnter the number of the country: ")
            clear_screen()
            if selected_idx.isdigit() and 1 <= int(selected_idx) <= len(deathrate):
                selected_slug = deathrate[int(selected_idx) - 1]['slug']
                selected_country_name = get_country_full_name(selected_slug)
                selected_population = deathrate[int(selected_idx) - 1]['value']
                selected_world_rank = deathrate[int(selected_idx) - 1]['ranking']
                selected_region = deathrate[int(selected_idx) - 1]['region']
                display_country_info(selected_country_name, selected_population, selected_world_rank, selected_region, "death rate")
                input("\nPress Enter to return to the main menu...")
            else:
                print("Invalid selection. Please choose a valid number.\n")
        elif user_choice == '7':
            while True:
                misc_menu()
                misc_choice = input("\nEnter your choice: ")

                if misc_choice == '1':
                    support_menu()
                    support_choice = input("\nEnter your choice (B to go back to Misc menu): ")
                    if support_choice.lower() == 'b':
                        break
                    else:
                        try:
                            selected_question = int(support_choice)
                            if 1 <= selected_question <= len(faq):
                                clear_screen()
                                print("/ -+ Support +- \\")
                                print(f"\nFAQ --\n")
                                print(f"{faq[selected_question - 1]}\n")
                                input("Press Enter to continue...")
                            else:
                                print("Invalid choice. Please select a valid FAQ number or 'B' to go back.\n")
                        except ValueError:
                            print("Invalid choice. Please select a valid FAQ number or 'B' to go back.\n")
                elif misc_choice == '2':
                    while True:
                        discord_menu()
                        discord_choice = input("\nEnter your choice (B to go back to Misc menu): ")
                        if discord_choice.lower() == 'b':
                            break
                        elif discord_choice == '1':
                            invite_link = "https://discord.gg/vxMVq2d4S6"
                            input(f"\nDiscord Invite Link: {invite_link}\nPress Enter to continue...")
                        elif discord_choice == '2':
                            web_url = "https://discord.gg/vxMVq2d4S6"
                            webbrowser.open(web_url)
                            input(f"\nRedirecting to Discord Web: {web_url}\nPress Enter to continue...")
                        elif discord_choice == '3':
                            app_url = "discord://"
                            try:
                                webbrowser.open(app_url)
                                input("\nOpening Discord App...\nPress Enter to continue...")
                            except Exception as e:
                                print(f"Failed to open Discord app: {str(e)}")
                        else:
                            print("Invalid choice. Please select a valid option or 'B' to go back.\n")
                elif misc_choice == '3':
                    factbook_url = "https://www.cia.gov/the-world-factbook/"
                    webbrowser.open(factbook_url)
                    input(f"\nRedirecting to the CIA World Factbook: {factbook_url}\nPress Enter to continue...")
                elif misc_choice == '4':
                            clear_screen()
                            print("[-] Requesting: (more info, a new feature etc)")
                            request = input("[-] Request: ")
                            name = input("[-] Name: ")
                            contact = input("[-] Contact: ")

                            send_request_to_webhook(request, name, contact)
                            print("\nRequest sent successfully to the webhook.\n")
                elif misc_choice == '5':
                    break
                else:
                    print("Invalid choice. Please select a valid option.\n")
        elif user_choice == '8':
            print(Fore.RED+"Exiting",Fore.WHITE+"the Central Intelligence Agency's World",Fore.MAGENTA+"Factbook")
            print(Fore.RESET)
            break
        else:
            print("Invalid choice. Please select a valid option.\n")
