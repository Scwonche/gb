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
#3
from random import randint

a = []
s = 0
for i in range(16):
    p = randint(1, 100)
    a.append(p)
k = a.index(max(a))
p = a.index(min(a))
if k < p:
    print(sum(a[k:p]))
else:
    print(sum(a[p:k]))
print(*a)


#4
from random import randint

a = []
s = 0
for i in range(16):
    p = randint(1, 100)
    s += p
    a.append(p)

print(*a)
print(s/len(a))
