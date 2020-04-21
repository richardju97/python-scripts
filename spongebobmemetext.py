
# spongebobmemetext.py
# takes in text input and changes the formatting to match that of the spongebob meme

str = raw_input("\nEnter original string:\n")
str = str.lower()

print("\n\n")
print("All Lower Case:\n")
print(str)

srr = ""

for i in range(0, len(str)):
	if (i % 2 != 0):
		srr += str[i].upper()
	else:
		srr += str[i]

print("\n\n")
print("Memeified String:\n")
print(srr)
print("\n\n")

