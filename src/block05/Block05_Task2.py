## Hier soll eine Datei eingelesen und ihr Inhalt in der vorgegebenen Weise ausgegeben werden. Dabei sollen jeweils nur die ersten 5 Zeilen der Datei in der Ausgabe erscheinen. Danach soll eine Meldung ausgegeben werden, wie viele Zeilen ausgelassen wurden. Die Meldung soll so formuliert sein wie in der Beispielausgabe in der Tabelle angegeben.

## lines = number of lines that are to be printed
def filereader(filename, lines):
    i=0
    with open(filename, "r") as file:
        for line in file:
            if i < lines:
                print(line.strip())
                i=i+1
    print("Ausgelassene Zeilen aus der Datei: " + str(i-lines)±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±± +"\n")





filereader("04-03-datei1.txt", 5)
filereader("04-03-datei2.txt", 5)
filereader("04-03-datei3.txt", 5)