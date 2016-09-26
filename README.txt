Python Scripts

What is it?
-----------

This is a collection of various python scripts that I've written.
The goal of these scripts is to make performing various tasks more efficient 
(in comparison to doing them by hand/manually calculating them, etc.)

Files Included in this Folder
-----------------------------

1. costCalculator.py
2. goldenHour.py

All files are left within the same directory/repository and therefore one README file.
This is so that no matter what script is being run, you'll always cd into the same directory.


1. costCalculator.py
--------------------

Originally started to help my friend calculate how much he would need to purchase "X"
number of Boneless Wings from Buffalo Wild Wings on their 65 cent per wing deals. 

Expansion Plans:
	1. Modify so that it's more modular so that it calculates various different costs based on user input/selection

2. goldenHour.py
----------------

Originally started at the Hack the North 2016 hackathon (hosted by University of Waterloo). 
Intended for OS X only at the moment.

Utilizes the Yahoo Weather API to get the sunset times for a specific location.
Sends a reminder to OS X's Notification Center an hour before sunset to remind photographers to take a photo of the sunset. 

Parameters:
	"<city, state>"
	Example: "West Lafayette, IN"

Dependencies:
	terminal-notifier (OS X)

To install:
	$ sudo gem install terminal-notifier
	
Expansion Plans:
	1. Modify to run as a background task that repeats daily
	2. Calculate actual "golden hour" times instead of approximating at 30 minutes
	3. Assess the script's footprint and determine if there are ways to minimize it