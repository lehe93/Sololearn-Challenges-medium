# Bankraub, bei dem nach einem bestimmten Item gesucht werden soll. 
# Für jede Box brauche ich 5 Minuten. Wie lange brauche ich, um alle 
# Boxen zu durchsuchen, bis ich das korrekte Item gefunden habe.?

boxinput = input()
search = input()

boxlist = boxinput.split(',')
time = 5


for i in boxlist:
    if i == search: 
        print(time)
    else:
       time += 5
