# MathLOL
**MathLOL** - python модуль для работы с матрицами и векторами без использования NumPy

[Примеры использования модуля (Exampes)](https://github.com/ilikeevb/MathLOL/blob/master/example.ipynb)

```python
from mathlol import mathlol

matrix = mathlol()
matrix.set([[5, -2, -10], [0, -6, -2], [6, 9, 2]])

print("Матрица: ", matrix.get())

# Matrix determinant
print("Определитель матрицы: ", matrix.determinant())
# Transposed matrix
print("Транспонированная матрица: ", matrix.transposition())
# Inverse matrix
print("Обратная матрица", matrix.inverse())

# Multiply matrices
B = [[0, -1, 2], [-2, 1, 2], [2, -1, 0]]
print("Произведение матриц: ", matrix * B)

# LU разложение  (LU decomposition)
L, U = matrix.lu()
print("L: ", L)
print("U: ", L)
```
