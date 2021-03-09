#Определить, является ли введенное число простым
def primenumder(n):
    if n % 2 == 0:
        print("Not prime",'\n')
        return      
    k = 3
    while k **2 <= n and n % k != 0:
        if n % k == 0:
            print("Not prime",'\n')
            return
        k+=2
    print("Prime",'\n')
#primenumder(int(input("Введите число, и я скажу простое оно или нет ")))

#Нахождение наибольшего общего делителя
#x = int(input("Введите 2 числа через enter, и я покажу их наибольший общий делитель "))
#y = int(input())
from math import gcd
def HOD(a,b):
    if a == b:
        return(a)
    elif a > b:
        return HOD(a-b,b)
    else:
        return HOD(a,b - a)
#print("HOD = ",HOD(x,y),'\n')

#Нахождение наименьшего общего кратоного
#x = int(input("Введите 2 числа через enter, и я покажу их наименьшее общее кратное "))
#y = int(input())
def HOK(a,b):
    return(a * b // HOD(a,b))
#print("HOK = ",HOK(8,12),'\n')

#Выравнивание f-string пример
def poem():
    poem = [['Я', 'узнал,', 'что у', 'меня'],
            ['Есть', 'огромная', 'семья', ''],
            ['И', 'Тропинка', 'и', 'лесок'],
            ['В', 'поле', 'каждый', 'колосок']]
    for words in poem:
        word1, word2, word3, word4 = words
        print(f'{word1:10} {word2:10} {word3:10} {word4:10}')

while 1:
    print('Выберите задачу:')
    print('1. Определить порстое число или нет.')
    print('2. Наибольший общий делитель.')
    print('3. Наименьшее общее кратное.')
    print('4. Выход.')
    print('5. Пример f-string выравнивания')
    a = int(input())
    if a == 1:
        k = input("Введите целое положительное число, и я скажу простое оно или нет ")
        if k.isdigit():
            k = int(k)
            primenumder(k)
        else:
            print('Введен неверный символ')
    elif a == 2:
        x, y = input("Введите 2 числа через пробел, и я покажу их наибольший общий делитель ").split()
        #y = input()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            print(f"HOD = {HOD(x,y)}")
        else:
            print('Введен неверный символ')
    elif a == 3:
        x, y = input("Введите 2 числа через пробел, и я покажу их наименьшее общее кратное ").split()
        #y = input()
        if x.isdigit() and y.isdigit():
            x = int(x)
            y = int(y)
            print(f"HOK = {HOK(x,y)}")
        else:
            print('Введен неверный символ')
    elif a == 4:
        print('Goodbye!')
        break
    elif a == 5:
        poem()
    else:
        print('Введен неверный символ')
        