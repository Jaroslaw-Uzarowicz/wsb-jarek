def show():
    print('Hello', end='')
    print('Jeryk')


show()


def iloraz(a, b):
    return a//b #zwraca liczbę całkowitą "//"
    # return a/b

print(iloraz(2, 3))


'''
Użytkownik podaje z klawiatury marke, model, pojemnosc, predkosc maskymalna
Zdefiniuj funkcje, ktora pobierze dane od uzytkownika i przypisze do slownika


Utworz druga funkcje wyswietlajaca dane w formacie:
Marka i model:
Pojemnosc:
Predkosc maksymalna:
'''

car = {}

def erykCar():
    car['brand'] = input("Podaj markę: ")
    car['model'] = input("Podaj model: ")
    car['tank'] = input("Podaj pojemność: ")
    car['max_speed'] = input("Podaj maks. prędkość: ")

def jarekCar():
    print(f'Marka i model:{car["brand"]} {car["model"]}' )
    print(f'Pojemność: {car["tank"]}' )
    print(f'maks. prędkość:{car["max_speed"]} ' )

erykCar()
jarekCar()