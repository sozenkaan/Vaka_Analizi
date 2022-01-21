import numpy as np
def preProcess(mat, aux):
    for i in range(0, n, 1):
        aux[0][i] = mat[0][i]

    for i in range(1, m, 1):
        for j in range(0, n, 1):
            aux[i][j] = mat[i][j] + aux[i - 1][j]

    for i in range(0, m, 1):
        for j in range(1, n, 1):
            aux[i][j] += aux[i][j - 1]

def sumQuery(aux, r1, c1, r2, c2):
    res = aux[r2][c2]
    if (r1 > 0):
        res = res - aux[r1 - 1][c2]
    if (c1 > 0):
        res = res - aux[r2][c1 - 1]
    if (r1 > 0 and c1 > 0):
        res = res + aux[r1 - 1][c1 - 1]

    return res

if __name__ == '__main__':
    print("Matrislerin satir sayisini giriniz (m)=")
    m = int(input())
    print("Matrislerin sutun sayisini giriniz (n)=")
    n = int(input())
    mat = np.array([[0 for i in range(n)] for i in range(m)])
    print("Input matrisini giriniz:")
    for i in range(m):
        for j in range(n):
            print('A[{}][{}]'.format(i, j))
            mat[i][j] = int(input())

print(mat)

aux = [[0 for i in range(n)]
       for j in range(m)]

preProcess(mat, aux)
for i in range(3):
    r1 = int(input())
    c1 = int(input())
    r2 = int(input())
    c2 = int(input())
    if i==0:
        print(f"Offer1:point 1({r1,c1}),point 2({r2,c2})")
        print("Output:")
        print("Offer1:", sumQuery(aux, r1, c1, r2, c2))
    elif i==1:
        print(f"Offer2:point 1({r1, c1}),point 2({r2, c2})")
        print("Output:")
        print("Offer2:", sumQuery(aux, r1, c1, r2, c2))
    elif i==2:
        print(f"Offer3:point 1({r1, c1}),point 2({r2, c2})")
        print("Output:")
        print("Offer3:", sumQuery(aux, r1, c1, r2, c2))


"""
Time Complexity:O(n^2)
The runtime will be n^2 since 
m rows and n columns will be traversed with the whole for loop of the matrix.

Space Complexity:O(1)
From the entered matrix, a sum matrix (aux) is formed by hovering over all 
the elements up to the i, j of the matrix. 
Since the total value of the elements between the entered 
r1,c1 and r2,c2 is taken from this matrix, the area complexity is O(1).
"""