import sys
import requests
from time import sleep
from uuid import uuid4
from colorama import init, Fore
from os import system
import subprocess

init(autoreset=True)  # initialize colorama

Creator = "t.me/Amir_Ali667"
session = requests.Session()
session.headers.update({'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; 23049PCD8G Build/TKQ1.221114.001)',
                        'Accept-Encoding': 'gzip',
                        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'})

cr = Creator
restore_key = input("Please enter your restore key: ")


def load():
    data = {
        'game_version': '1.7.10655',
        'device_name': 'unknown',
        'os_version': '10',
        'model': 'SM-A750F',
        'udid': str(uuid4().int),
        'store_type': 'iraqapps',
        'restore_key': restore_key,
        'os_type': 2
    }
    try:
        response = session.post('http://iran.fruitcraft.ir/player/load', data=data, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
        sys.exit(1)
    except ValueError as e:
        print("Error decoding JSON response.")
        sys.exit(1)


def collect_gold(session, data):
    url = "http://iran.fruitcraft.ir/cards/collectgold"
    try:
        response = session.post(url, data=data)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        if response.status_code == 200:
            return response.json()  # Return JSON response if request is successful
        else:
            print(f"Unexpected status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
        return None


def start(sleep_time):
    done = 0
    lost = 0

    try:
        collect_gold(session, collect_data)
        done += 1
    except Exception as e:
        print(e)
        lost += 1
    finally:
        sys.stdout.write(
            f"\r• Gold Mine Done: {Fore.GREEN}{str(done)}{Fore.RESET} --- • Gold Mine Lost: {Fore.RED}{str(lost)}{Fore.RESET}")
        sys.stdout.flush()
        sleep(sleep_time * 60)  # login once after starting

        while True:
            sleep(sleep_time * 60)  # sleep for the specified time in minutes
            try:
                collect_gold(session, collect_data)
                done += 1
            except Exception as e:
                print(e)
                lost += 1
            finally:
                sys.stdout.write(
                    f"\r• Gold Mine Done: {Fore.GREEN}{str(done)}{Fore.RESET} --- • Gold Mine Lost: {Fore.RED}{str(lost)}{Fore.RESET}")
                sys.stdout.flush()


def print_banner():
    system("figlet AmirAli67 | lolcat")
    print(Fore.YELLOW + "----------------------" + Fore.RESET)


def main():
    print_banner()
    sleep_time = int(input("Please enter the mine time (in minutes): "))
    print("\n\n\n\n", 'mine time is >> ', Fore.CYAN, str(sleep_time), Fore.RESET, ' min', "\n")
    start(sleep_time)


# collect_data
collect_data = {'udid': str(uuid4().int), 'restore_key': restore_key}

subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "lolcat"])

main()
