from math import *
from random import *
#31/01/23 #3
arvud=[]
kogus=int(input("Kogus:"))
for i in range(kogus):
    arvud.append(randint(-100,100))
print(arvud)
max_arv=max(arvud)
ind=arvud.index(max_arv)
print(ind)
print(max_arv)
max_arv=round(max_arv/kogus)
arvud.insert(ind,max_arv)
arvud.pop(ind+1)
print(arvud)




#31/01/23  #1
index=""
maakonnad=["Tln","Narva","K-Järve","Ida-Viirumaa","Tartu","Viljandi","Pärnumaa","Saaremaa"]
osa1=[]
osa2=[]
if len(maakonnad)%2==0 and len(maakonnad)>=2:
    n=int(len(maakonnad)/2)
    for i in range(1,n+1): #1,...n
        osa1.append(maakonnad[i-1])
    for j in range(n+1,len(maakonnad)+1): #n+1,... len()
        osa2.append(maakonnad[j-1])
    osa1.reverse()
    osa2.reverse()
    osa2.extend(osa1)
    print(osa2)
else:
    print("Viga")




#31/01/23 #2
def swap_elements(lst):
  n = int(input("Sisestage vahetatavate elementide arv: "))
  for i in range(n//2):
    lst[i], lst[-(i+1)] = lst[-(i+1)], lst[i]
  return lst

lst = [1, 2, 3, 4, 5]
print("Algne loend:", lst)
lst = swap_elements(lst)
print("Muudetud loend:", lst)

        


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

