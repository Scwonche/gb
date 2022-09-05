from random import randint

def mass_print(mass):
    for row in mass:
        for elem in row:
            print(elem, end=' ')
        print()
def mass_pow(ar1,ar2):

    if len(ar1) == len(ar2[0]):
        ar3 = [[0 for j in range(len(ar2[0]))] for i in range(len(ar1))]
        for i in range(len(ar1)):
            s = 0
            for k in range(len(ar1[0])):

                for j in range(len(ar2[0])):
                    s += ar1[i][k]*ar2[k][j]
                    ar3[i][j] = s
    return ar3
a = [[randint(1, 100) for j in range(1)] for i in range(3)]
b = [[randint(1, 100) for j in range(3)] for i in range(1)]
mass_print(a)
print()
mass_print(b)
print()
mass_print(mass_pow(a,b))