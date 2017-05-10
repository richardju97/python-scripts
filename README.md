## Python Scripts

# What is it?

This is a collection of various python scripts that I've written.
The goal of these scripts is to make performing various tasks more efficient 
(in comparison to doing them by hand/manually calculating them, etc.)

# Files Included in this Repository

1. costCalculator.py
2. goldenHour.py
3. cvp.py
4. ri.py
5. booleanAlgebra.py
6. testJapanese.py
7. randomVariable.py

All files are left within the same directory/repository and therefore one README file.
This is so that no matter what script is being run, you'll always cd into the same directory.


1. costCalculator.py

Originally started to help my friend calculate how much he would need to purchase "X"
number of Boneless Wings from Buffalo Wild Wings on their 65 cent per wing deals. 

Expansion Plans:
	1. Modify so that it's more modular so that it calculates various different costs based on user input/selection

2. goldenHour.py

Originally started at the Hack the North 2016 hackathon (hosted by University of Waterloo). 
Intended for OS X only at the moment.

Utilizes the Yahoo Weather API to get the sunset times for a specific location.
Sends a reminder to OS X's Notification Center an hour before sunset to remind photographers to take a photo of the sunset. 

Updated 11/23 to utilize the Twilio REST API to send an additional SMS reminder to a user passed in Phone Number. 

Parameters:
	"<city, state>"
	Example: "West Lafayette, IN"

	"<Phone Number with Area Code and +1 extension>"
	Example: "+18002221222"

Dependencies:
	terminal-notifier (OS X)
	Twilio Rest API Client

To install terminal-notifier (OS X):
```bash
$ sudo gem install terminal-notifier
```
Expansion Plans:
	1. Modify to run as a background task that repeats daily
	2. Calculate actual "golden hour" times instead of approximating at 30 minutes
	3. Assess the script's footprint and determine if there are ways to minimize it
	Alternative: Adjust to be deployed as a Chrome Extension

3. cvp.py

Calculates the nnumber of units needed to achieve a certain target net income (either before or after taxes) using the CVP formula from Managerial Accounting.

Prompts users to select 1 or 3 options: Break Even (net income = 0), Target Net Income Before Taxes, and Target Net Income After Taxes. 

Then prompts users to input the following variables where applicable:
	Unit Selling Price
  	Unit Variable Cost
	Total Fixed Cost
	Target Net Income Before/After Taxes
	Income Tax Rate

4. ri.py

5. booleanAlgebra.py

Currently only has some basic data for printing truth tables.

6. testJapanese.py

Basic Python Script related to the Japanese language. 
Intended as practice/concept testing and understanding how the Japanese language interacts with Python via Unicode encodings before pursuing a larger project in this topic.

Currently can convert from dictionary form to masu form.

7. randomVariable.py

Object Oriented Python Script that allows for calculating operations on Random Variables
Currently supports primarily discrete random variables (Bernoulli, Binomial, Geometric, Negative Binomial, and Poisson)
Supported functions for each random variable include: Probability Mass Function, Expected Value, Variance, and Summations.
Support for Continous Random Variables will be added in the near future. 

References combination.py for calculating combinations (primarily used for Binomial and Negative Binomial Random Variables). 
