# Data inserter for Elise's project
# Date: 30.12.2022
# Author: Zeek Liviu & Zamfir Elise
from random import choice, randint, sample, uniform
from bs4 import BeautifulSoup
from requests import get
from faker import Faker
from datetime import date
from anyascii import anyascii
import json
import pycountry

########### GENERARE ANGAJATI ###########

nume_romanesti = []
prenume_baieti = []
prenume_fete = []
id_angajati = []
nume_angajati = []
salarii_angajati = []
id_manageri = [0 for j in range(0, 105)]

with open('nume_romanesti.txt', 'r') as nr:
    nume_romanesti.extend(nr.readlines())
nume_romanesti = [j.replace('\n', '') for j in nume_romanesti]
with open('prenume_fete.txt', 'r') as nr:
    prenume_fete.extend(nr.readlines())
prenume_fete = [j.replace('\n', '') for j in prenume_fete]
with open('prenume_baieti.txt', 'r') as nr:
    prenume_baieti.extend(nr.readlines())
prenume_baieti = [j.replace('\n', '') for j in prenume_baieti]

for j in range(0, 20):
    doua_prenume = randint(0, 1)
    if doua_prenume:
        nume_angajati.append(f"{choice(nume_romanesti)} {choice([' '.join([choice(prenume_fete), choice(prenume_fete)]), ' '.join([choice(prenume_baieti), choice(prenume_baieti)])])}")
    else:
        nume_angajati.append(f"{choice(nume_romanesti)} {choice([choice(prenume_baieti), choice(prenume_fete)])}")
    id_angajati.append(j)
    salariul = randint(4000, 5000)
    salarii_angajati.append(salariul)

for j in range(20, 105):
    doua_prenume = randint(0, 1)
    if doua_prenume:
        nume_angajati.append(f"{choice(nume_romanesti)} {choice([' '.join([choice(prenume_fete), choice(prenume_fete)]), ' '.join([choice(prenume_baieti), choice(prenume_baieti)])])}")
    else:
        nume_angajati.append(f"{choice(nume_romanesti)} {choice([choice(prenume_baieti), choice(prenume_fete)])}")
    id_angajati.append(j)
    salariul = randint(2000, 3500)
    salarii_angajati.append(salariul)

for j in range(1, 20):
    while salarii_angajati[j] > salarii_angajati[0]:
        salarii_angajati[j] -= randint(100, 200)
id_manageri[0] = 'null'
begin = randint(1, 19)
end = randint(1, 19)
if begin > end:
    begin, end = end, begin
for j in range(begin, end+1):
    id_manageri[j] = 0
for j in range(1, begin+1):
    id_manageri[j] = randint(begin, end)
for j in range(end+1, 20):
    id_manageri[j] = randint(begin, end)

for j in range(20, 105):
    id_manageri[j] = randint(1, 19)

with open('angajati.txt', 'w') as angajati:
    for j in range(0, 105):
        angajati.write('insert into angajati_patiserie (id_angajat, salariul, id_manager, nume)\nvalues ')
        angajati.write(f"({id_angajati[j]}, {salarii_angajati[j]}, {id_manageri[j]}, '{nume_angajati[j]}');\n")

#######################################

########### GENERARE INGREDIENTE ###########

id_produse = [i for i in range(0, 404)]
producatori = []
preturi = []
nume = []

