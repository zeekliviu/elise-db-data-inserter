# Data inserter for Elise's project
# Date: 30.12.2022
# Author: Zeek Liviu & Zamfir Elise
from random import choice, randint

nume_romanesti = []
prenume_baieti = []
prenume_fete = []
id_angajati = []
nume_angajati = []
salarii_angajati = []
id_manageri = [0 for i in range(0, 105)]

with open('nume_romanesti.txt', 'r') as nr:
    nume_romanesti.extend(nr.readlines())
nume_romanesti = [i.replace('\n', '') for i in nume_romanesti]
with open('prenume_fete.txt', 'r') as nr:
    prenume_fete.extend(nr.readlines())
prenume_fete = [i.replace('\n', '') for i in prenume_fete]
with open('prenume_baieti.txt', 'r') as nr:
    prenume_baieti.extend(nr.readlines())
prenume_baieti = [i.replace('\n', '') for i in prenume_baieti]

for i in range(0, 20):
    doua_prenume = randint(0, 1)
    if doua_prenume:
        nume_angajati.append(f"{choice(nume_romanesti)} {choice([' '.join([choice(prenume_fete), choice(prenume_fete)]), ' '.join([choice(prenume_baieti), choice(prenume_baieti)])])}")
    else:
        nume_angajati.append(f"{choice(nume_romanesti)} {choice([choice(prenume_baieti), choice(prenume_fete)])}")
    id_angajati.append(i)
    salariul = randint(4000, 5000)
    salarii_angajati.append(salariul)

for i in range(20, 105):
    nume_angajati.append(f"{choice(nume_romanesti)} {choice([choice(prenume_baieti), choice(prenume_fete)])}")
    id_angajati.append(i)
    salariul = randint(2000, 3500)
    salarii_angajati.append(salariul)

for i in range(1, 20):
    while salarii_angajati[i] > salarii_angajati[0]:
        salarii_angajati[i] -= randint(100, 200)
id_manageri[0] = 'null'
begin = randint(1, 19)
end = randint(1, 19)
while begin > end:
    end = randint(1, 19)
for i in range(begin, end+1):
    id_manageri[i] = 0
for i in range(1, begin+1):
    id_manageri[i] = randint(begin, end)
for i in range(end+1, 20):
    id_manageri[i] = randint(begin, end)

for i in range(20, 105):
    id_manageri[i] = randint(1, 19)

with open('angajati.txt', 'w') as angajati:
    for i in range(0, 105):
        angajati.write('insert into angajati_patiserie (id_angajat, salariul, id_manager, nume)\nvalues ')
        angajati.write(f"({id_angajati[i]}, {salarii_angajati[i]}, {id_manageri[i]}, '{nume_angajati[i]}');\n")