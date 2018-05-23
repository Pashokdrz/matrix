import matrixModul
from matrixModul import Matrix
 
A = Matrix(4, 4)
B = Matrix(4, 4)
C = A + B
D = A - B
E = A * 4
F = A * B
print('Матрица А = ')
A.outputMatrix()
print('Матрица В = ')
B.outputMatrix()
print('C = A + B: ')
if C != 1:
    C.outputMatrix()
else:
    print('Матрицы разных размеров!')
print('D = A - B: ')
if D != 1:
    D.outputMatrix()
else:
    print('Матрицы разных размеров!')
print('E = A * 4: ')
E.outputMatrix()
print('F = A * B: ')
if F != 1:
    F.outputMatrix()
else:
    print('Матрицы разных размеров!')
print(determinant(A))
print('Матрица А транспонированная: ')
A.transporate()
A.outputMatrix()
