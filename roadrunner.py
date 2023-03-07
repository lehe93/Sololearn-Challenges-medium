# Koyote jagt Läufer mit Vorsprung. 
# Erster Input ist Distanz zum Safespot, zweiter ist Läufer und dritter ist Koyote. 
# Läufer gewinnt: Meep Meep // Koyote gewinnt: Yum

distanz = int(input())
runner = int(input())
koyote = int(input())

dist_koy = distanz + 50
time_k = dist_koy / koyote
time_r = distanz / runner

if time_k < time_r:
    print("Yum")
elif time_k > time_r:
    print("Meep Meep")
