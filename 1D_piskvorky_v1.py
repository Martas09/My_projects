import random

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole and "xxx" not in pole and "ooo" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def tah_hrace(pole):
    symbol = str("o")
    while True:
        cislo_policka = int(input("Na jakou pozici chcete hrat? "))
        try:
            if pole[cislo_policka] == "-" and 0 <= cislo_policka <= 19:
                return tah(pole, cislo_policka, symbol)
            elif pole[cislo_policka] == "x" or pole[cislo_policka] == "o":
                print("Pozor! Pole je jiz obsazene. Zvolte prosim jine. ")
            elif cislo_policka < 0:
                print("Pozor! Pole neexistuje. Zvolte prosim jine. ")
        except IndexError:
            print("Pozor! Pole neexistuje. Zvolte prosim jine. ")

def tah_pocitace(pole):
    symbol = str("x")
    while True:
        cislo_policka = random.randint(0, 19)
        if pole[cislo_policka] == "-":
            return tah(pole, cislo_policka, symbol)

def piskvorky1d():
    puvodni_pole = str("--------------------")
    print("Aktualni stav pole je: ", puvodni_pole)
    pole = str("--------------------")
    while True:
        if vyhodnot(pole) == "x":
            print("Konec hry! Vyhral pocitac!")
            break
        elif vyhodnot(pole) == "o":
            print("Konec hry! Vyhral clovek!")
            break
        elif vyhodnot(pole) == "!":
            print("Konec hry! Remiza!")
            break
        else:
            pole = tah_hrace(pole)
            print("Po vasem tahu je aktualni stav pole: ", pole)
            pole = tah_pocitace(pole)
            print("Po tahu pocitace je aktualni stav pole: ", pole)

piskvorky1d()
