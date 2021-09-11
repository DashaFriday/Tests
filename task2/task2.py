'''Вывод кода нахождения точки относительно окружности, инпут из файла'''

'''Чтение файлов'''
asd1 = open(input(), 'r')
asd2 = open(input(), 'r')

'''Считывание данных из первого файла'''
xc, yc = map(float, asd1.readline().split())
r = float(asd1.readline())

xt = 0
yt = 0

'''Считывание данных из второго файла в массив'''
ml = asd2.readlines()

'''Проход для каждой точки циклом'''
for i in range(len(ml)):
    xt, yt = map(float, ml[i].split())

    '''Вычисление местоположения точки'''
    if (xt - xc) * (xt - xc) + (yt - yc) * (yt - yc) == r * r:
        print(0)
    elif (xt - xc) * (xt - xc) + (yt - yc) * (yt - yc) < r * r:
        print(1)
    else:
        print(2)
