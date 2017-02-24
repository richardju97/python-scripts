import urllib2, urllib, json, sys
import os, time
import datetime
from threading import Timer

#Twilio integration for sending SMS
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
# Make sure to remove these before pushing to GitHub
account_sid = "AC93bc79a222d23f5e7e09308591e8bec2"
auth_token = "ceef4b2d00ddca1ddc4b73ede5bc4539"
client = TwilioRestClient(account_sid, auth_token)

loc = str(sys.argv[1])
phoneNo = str(sys.argv[2])

def checkWeather():
	baseurl = "https://query.yahooapis.com/v1/public/yql?"
	yql_query = "select astronomy.sunset from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + loc + "')"
	yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
	result = urllib2.urlopen(yql_url).read()
	data = json.loads(result)
	return data['query']['results']['channel']['astronomy']['sunset']

def sendReminder():
	t = '-title {!r}'.format("Golden Hour Reminder")
	m = '-message {!r}'.format("Reminder that sunset is at " + str(sunset) + " today.")
	os.system('terminal-notifier {}'.format(' '.join([m, t])))

def sendSMS():
	msg = "Reminder that sunset is at " + str(sunset) + " today."

	message = client.messages.create(to=phoneNo, from_="+14083421269", body=msg)

sunset = checkWeather()
currDate = str(time.localtime()[0]) + ' ' + str(time.localtime()[1]) + ' ' + str(time.localtime()[2])

sunset_time = datetime.datetime.strptime(str(currDate) + ' ' + str(sunset), '%Y	 %m %d %I:%M %p')
goldenhr = sunset_time - datetime.timedelta(minutes=30)
reminder = goldenhr - datetime.timedelta(minutes=30)

now = datetime.datetime.today()
delta = (reminder-now).seconds+1

#would normally be delta, but for the purpose of demoing will be left at intervals of 10 seconds
timer = Timer(10, sendReminder)
timer.start()

timer = Timer(10, sendSMS)
timer.start()