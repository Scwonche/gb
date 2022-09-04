#54
from random import randint
def mass_print(mass):
    for row in mass:
        for elem in row:
            print(elem, end=' ')
        print()
n, m = map (int, input().split())
a = [[randint(1, 100) for j in range(m)] for i in range(n)]
print(mass_print(a))
a.sort(key=lambda x: int(x[n - 1]), reverse=True)
print(mass_print(a))
#56
#60
#58

