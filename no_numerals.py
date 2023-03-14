#Es wird ein Satz als Input eingegeben. Nun sollen alle Zahlen (0 - 10) als englisches Wort (z.B: 1 == one) ausgegeben werden. 

sentence = input()

s10 = sentence.replace("10", "ten")
s1 = s10.replace("1", "one")
s2 = s1.replace("2", "two")
s3 = s2.replace("3", "three")
s4 = s3.replace("4", "four")
s5 = s4.replace("5", "five")
s6 = s5.replace("6", "six")
s7 = s6.replace("7", "seven")
s8 = s7.replace("8", "eight")
s9 = s8.replace("9", "nine")
s0 = s9.replace("0", "zero")

print(s0)