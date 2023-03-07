# Input ist ein englischer Satz. Nun muss von jedem Wort der erste Buchstabe ans Wortende gepackt werden.
# Außerdem soll an jedes so neu entstandene Wort noch ein -ay hingepackt werden: road = oadray

piglatin = input()

x = piglatin.split()
y = 0

for i in x:
    x[y] = i[1:] + i[0] + "ay"
    y += 1


print(" ".join(x))