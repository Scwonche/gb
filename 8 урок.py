#54
from random import randint
def mass_print(mass):
    for row in mass:
        for elem in row:
            print(elem, end=' ')
        print()

def sum_row(mass):
    x = mass[0][0]
    for row in mass:
        if sum(row)< x:
            x = sum(row)
    print(x)
n, m = map (int, input('введите размер массива').split())
a = [[randint(1, 100) for j in range(m)] for i in range(n)]
mass_print(a)
for row in a:
    row.sort(reverse=True)
mass_print(a)
#56
sum_row(a)
#60
k,l,m = map(int,input('введите размер 3-хмерного массива').split())
ar = [[[0 for i in range(k)] for j in range(l)] for k in range(m)]
for i in range(k):
    for j in range(l):
        for t in range(m):
            x = int(input())
            ar.append(x)
#с выводом его не удалось
#58
