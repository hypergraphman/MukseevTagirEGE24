# Задание 5
# (А. Игнатюк) Исполнитель «Аппо» получает на вход четырехзначное число N и строит новое число R по следующим правилам:
# 1) Если первая цифра числа N делится на 4, то заменяем её на цифру 9.
# 2) Если первая цифра числа N делится на 2 и не делится на 4, то заменяем её на цифру 3.
# Сколько существует чисел N, для которых соответствующее число R начинается с цифры 9, а восьмеричная запись числа R оканчивается цифрой 4?

def cng(n):
    n = str(n)
    if int(n[0]) % 4 == 0:
        n = '9' + n[1:]
    # elif int(n[0]) % 2 == 0:
    #     n = '3' + n[1:]

    if n[0] == '9' and int(n) % 8 == 4:
        return True
    else:
        return False


s = 0
for k in range(1000, 9999 + 1):
    if cng(k):
        s += 1

print(s)

