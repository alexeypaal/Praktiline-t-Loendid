#1 Nimede lisamine loendisse
nimed = []

for i in range(5):    # Küsi kasutajalt viis nime
    name = input("Sisestage nimi: ")
    nimed.append(name)  # Salvesta need loendisse

nimed.sort()  # kuva tähestikulises järjekorras.

print("Nimed tähestikulises järjekorras:")
for name in nimed:
    print(name)

print("Viimati lisatud nimi:", nimed[-1])  #  Kuva eraldi viimati lisatud nimi.
print()





#2 Õpilased
opilased = ['Juhan','Kati','Maarja','Mario','Mati']

while True:
    print("Praegune opilaste nimede loend:", opilased)
    print("Valige valik:")
    print("1. Lisage opilase nimi")
    print("2. Kustutage opilase nimi")
    print("3. Uuendage opilase nimi")
    print("4. Välju")
    valik = input("Sisestage oma valik: ")

    if valik == '1':
        nimi = input("Sisestage opilase nimi, mida lisada: ")
        opilased.append(nimi)
    elif valik == '2':
        nimi = input("Sisestage opilase nimi, mida kustutada: ")
        opilased.remove(nimi)
    elif valik == '3':
        vananenud_nimi = input("Sisestage opilase nimi, mida uuendada: ")
        uus_nimi = input("Sisestage uus opilase nimi: ")
        indeks = opilased.index(vananenud_nimi)
        opilased[indeks] = uus_nimi
    elif valik == '4':
        break
    else:
        print("Vale valik. Palun proovige uuesti.")
        print()





#3 Duplikaadid
opilased = ['Juhan','Kati','Mario','Mario','Mati','Mati']

# Создание пустого списка для хранения уникальных имен
unikaalsed_õpilased = []

for student in opilased:
    if student not in unikaalsed_õpilased:
        unikaalsed_õpilased.append(student)

print("Unikaalsete õpilaste nimekiri:", unikaalsed_õpilased)
print()





#4 Vanused
van = [21, 45, 12, 67, 75, 18, 43, 19, 56, 32]
suurim = max(van)  ## Находим наибольший возраст

väikseim = min(van)  # Находим наименьший возраст

kokku = sum(van) # Нахождение суммы всех возрастов


keskmine = kokku / len(van) # Нахождение среднего возраста

print("Suurim vanus:", suurim)
print("Väikseim vanus:", väikseim)
print("Igas vanuses kokku:", kokku )
print("Keskmine vanus:", keskmine)
print()

