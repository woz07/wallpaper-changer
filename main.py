# Remove later
# Remove later
# Remove later
# Remove later
# TODO
#  For some reason I can't get it to change the background, everything else seems okay and functioning but the background just won't change

import json
import os
import random
import ctypes

# Get directory where wallpaper images are being stored
directory = None
data = []
with open('data.json') as r_file:
	data = json.load(r_file)
	directory = data['folder']
	# If folder is empty then ask for what to assign as wallpaper folder
	if directory is None or directory == "":
		directory = input('Enter path to wallpaper folder, with \\\\ seperating each folder except the last: ')
		data['folder'] = directory
		# Write out data back to json
		with open('data.json', 'w') as w_file:
			json.dump(data, w_file)

# Get all files from within wallpaper folder
wallpapers = os.listdir(directory)
# Let user decide if they want randomized wallpaper or a selected one or list them
while True:
	option = input('(1) List all wallpapers\n(2) Randomized wallpaper\n(3) Select a wall paper\n(4) Current wallpaper\n(5) Quit\n')
	if option == '5':
		# Break out of while loop
		break

	if option == '1':
		# Display all wallpapers within wallpaper folder
		for wallpaper in wallpapers:
			print("\t- " + wallpaper)
	elif option == '2':
		# Get a randomized wallpaper and if it's current wallpaper then reloop
		randomed = False
		wallpaper = None
		while randomed == False:
			wallpaper = random.choice(wallpapers)
			if wallpaper != data['current']:
				randomed = True
		# Set wallpaper
		path = os.path.join(directory, wallpaper)
		print(os.path.join(directory, wallpaper))
		style = 0
		SPI_ = 20
		image = ctypes.c_wchar_p(path)
		ctypes.windll.user32.SystemParametersInfoW(SPI_, 0, image, 3)
		# Update json
		data['current'] = wallpaper
		with open('data.json', 'w') as w_file:
			json.dump(data, w_file)
	elif option == '3':
		# Put wallpapers into dictionary<int,str>
		dictionary = {index + 1: value for index, value in enumerate(wallpapers)}
		# Print dictionary so like: index and it's values
		for index, value in dictionary.items():
			print(f'\t- ({index}) {value}')
		# Get what user wants to change wallpaper to
		option = int(input("Select either one of those by just typing in their number: "))
		# Set wallpaper
		wallpaper = dictionary[option]
		path = os.path.join(directory, wallpaper)
		print(os.path.join(directory, wallpaper))
		style = 0
		SPI_ = 20
		image = ctypes.c_wchar_p(path)
		ctypes.windll.user32.SystemParametersInfoW(SPI_, 0, image, style)
		# Update json
		data['current'] = wallpapers[option-1]
		with open('data.json', 'w') as w_file:
			json.dump(data, w_file)
	elif option == '4':
		# Print out value of 'current' from data.json
		print(data['current'])

# Write json back to file
with open('data.json', 'w') as w_file:
	json.dump(data, w_file)
