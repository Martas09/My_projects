import random

def vyhodnot(pole):
    if "ooo" in pole:
        return "o"
    elif "xxx" in pole:
        return "x"
    elif "-" not in pole and "xxx" not in pole and "ooo" not in pole:
        return "!"
    else:
        return "-"

def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def user_input():
    global cislo_policka
    cislo_policka = int(input("Na jakou pozici chcete hrat? "))
    return cislo_policka

def result_input():
    return cislo_policka

def tah_hrace(pole):
    symbol = str("o")
    while True:
        #cislo_policka = int(input("Na jakou pozici chcete hrat? "))
        cislo_policka = user_input()
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
    hracova_pozice = result_input()
    vetsi = hracova_pozice + 1
    mensi = hracova_pozice - 1
    while True:
        try:
            if pole[vetsi] == "-":
                cislo_policka = vetsi
                return tah(pole, cislo_policka, symbol)
            elif pole[mensi] == "-" and 0 <= mensi < 19:
                cislo_policka = mensi
                return tah(pole, cislo_policka, symbol)
            elif pole[vetsi] != "-" and pole[mensi] != "-":
                cislo_policka = pole.index("-")
                return tah(pole, cislo_policka, symbol)
            elif mensi < 0:
                cislo_policka = pole.index("-")
                return tah(pole, cislo_policka, symbol)
            elif vetsi > 19:
                cislo_policka = pole.index("-")
                return tah(pole, cislo_policka, symbol)
        except IndexError:
                cislo_policka = pole.index("-")
                return tah(pole, cislo_policka, symbol)

def piskvorky1d():
    pole = str("--------------------")
    print("Aktualni stav pole je: ", pole)
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