'''Путь по m, по круговому массиву n'''

'''Входные данные'''
n, m = map(int,input().split())
a = [1]

'''Пока переменная k не 1, считаем путь (остаток от деления)'''
k = -1
while k % n != 1:
    abs(k)
    '''Если остаток 0, прибавляем n'''
    if k % n == 0:
        a.append(k % n + n)
    else:
        a.append(k % n)
    '''Следующий шаг по массиву'''
    k = k + m - 1

'''Вывод'''
print(a)