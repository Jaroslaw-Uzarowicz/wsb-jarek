slownik = {'klucz1': 'wartość1', 'klucz2': 'wartość2'}
print(slownik)
print(slownik['klucz1'])

# utwórz słownik o nazwie worker zawierający klucze: imie , nazwsiko, miasto, wiek, imiona_dzieci i imiona_rodziców

worker = {'imie': 'Eryk', 'nazwsiko': 'Szymanski', 'miasto': 'Poznan',
          'wiek': '888888', 'imiona_dzieci': ['Er', 'Yk'], 'imiona_rodzicow': ['Szy', 'Manski']}
print(worker)
print(worker['imiona_rodzicow'])
print(worker['imiona_rodzicow'][0])


worker['wzrost'] = 197
print(worker)

for value in worker.values():
    print(value, end="")

key = 'imie'

if key in worker:
    del worker[key]
    print(f'Klucz {key} został usunięty!')
else:
    print(f'Klucz {key} nie został usunięty')

print(worker)

# dokończyć słowniki

