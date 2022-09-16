a = []
b = []
n = int(input("введите количество эл-тов массива"))
for i in range(n):
    s = input(f'введите {i+1}-ый элемент массива')
    a.append(s)
for elem in a:
    if len(elem)<4:
        b.append(elem)
