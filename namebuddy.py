group = input()
name = input()
N = name[0]
x = 0

for i in group:
    if i == N:
        print("Compare notes")
        break
    else:
        x += 1 

if x == len(group):
    print("No such luck")