with open('ingrediente.txt', 'w', encoding='utf-8') as ingrediente:
    for i in range(1, 5):
        url = f'https://www.pravaliamofturi.ro/catalog/ingrediente-prajituri-72/p{i}?view_type=grid'
        page = get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        produse = soup.find('div', class_='products-grid__items')
        produse = produse.find_all('div', class_='product product--grid')

        # print(str(produse[7].find('div', class_='product__data').find('a', class_='product__name').text).replace('\t', '').split()[0]) - pentru producator
        # print(' '.join(str(produse[10].find('div', class_='product__data').find('a', class_='product__name').text).replace('\t', '').split()[1:])) - pentru nume
        # print(float(str(produse[0].find('div', class_='product__data').find('div', class_='product__info product__info--price-row').find('span', class_='product__info product__info--price-gross').text).replace('\t', '').replace('\n', '').replace('RON', '').replace(',', '.'))) - pentru pret
        for j in range(0, 100):
            producatori.append(str(produse[j].find('div', class_='product__data').find('a', class_='product__name').text).replace('\t', '').replace("'", "''").split()[0])
            nume.append(' '.join(str(produse[j].find('div', class_='product__data').find('a', class_='product__name').text).replace('\t', '').replace("'", "''").split()[1:]))
            preturi.append(float(str(produse[j].find('div', class_='product__data').find('div', class_='product__info product__info--price-row').find('span', class_='product__info product__info--price-gross').text).replace('\t', '').replace('\n', '').replace('RON', '').replace(',', '.').replace('\xa0/ pachet', '').replace('\xa0/ set', '')))
    url = f'https://www.pravaliamofturi.ro/catalog/ingrediente-prajituri-72/p5?view_type=grid'
    page = get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    produse = soup.find('div', class_='products-grid__items')
    produse = produse.find_all('div', class_='product product--grid')
    for j in range(0, 4):
        producatori.append(str(produse[j].find('div', class_='product__data').find('a', class_='product__name').text).replace('\t', '').replace("'", "''").split()[0])
        nume.append(' '.join(str(produse[j].find('div', class_='product__data').find('a', class_='product__name').text).replace('\t', '').replace("'", "''").split()[1:]))
        preturi.append(float(str(produse[j].find('div', class_='product__data').find('div', class_='product__info product__info--price-row').find('span', class_='product__info product__info--price-gross').text).replace('\t', '').replace('\n', '').replace('RON', '').replace(',', '.').replace('\xa0/ pachet', '').replace('\xa0/ set', '')))
    for j in range(0, 404):
        ingrediente.write('insert into ingrediente (id_ingredient, producator, nume, pret)\nvalues ')
        ingrediente.write(f"({id_produse[j]}, '{producatori[j]}', '{nume[j]}', {preturi[j]});\n")

#######################################

########### GENERARE LOCATII_PATISERII ###########

id_patiserie = [i for i in range(0, (end-begin+1))] # 5 - 11 = 7 -> range(0, 11-5+1) = range(0, 7) -> 0, 1, 2, 3, 4, 5, 6
nr_angajati = []
date_infiintare = []
id_manageri_locatii = []
for i in range(begin, end+1): # begin = 5, end = 11 -> range(5, 11+1) = range(5, 12) -> 5, 6, 7, 8, 9, 10, 11
    id_manageri_locatii.append(i)
    nr_angajati.append(id_manageri.count(i))
    date_infiintare.append(str(Faker().date_between(start_date=date(2015, 1, 1), end_date=date(year=2022, month=12, day=31))))
with open('locatii_patiserii.txt', 'w') as locatii_patiserii:
    for i in range(0, (end-begin+1)):
        locatii_patiserii.write('insert into locatii_patiserii (id_patiserie, nr_angajati, data_infiintare, id_manager)\nvalues ')
        locatii_patiserii.write(f"({id_patiserie[i]}, {nr_angajati[i]}, to_date('{date_infiintare[i]}', 'yyyy-mm-dd'), {id_manageri_locatii[i]});\n")
#######################################

########### GENERARE MENIURI ###########

id_meniuri = [i for i in range(0, (end-begin+1))]
nr_produse = sample(range(1, 11), (end-begin)+1)
with open('meniuri.txt', 'w') as meniuri:
    for i in range(0, (end-begin+1)):
        meniuri.write('insert into meniuri (id_meniu, id_patiserie, nr_produse)\nvalues ')
        meniuri.write(f"({id_meniuri[i]}, {id_patiserie[i]}, {nr_produse[i]});\n")

#######################################

########### GENERARE RANDURI_MENIU ###########

id_randuri_meniu = []
for _ in id_meniuri:
    id_randuri_meniu.append([i for i in range(0, nr_produse[id_meniuri.index(_)])])
