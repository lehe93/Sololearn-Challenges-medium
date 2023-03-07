# Kindergarten mit 15 Kindern, Bauklötze sollen fair aufgeteilt werden. 
# 4 Int-Inputs, für blaue, rote, grüne und gelbe Klötze.
# Diese müssen fair auf die Kinder verteilt werden. 
# Output ist der zusammengezählte Rest aller Leftover-Klötze. 

blue = int(input())
red = int(input())
green = int(input())
yellow = int(input())

print(int(blue % 15 + red % 15 + green % 15 + yellow % 15))