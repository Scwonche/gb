#34
import random

a = []
k = 0
for i in range(100):
    a.append(random.randint(100,999))
    if a[i] % 2 == 0:
        k +=1
print(*a)
print(k)
#36
b = []
b_sum = 0
for i in range(100):
    b.append(random.randint(1,199))
    if i % 2 != 0:
        b_sum += b[i]
print(*b)
print(b_sum)
#38
c = []
for i in range(100):
    c.append(random.uniform(10,60))
print(*c)
print(max(a)-min(a))