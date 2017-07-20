# message.py
# Fills in certain blanks based off an array (presumably names) into a given message template

array = ["Rutgers",
         "Cornell",
         "Bryn Mawr College",
         "Wellesley College",
         "Stanford",
         "NYU",
         "UW",
         "Stony Brook",
         "Northwestern",
         "University of Maryland, College Park",
         "University of Virginia",
         "Brown",
         "Arizona State",
         "Boston College",
         "Princeton",
         "College of William and Mary",
         "Tufts"]

file = open("lookingforitasareps.txt", 'w')

message = "Hey There! I'm Richard and this upcoming year's ITASA National Conference Liaison. I was going through the National Board Contact Sheet and couldn't seem to find UCSB's ITASA Representative's information.\nAs such, I was wondering if you could direct me to the UCSB representative. Thanks in advance!"

file.write(message)
