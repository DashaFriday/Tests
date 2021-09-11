'''Нахождение наименьшего количества ходов, для приведения массива к одному числу. Операции +1 и -1'''

'''Чтение файла'''
asd1 = open(input(), 'r')

'''Объявление переменных'''
numsy = []
ml = asd1.readlines()
test = []
mini = 10000

'''Считывание значений из файла в массив'''
for i in range(len(ml)):
    a = int(ml[i])
    numsy.append(a)

'''Нахождение разницы между каждым и каждым элементом, наименьшая сумма - ответ'''
for i in range(len(numsy)):
    for j in range(len(numsy)):
        test.append(abs(numsy[i]-numsy[j]))
    if mini > sum(test):
        mini = sum(test)
    test = []

'''Вывод'''
print(mini)