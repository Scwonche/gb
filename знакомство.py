#1 максимум и минимум
a, b = map(int,input().split())
print(f'максимум {max(a,b)} минимум {min(a,b)}')
#2
a, b, c = map(int,input().split())
print(f'максимум {max(a,b,c)} ')
#3
a = int(input())
if a % 2 == 0:
    print('четное')
else:
    print('нечетное')
#4
n = int(input())
for i in range(2,n + 1):
    if i % 2 == 0:
        print(i)