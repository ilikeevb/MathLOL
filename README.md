# MathLOL
**MathLOL** - python модуль для работы с матрицами и векторами без использования NumPy
[Примеры использования модуля](https://github.com/ilikeevb/MathLOL/blob/master/example.ipynb)
```python
from mathlol import Matrix, Vector

matrix = Matrix()
matrix.set([[5, -2, -10], [0, -6, -2], [6, 9, 2]])

print("Матрица: ", matrix.get())

print("Определитель матрицы: ", matrix.determinant())
print("Транспонированная матрица: ", matrix.transposition())
print("Обратная матрица", matrix.inverse())

B = [[0, -1, 2], [-2, 1, 2], [2, -1, 0]]
print("Произведение матриц: ", matrix * B)

# LU разложение
L, U = matrix.lu()
print("L: ", L)
print("U: ", L)
```
