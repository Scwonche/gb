# 68
def akk(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akk(m - 1, 1)
    else:
        return akk(m - 1, akk(m, n - 1))

print(akk(2, 2))
#64, 65
m, n = map(int, input().split())
print(*[i for i in range(m, n + 1)])
print(sum([i for i in range(m, n + 1)]))
