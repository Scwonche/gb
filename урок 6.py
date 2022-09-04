#41
def find_rev(mass):
    return sum(True for i in mass if i < 0)
input("введите числа")
a = map(int,input().split())
print(find_rev(a))

#43 пользовался методом крамера для матрицы размером 2
def delta_matrix(x1,y1,x2,y2):
    return x1*y2-x2*y1
k1, b1 = map(int,input('Введите коэфф. 1 прямой').split())
k2, b2 = map(int,input('Введите коэфф. 2 прямой').split())
delta = delta_matrix(-k1,1,-k2,1)
delta_x = delta_matrix(b1,1,b2,1)
delta_y = delta_matrix(-k1,b1,-k2,b2)
print(f'искомые координаты ({delta_x/delta},{delta_y/delta})')