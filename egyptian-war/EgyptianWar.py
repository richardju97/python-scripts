# EgyptianWar.py

class Player:
    def __init__(self, name):
        self.name = name

print("Starting Egyptian War Bot:")
numPlayers = int(input("Enter Total Number of Players: "))

players = []
for i in range(0, numPlayers):
    myPlayer = Player(input("Enter Name for Player " + str(i+1)))
    players.append(0) #temporary - probably use a queue

# need to log order of all unique cards first

# need to change later
index = 0
while (true):
    temp = input(players[index].getName() + ": ")
