# newEpisode.py

# Automatically sends reminders via Mac OS X's Notification Center when a new episode for selected series comes out
# Current implementation is specific to masterani.me

import requests
import os

# Test to make sure requests is working properly
# request = requests.get('http://www.google.com')

# Fails, seems to be issues with kissanime.ru's link
# request = requests.get('http://kissanime.ru/Anime/Youjo-Senki/Episode-005?id=134058')

# Success
# request = requests.get('http://www.masterani.me')
request = requests.get('http://www.masterani.me/anime/watch/2386-youjo-senki/2')

if request.status_code < 400:
	print 'Website Exists'
	print request.status_code
else:
	print 'Website does not exist'
	print request.status_code
	
# Logic/Pseudo Code
# Given array with base URL, anime name, and episode # counter
# Check every day at X time (e.g. 6am) in case it released earlier than anticipated
# Check every hour on predicted release date (e.g. Thursdays)