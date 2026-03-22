import math
import os
from os import *


def display_title():
    print("""  _____                   ____      _      
 | ____|__ _ ___ _   _   / ___|__ _| | ___ 
 |  _| / _` / __| | | | | |   / _` | |/ __|
 | |__| (_| \__ \ |_| | | |__| (_| | | (__ 
 |_____\__,_|___/\__, |  \____\__,_|_|\___|
                 |___/                     
 By @tishor123 (TG)\n""")





class Calc:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return math.sqrt(a)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    calc = Calc()
    clear_terminal()
    display_title()
    print("Scegli il tipo di operazioni!")
    print("1 addizione")
    print("2 sottrazione")
    print("3 moltiplicazione")
    print("4 divisione")
    print("5 potenza")
    print("6 radice quadrata")
    print("7 esci")

    scelta = int(input("Scrivi qui la tua scelta!: "))

    if scelta == 1:
        clear_terminal()
        display_title()
        a = int(input("Scrivi il primo numero!: "))
        b = int(input("Scrivi il secondo numero!: "))
        risultato = calc.add(a, b)
        clear_terminal()

    elif scelta == 2:
        a = int(input("Scrivi il primo numero!: "))
        b = int(input("Scrivi il secondo numero!: "))
        risultato = calc.subtract(a, b)

    elif scelta == 3:
        a = int(input("Scrivi il primo numero!: "))
        b = int(input("Scrivi il secondo numero!: "))
        risultato = calc.multiply(a, b)

    elif scelta == 4:
        a = int(input("Scrivi il primo numero!: "))
        b = int(input("Scrivi il secondo numero!: "))
        risultato = calc.divide(a, b)

    elif scelta == 5:
        a = int(input("Scrivi il primo numero!: "))
        b = int(input("Scrivi il secondo numero!: "))
        risultato = calc.power(a, b)

    elif scelta == 6:
        a = int(input("Scrivi il numero!: "))
        risultato = calc.sqrt(a)

    elif scelta == 7:
        print("uscita in corso...")
        return
    
    else:
        print("Scelta non valida!")
        return

    print("Il risultato è:", risultato)
    input("\nPremi invio per continuare...")

main()