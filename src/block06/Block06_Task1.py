# 1. strings: Entschlüssele die geheime Nachricht indem du jeden dritten character des Strings ausgibst!
# Vorsicht, die Nachricht beginnt erst beim dritten Zeichen.

# 2. lists: Multipliziere alle Elemente dieser Liste, die eine Zahl sind, miteinander! Gebe anschließend ihr Produkt aus!
# Denke dran, dass nicht alle Zahlen in Python vom Typ Integer sein müssen!

# 3. range: Bitte gebt alle Primzahlen zwischen 10 und 30 aus!


warmup_string = "drdaxusz seh saiwssnttr  lengsoj cagh e vsnuciihdya jfjefuttdk!"
warmup_list = ["e",6,["b","c"],22,True,0.5,"45",{"apfel":3},3,[12]]


i=-1
outstring = ""
while i < len(warmup_string):
    outstring = outstring +  warmup_string[i]
    i+=3
print (outstring)

###############################################################################
total = 0
for item in warmup_list:
    if type(item) == int:
        total = total + int( item )
    if type(item) == float:
        total = total + float(item)

print(f"Die Summe ist {total} " )


###############################################################################

# - definiere feste Zahl test < 31
# - divident  = 1
# - dividiere test durch divident
# - wenn type(Ergebnis) = int
#   -     erhöhe divident += 1

# -     gehe zu 2.
# -


###############################################################################

hint_list = []
hint_list.append("Schaut nochmal in die Folien!".split() )


print(hint_list.reverse())
