### Aufgabe: Schreibe Unit-Tests mit dem Modul unittest, um folgende Aspekte abzudecken:
# - Teste jede Methode (add, sub, mul, div) auf korrekte Ergebnisse.
# - Teste Grenzfälle (z. B. negative Zahlen, große Zahlen, float-Werte).
# - Teste, ob bei Division durch 0 korrekt eine ValueError-Exception ausgelöst wird.
# - Achte darauf, dass Testfunktionen sprechende Namen haben.
# - Verwende ein Setup, um vor jedem Test eine neue Rechner-Instanz anzulegen.




import unittest
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Rechner:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ValueError("Division durch Null ist nicht erlaubt")
        return a / b
