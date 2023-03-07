# Fuer Karottenkuchen brauche ich 7 Karotten.
# Erster Input sagt, wie viele Karotten in Boxen (zweiter Input) gepackt werden. 
# Rest-Karotten gehoeren mir + ggf. weitere kaufen, wenn < 7. 
# "Cake Time" oder "I need to buy X more"

total = int(input())
box = int(input())

x = int(total % box)

if x >= 7:
	print("Cake Time")
elif x < 7: 
	print("I need to buy " + str(7-x) + " more")
