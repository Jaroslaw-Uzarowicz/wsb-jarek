# listy
progr = ['PHP', 'Python']
print(progr)
progr.append('C#')
print(progr)
count = progr.count('Python')
print(f'Python występuje {count} razy')


# tuple
str = ('Janusz', 'Anna')
int = (1, 2, 3)

print(int)

test = (1)
print(type(test))

test1 = (1,)
print(type(test1))

first = int[0]
print(first)

# int.append(4) -> nie można modyfikować tupli
# print(int)

# wyszukiwanie

if 2 in int:
    print('W tuplu int istnieje 2')
else:
    print('W tuplu int nie istieje 2')


# słowniki

person = {
    'name': 'Anna',
    'surname': 'Nowak'
}
print(person)

print(type(person))
print(person['name'])
print(person.keys())
print(person.get('height', 'brak danych'))
print(person.get('name', 'brak danych'))

person['height'] = 180
print(person.get('height', 'brak danych'))

'''
 Utwórz słownik i przypisz mu trzy imiona podane z klawiatury.
 Klucze w słowniku to liczby całkowite : 0,1,2
 Wyświel te dane na ekranie w formacie:
    Imię1 : ...
    Imię2 : ... 
    Imię3 : ...  
'''
names = {}

for n in range(3):
    name = input(f'Podaj {n} Imię:')
    names[n] = name

for key, value in names.items():
    print(f'Imię{key+1}: {value}')
