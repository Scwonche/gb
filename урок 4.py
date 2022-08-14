#1
import random

a,b = map(int,input().split())
x = 1
for i in range(1,b+1):
    x *= a
print(x)
#2
n = int(input())
s = 0
if n < 0:
    n = abs(n)
while n > 0:
    s += n % 10
    n //= 10
print(s)
#3
arr = []
for i in range(8):
    y = random.randint(100,500)
    arr.append(y)
print(*arr)