#1
from random import randint

a = []

for i in range(16):
    p = randint(1, 100)
    a.append(p)
print(*a)
print(a.index(max(a))+1, a.index(min(a))+1)

#2
from random import randint

a = []

for i in range(16):
    p = randint(1, 100)
    a.append(p)
print(*a)
for i in range(15,0,-1):
    print(a[i],end=' ')
