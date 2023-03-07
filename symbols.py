# input ist ein String mit Symbolen, Output sollen nur Buchstaben und Zahlen sein. 

string = input()

x = ""

for i in string:
	if i in  "1234567890 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
		x += i

print(x)