id_produse_patiserie = []
nr_prod = 0
for _ in id_randuri_meniu:
    for __ in _:
        id_produse_patiserie.append(nr_prod)
        nr_prod += 1
dict_produse = {}
url = 'https://www.cofetariaarmonia.ro/prajituri/#'
page = get(url)
soup = BeautifulSoup(page.content, 'html.parser')
produse = soup.find('ul', class_='product_list grid row').find_all('li', class_='ajax_block_product')
for _ in produse:
    dict_produse.update({anyascii(str(_.find('a', class_='product-name').text).replace('\t', '').replace('\n', '')):
    float(str(_.find('span', class_='price product-price').text).replace('\t', '').replace('\n', '').replace(' lei', '').replace(',', '.'))})
soup = BeautifulSoup(open('pagina2.html', encoding='utf-8').read(), 'html.parser')
produse = soup.find('ul', class_='product_list grid row').find_all('li', class_='ajax_block_product')
for _ in produse:
    dict_produse.update({anyascii(str(_.find('a', class_='product-name').text).replace('\t', '').replace('\n', '')):
    float(str(_.find('span', class_='price product-price').text).replace('\t', '').replace('\n', '').replace(' lei', '').replace(',', '.'))})
url = 'https://www.lidl.ro/sortiment/brutaria'
page = get(url)
soup = BeautifulSoup(page.content, 'html.parser')
produse = soup.find('div', class_='nuc-m-flex-container__container').find_all('div', class_='nuc-a-flex-item nuc-a-flex-item--width-6 nuc-a-flex-item--width-4@sm')
for _ in produse:
    pret = round(uniform(1.5, 10), 2)
    dict_produse.update({anyascii(str(_.find('div', class_='ret-o-card__body').find('header').find('h3').text).replace('\t', '').replace('\n', '').rstrip()): pret})
nr_prod = 0
dict_produse_alese = {}
with open('randuri_meniu.txt', 'w') as rm:
    for _ in id_randuri_meniu:
        produse_alese_in_meniu = []
        for __ in _:
            rm.write('insert into randuri_meniu (id_meniu, denumire_produs, pret, id_produs)\nvalues ')
            produs = choice(list(dict_produse.keys()))
            while produs in produse_alese_in_meniu:
                produs = choice(list(dict_produse.keys()))
            produse_alese_in_meniu.append(produs)
            if produs not in dict_produse_alese.keys():
                nr_prod += 1
                dict_produse_alese.update({produs: nr_prod})
            rm.write(f"({id_meniuri[id_randuri_meniu.index(_)]}, '{produs}', {dict_produse[produs]}, {dict_produse_alese[produs]});\n")


#######################################

########### GENERARE PRODUSE PATISERIE ###########

with open('produse_patiserie.txt', 'w') as pp:
    for _ in dict_produse_alese.keys():
        pp.write('insert into produse_patiserie (denumire_produs, id_produs, pret, gramaj, calorii, tara_origine)\nvalues')
        pp.write(f"('{_}', {dict_produse_alese[_]}, {dict_produse[_]}, {randint(50, 1000)}, {randint(80, 2000)}, '{choice(list(pycountry.countries)).name}');\n")

#######################################

# concatenare toate fisierele de output intr-un singur denumit ScriptSQL.txt

d1 = d2 = d3 = d4 = d5 = d6 = ''

with open('angajati.txt', 'r') as f:
    d1 = f.read()
with open('ingrediente.txt', 'r') as f:
    d2 = f.read()
with open('locatii_patiserii.txt', 'r') as f:
    d3 = f.read()
with open('meniuri.txt', 'r') as f:
    d4 = f.read()
with open('randuri_meniu.txt', 'r') as f:
    d5 = f.read()
with open('produse_patiserie.txt', 'r') as f:
    d6 = f.read()

d1 = 'set define off;\n' + d1 + '\n' + d2 + '\n' + d3 + '\n' + d4 + '\n' + d5 +'\n' + d6 + '\nset define on;'
with open('ScriptSQL.txt', 'w') as script:
    script.write(d1)