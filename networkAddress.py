# networkAddress.py

# Some basic converters related to networks

import sys

# 32bit Binary String -> IPv4 Address
str = sys.argv[1]
#print(str[1])
#idx = 0
ipaddr = ""
for i in range(0, len(str), 4):
	ipaddr += str[i:i+4]
	ipaddr += "."
print (ipaddr[:len(str)+1])

# IPv4 Address -> 32bit Binary String

# 48bit Binary String -> Ethernet/Hardware/MAC Address

# Ethernet/Hardware/MAC Address -> 48bit Binary String
