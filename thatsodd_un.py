# Input sind mehrere Zahlen nacheinander. Alle geraden Zahlen sollen addiert werden.

lenlist = int(input())

count = 0
list = []
summe = 0

while count < lenlist:
    list.append(int(input()))
    count += 1

for i in list:
    if i % 2 == 0:
        summe += i

print(summe)
