# Nachricht muss decodiert werden. 
# Input ist ein String mit Zeichen, Output ist die decodierte Nachricht. 
# Code muss geflippt werden und nur mit Buchstaben dargestellt werden. 

msg = input()

x = ""

for i in msg[::-1]:
    if i in "1234567890!§$%&/()=?+-.:;*,":
        x += ""
    elif i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ":
        x += i

print(x)