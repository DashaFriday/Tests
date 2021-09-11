'''Чтение двух файлов, чтобы занести инфу в третий'''
import json

'''Объявление переменных, а-с для поиска удаляемых фрагментов, массивы для вычленения инф-ции'''
a = '"value": ""'
b = '"id": '
c = '""'
freport = []
forstring = []
testing = []
testing2 = []

'''Считывание первого файла'''
with open('tests.json') as asd1:
    for line in asd1:
        line2 = line.replace('\n', '')
        freport.append(line2)

'''Считывание второго файла, учёт индексов строк с нужной инф-цией'''
with open('values.json') as asd2:
    for index, line in enumerate(asd2):
        line2 = line.replace('    "value": "', '')
        line2 = line2.replace('"\n', '')
        testing.append(line2)
        if b in line:
            forstring.append(index+1)

'''Заполнение массива полезным содержанием по собраным индексам'''
for i in range(len(forstring)):
    testing2.append(testing[forstring[i]])

'''Склеивание текста для третьего файла'''
j = 0
for i in range(len(freport)):
    if c in freport[i]:
        d = freport[i].find(c)
        e = freport[i]
        freport[i] = e[:d+1] + testing2[j] + e[d+1:]
        j = j + 1

'''Занесение информации в третий файл json'''
with open('report.json', 'a', encoding='utf-8') as asd3:
    for i in range(len(freport)):
        json.dump(freport[i], asd3)
        asd3.write('\n')
