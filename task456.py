#XOR шифрование,
def xor(stroka,key):
    s = ""
    for symbol in stroka:
        s += chr(ord(symbol) ^ key)
    return s
#print(xor('cdscewdcsf',3))
#print(xor('`gp`ftg`pe',3))

#Частота использования цифр в диапазоне чисел.
def usedigits(start,end):
    st = ''
    for s in range(start,end+1):
        st += str(s)
    print(f'Записываем значения в одну строку: {st}')
    for i in range (0,10):
        print(f"Число {i} встречается {st.count(str(i))} раз(a)")

#Частота использования символов в тексте.
#stroka = str(input('Введите строку: '))
def usealpha(stroka):
    stroka = str(stroka)
    print(f'Введенная строка: {stroka}')
    while len(stroka) != 0:
        print(f'Символ {stroka[0]} встречается {stroka.count(stroka[0])} раз(а)')
        stroka = stroka.replace(stroka[0],'')
        #print(stroka)
#usealpha(stroka)

while 1:
    print('Выберите задачу:')
    print('1. XOR шифрование.')
    print('2. Частота использования цифр в диапазоне чисел.')
    print('3. Частота использования символов в тексте.')
    print('4. Выход.')
    a = int(input())
    if a == 1:
        k,key = input("Введите зашифрованную или расшфрованную строку и ключ через пробел ").split()
        #key = input()
        if key.isdigit():
            key = int(key)
            print(f'Зашифрованное/расшифрованное слово: {xor(k,key)}')
        else:
            print('Введен неверный символ')
    elif a == 2:
        #Проверку на не числа убрал, потому что нельзя будет брать отрицательный диапазон
        x, y = input("Введите диапазон чисел через пробел(от х до у) ").split()
        #y = input()
        x = int(x)
        y = int(y)
        usedigits(x,y)
    elif a == 3:
            x = str(input("Введите строку "))
            usealpha(x)
    elif a == 4:
        print('Goodbye!')
        break
    else:
        print('Введен неверный символ')