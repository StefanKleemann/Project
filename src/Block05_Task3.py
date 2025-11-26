liste_verben = ["sage", "bauen", "führen", "gehe", "laufen"]
# liste_verben = ["schlugen", "briet", "riefen", "ging", "tauchte", "hatten"]
# liste_verben = ["hinke", "schubste", "esse", "verkaufe", "spielen", "war"]

def singularorplural( liste ):
    i = 0
    for Wort in liste:
        i +=1
        tail = Wort[-2:]
        if type(Wort) != str:
            print("wrong parameter. Input must be of type string")
            return 1
        if len(Wort) < 3:
            print("parameter too short. undecideable. ")
            return 1
        # Stringbewertung
        output = f"{i}. {Wort} - "
        if tail == "en":
            print(output + "1. Person Plural")
        else:

            print(output + "1. Person Singular")



singularorplural(liste_verben)





