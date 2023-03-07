# Sale im Store: 30% auf alle Items, bis auf das teuerste.
# Sale-Tax ist 7%, ergo Sale * 1.07.
# Betraege unter einem Dollar werden gespendet (rounddown)
# Input ist ein String mit Zahlen (floats), Output ist ein Int (gerundet). 
import math
items = sorted([float(x) for x in input().split(",")])

items.sort()
gesamt = 0

for i in items[:-1]:
    gesamt += float(i)

print(math.floor(gesamt * 0.3 * 1.07))