#Einkauf im Dutyfree-Shop, aber jeder Artikel soll nicht mehr als 20 Dollar kosten. 
#Die Umrechnung sind 1.1 Dollar = 1 Euro. 
#22 Dollar = 20 Euro. 

list = input().split(" ")

list.sort()
x = 0

#Strings in der Liste in Integers umwandeln
#kürzere Variante wäre: list = [int(i) for i in list]
for i in range(0, len(list)):
    list[i] = float(list[i])

for i in list: 
    if i * 1.1 >= 20:
        x += 1
    elif i * 1.1 < 20:
        x += 0

if x == 0:
    print("On to the terminal")
elif x > 0:
    print("Back to the store")

