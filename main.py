import json
import os
import random
import ctypes

SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 1
SPIF_SENDCHANGE = 2

# Load configuration
with open('data.json') as r_file:
    data = json.load(r_file)
    directory = data.get('folder', '')

    # If folder is empty then ask for what to assign as wallpaper folder
    if not directory:
        directory = input('Enter path to wallpaper folder, with \\\\ separating each folder except the last: ')
        data['folder'] = directory
        with open('data.json', 'w') as w_file:
            json.dump(data, w_file)

# Get all files from within wallpaper folder
wallpapers = os.listdir(directory)

def set_wallpaper(path):
    # Convert to absolute path
    abs_path = os.path.abspath(path)
    success = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, abs_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
    if not success:
        print(f"Failed to set wallpaper. Please check the path or try again. Path: {abs_path}")
    return success

# Main loop
while True:
    option = input('(1) List all wallpapers\n(2) Randomized wallpaper\n(3) Select a wallpaper\n(4) Current wallpaper\n(5) Quit\n')
    if option == '5':
        break

    if option == '1':
        for wallpaper in wallpapers:
            print("\t- " + wallpaper)
    elif option == '2':
        wallpaper = random.choice(wallpapers)
        while wallpaper == data.get('current'):
            wallpaper = random.choice(wallpapers)
        path = os.path.join(directory, wallpaper)
        print(path)
        if set_wallpaper(path):
            data['current'] = wallpaper
    elif option == '3':
        for index, wallpaper in enumerate(wallpapers, start=1):
            print(f'\t- ({index}) {wallpaper}')
        option = int(input("Select a wallpaper by typing its number: "))
        wallpaper = wallpapers[option - 1]
        path = os.path.join(directory, wallpaper)
        print(path)
        if set_wallpaper(path):
            data['current'] = wallpaper
    elif option == '4':
        print(f"Current wallpaper: {data.get('current', 'No wallpaper set')}")

# Save updated configuration
with open('data.json', 'w') as w_file:
    json.dump(data, w_file)
