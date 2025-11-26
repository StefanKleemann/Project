## Wir erhalten eine Liste mit Elementen, die in eine Datei geschrieben werden sollen. Dazu soll jedes Element der Liste jeweils mit der zusätzlichen Information, an welchem Index wir uns gerade befinden, versehen werden. (Siehe Beispielausgabe in der Tabelle.)

## In dieser Aufgabe brauchen wir keinen zusätzlichen print()-Aufruf. Es sollen nur Inhalte in die Datei geschrieben werden; es soll also keine normale Ausgabe der Inhalte geben.
## Tipp: Um sowohl Strings als auch Zahlen in die jeweils aktuelle Zeile zu schreiben, können Zahlen mit str() explizit in einen String umgewandelt werden. Dann können alle Teile der Ausgabe mit einem + aneinandergefügt werden.

def enumerate_all_elements(outfile, list_items):
    with open(outfile,'w+') as liste:
        i =1
        for item in list_items:
            print(f"Eintrag {i}: {item}", file=liste)
            i=i+1

list_tiere = ["Pinguin", "Nashorn", "Chamäleon", "Pinguin"]
enumerate_all_elements("tiere.txt", list_tiere)

list_snacks = ["Schokolade", "Chips", "Bonbons", "Kuchen", "Käsebrot"]
enumerate_all_elements("snacks.txt", list_snacks)

list_farben = ["blau", "gelb", "rot", "lila"]
enumerate_all_elements("farben.txt", list_farben)
