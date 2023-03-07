# Werden bei der Eingabe nur einzigartige Buchstaben oder auch gleiche verwendet?
# Input ist string mit Buchstaben, Output ist "Unique" oder "Deja Vu"

text = input()
y = 0

for i in text:
	if  text.count(i) > 1:
		y += 1

if y <= 0:
	print("Unique")
else:
	print("Deja Vu")

