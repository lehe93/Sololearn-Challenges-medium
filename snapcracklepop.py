# 6 Schüsseln mit Reis-Crispies. Je nach Menge, gibt es ein anderes Geräusch. 
# durch 3 dividierend (kein Rest) --> print("Pop")
# nicht durch 3 teilend und es ist ungerade --> print("Snap")
# nicht durch drei teilend und es ist gerade --> print("Crackle")
# Input sind 6 Integers, Output sind 6 Strings (je nach Schüsselinhalt)

b1 = int(input())
b2 = int(input())
b3 = int(input())
b4 = int(input())
b5 = int(input())
b6 = int(input())

list = [b1, b2, b3, b4, b5, b6]
list = [int(i) for i in list]
x = ""

for i in list:
    if i % 3 == 0:
        x += "Pop"
    elif(i %3 != 0 and i % 2 == 1):
        x += "Snap"
    elif(i % 3 != 0 and i % 2 == 0):
        x += "Crackle"

print(x)


   

