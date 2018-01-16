# websitestatus.py
# python script that periodically pings a website url to check if it's still live
# notifications are sent in the event that the specified site is down

import subprocess

s = subprocess.check_output(['ping', '-o', 'data.itasa.org'])
print(s)
