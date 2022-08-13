from math import sqrt
#1 (строки)
n = int(input('введите 5 значное число'))
if n > 9999 and n < 1000000:
    s = str(n)
    if s == s[::-1]:
        print('да')
    else:
        print('нет')
else:
    print('Число не пятизначное')
#1 (числа)
n = int(input('введите 5 значное число'))
if n > 9999 and n < 1000000:
    if n % 100 == n // 10000 + n // 1000 % 10 * 10:
        print('да')
    else:
        print('нет')
else:
    print('Число не пятизначное')
#2
x1,y1,z1 = map(int,input("Введите координаты 1 точки").split())
x2,y2,z2 = map(int,input("Введите координаты 2 точки").split())
a = (x2-x1)**2
b = (y2-y1)**2
c = (z2-z1)**2
print('%.2f' % sqrt(a+b+c))
#3
n = int(input())
for i in range(n):
    print(i**3,end=" ")