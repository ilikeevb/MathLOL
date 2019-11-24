#!/usr/bin/env python
# coding: utf-8

import os
import math

class mathlol(object):
    def __init__(self):
        """
        Конструктор класса Матрица
        """
        
        self.matrix = None
        self.I = 0
        self.J = 0
    
    def get(self):
        """
        Возращает матрицу
        """
        
        return (self.matrix)
    
    def set(self, matrix):
        """
        Устанавливает матрицу
        """
        if (type(matrix[0]) != list):
            matrix = [matrix]
          
        self.matrix = matrix
        self.I = len(matrix)
        self.J = len(matrix[0])
    
    def shape(self, matrix = None):
        """
        Возвращает размер матрицы
        """
        if matrix == None:
            matrix = self.matrix
        return (len(matrix), len(matrix[0]))
    
    def size(self, matrix = None):
        """
        True - матрица квадратная NxN
        False - матрица не квадратная MxN
        """
        
        if matrix == None:
            matrix = self.matrix
        
        temp = len(matrix[0])
        for i in matrix:
            if (temp != len(i)):
                return False
        return True
    
    def copy(self, matrix = None):
        """
        Возвращает копию матрицы
        """
        if matrix == None:
            matrix = self.matrix
        
        result = []
        
        if self.checkvector(matrix = matrix):
            for i in matrix:
                result.append(i)
        else:
            i = len(matrix)
            j = len(matrix[0])

            for i_ in range(i):
                temp = []
                for j_ in range(j):
                    temp.append(matrix[i_][j_])
                result.append(temp)
        return result
    
    def compare(self, other):
        """
        Сравнивает матрицы
        Возвращает True, если матрицы идентичны
        """
        
        if (type(self) == type(other)):
            other = other.matrix
            
        if (len(self.matrix) == len(other)):
            if (self.size(matrix = self.matrix) == self.size(matrix = other)):
                shape = self.shape(matrix=self.matrix)
                for i in range(shape[0]):
                    for j in range(shape[1]):
                        if self.matrix[i][j] != other[i][j]:
                            return False
        return True
    
    def comparesize(self, other):
        """
        Сравнивает размеры матриц
        Возвращает True, если матрицы одинакового размера
        """
        
        if (type(self) == type(other)):
            other = other.matrix
            
        if (len(self.matrix) == len(other)):
            if (self.size(matrix = self.matrix) == self.size(matrix = other)):
                return True
        return False
    
    def checkvector(self, matrix = None):
        """
        Проверяет, является ли матрица вектором
        """
        if matrix == None:
            matrix = self.matrix
        
        if (type(matrix[0]) != list):
            return True
        else:
            if len(matrix[0]) == 1 or len(matrix) == 1:
                return True
        return False
    
    def zeroes(self, i = None, j = None):
        """
        Возвращает нулевую матрицу
        """
        if j == None:
            j = i

        result = []

        for i_ in range(i):
            temp = []
            for j_ in range(j):
                temp.append(0)
            result.append(temp)
        return result
    
    def eye(self, n = None):
        """
        Возвращает единичную матрицу
        """
        
        if(n == None):
            matrix = []
            for i in range(self.I):
                temp = []
                for j in range(self.J):
                    temp.append(0)
                temp[i] = 1
                matrix.append(temp)
            return(matrix)
        else:
            matrix = []
            for i in range(n):
                temp = []
                for j in range(n):
                    temp.append(0)
                temp[i] = 1
                matrix.append(temp)
            return(matrix)
    
    def yoda(self, matrix = None, n = 3):
        """
        Возвращает матрицу округлив все элементы
        """
        if matrix == None:
            matrix = self.matrix
        
        result = []
        
        if self.checkvector(matrix):
            for i in matrix:
                result.append(round(i, 3))
        else:
            for i in matrix:
                temp = []
                for j in i:
                    temp.append(round(j, 3))
                result.append(temp)
        
        return(result)
    
    def minor(self, i, j, matrix = None):
        """
        Возвращает минор матрицы
        """
        
        if matrix == None:
            matrix = self.matrix
            
        matrix_minor = []
        for row in (matrix[:i]+matrix[i+1:]):
            matrix_minor.append(row[:j] + row[j+1:]) 
        
        return matrix_minor
    
    def determinant(self, matrix = None, mul = 1):
        """
        Определитель матрицы
        """
        
        if matrix == None:
            matrix = self.matrix
        
        width = len(matrix)
        
        if width == 1:
            return mul * matrix[0][0]
        else:
            sign = -1
            sum = 0
            
            for i in range(width):
                m = []
                for j in range(1, width):
                    buff = []
                    for k in range(width):
                        if k != i:
                            buff.append(matrix[j][k])
                    m.append(buff)
                sign *= -1
                sum += mul * self.determinant(m, sign * matrix[0][i])
            
            return sum
    

    def transposition(self, matrix = None):
        """
        Транспонирование матрицы
        """
        
        if matrix == None:
            matrix = self.matrix
        
        transpos_matrix = []
        
        for j in range(self.J):
            temp = []
            for i in range(self.I):
                temp.append(self.matrix[i][j])
            transpos_matrix.append(temp)
        
        return transpos_matrix
    
    def add(self, matrix):
        """
        Сумма матриц
        """
        
        if (type(self) == type(matrix)):
            matrix = matrix.matrix
            
        if self.comparesize(matrix):
            sum_matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append((self.matrix[i][j] + matrix[i][j]))
                sum_matrix.append(temp)
            return sum_matrix
        else:
            print("Нельзя складывать матрицы разной длинны")
            return 0
    
    def __add__(self, other):
        """
        Перегрузка + (сумма матриц)
        """
        
        if (type(self) == type(other)):
            other = other.matrix
        return self.add(matrix = other)
    
    def sub(self, matrix):
        """
        Разность матриц
        """
        
        if (type(self) == type(matrix)):
            matrix = matrix.matrix
            
        if self.comparesize(matrix):
            sum_matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append((self.matrix[i][j] - matrix[i][j]))
                sum_matrix.append(temp)
            return sum_matrix
        else:
            print("Нельзя вычитать матрицы разной длинны")
            return 0
    
    def __sub__(self, other) :
        """
        Перегрузка - (разность матриц)
        """
        
        if (type(self) == type(other)):
            other = other.matrix
        return self.sub(matrix = other)
    
    def dot(self, matrix):
        """
        Произведение матриц
        """
        
        if type(matrix) == int or type(matrix) == float:
            return(self.dotAn(matrix=self.matrix, n = matrix))
        else:
            if (type(self) == type(matrix)):
                matrix = matrix.matrix
        
            mult = []

            try:
                for i in range(0,len(self.matrix)):
                    temp=[]
                    for j in range(0,len(matrix[0])):
                        s = 0
                        for k in range(0,len(self.matrix[0])):
                            s += self.matrix[i][k]*matrix[k][j]
                        temp.append(round(s, 2))
                    mult.append(temp)
                return mult
            except IndexError:
                print("Index Error")
    
    def __mul__(self, other):
        """
        Перегрузка * (произведение матриц)
        """
        
        if (type(self) == type(other)):
            other = other.matrix
        return self.dot(matrix = other)
    
    def dotAn(self, matrix, n):
        """
        Произведение матрицы на число
        """
        
        if type(n) == int or type(n) == float:
            mult = []
            for i in matrix:
                temp = []
                for j in i:
                    temp.append(round(j*n, 2))
                mult.append(temp)
            return mult
        
    def dotAB(self, A, B):
        """
        Произведение двух заданных матриц
        """
        
        if (type(self) == type(A)):
            A = A.matrix
        if (type(self) == type(B)):
            B = B.matrix
        
        if (type(A) == int or type(A) == float):
                return(self.dotAn(matrix = B, n = A))
        if (type(B) == int or type(B) == float):
                return(self.dotAn(matrix = A, n = B))
        else:
            mult = []

            try:
                for i in range(0,len(A)):
                    temp=[]
                    for j in range(0,len(B[0])):
                        s = 0
                        for k in range(0,len(A[0])):
                            s += A[i][k]*B[k][j]
                        temp.append(round(s, 2))
                    mult.append(temp)
                return mult
            except IndexError:
                print("Index Error")
                return 0
    
    def condition_number(self, matrix = None):
        """
        Возвращает число обусловленности
        """
        if matrix == None:
            matrix = self.matrix
        return self.norm_E(matrix=matrix) * self.norm_E(matrix=self.inverse(matrix=matrix))
    
    def union_matrix(self, matrix = None):
        """
        Союзная матрица
        """
        
        if matrix == None:
            matrix = self.matrix
        
        determ = self.determinant(matrix = matrix)
        
        transp_matrix = self.transposition(matrix = matrix)
        
        union = []
        
        for i in range(len(transp_matrix)):
            temp = []
            for j in range(len(transp_matrix[0])):
                minor_determ = (-1)**(i+1 + j+1) * self.determinant(matrix=self.minor(matrix = transp_matrix, i=i, j=j))
                temp.append(minor_determ)
            union.append(temp)
        
        return union
    
    def inverse(self, matrix = None):
        """
        Обратная матрица
        """
        
        if matrix == None:
            matrix = self.matrix
        
        determ = self.determinant(matrix = matrix)
        
        if (determ != 0):
            inverse_matrix = self.dotAn(matrix = self.union_matrix(matrix), n = (1/determ))
            return inverse_matrix
        else:
            print("Матрица вырожденная\nОбратная для неё не существует")
            return 0
    
    def norm1(self):
        """
        Первая норма матрицы
        """
        
        matrix = []
        
        for j in range(self.J):
            temp = 0
            for i in self.matrix:
                temp += abs(i[j])
            matrix.append(temp)
        
        return max(matrix)
    
    def norm1_vector(self):
        """
        Первая норма вектора
        """
        
        result = 0
        for i in self.matrix[0]:
            result += abs(i)
        
        return result
    
    def norm2(self):
        """
        Вторая норма матрицы
        """
        
        t_matrix = self.transposition()
        
        return self.dotAB(t_matrix, self.matrix)
    
    def norm2_vector(self):
        """
        Вторая норма вектора
        """
        
        result = 0
        for i in self.matrix[0]:
            result += abs(i**2)
        return math.sqrt(result)
    
    def norm3_vector(self):
        """
        Третья норма вектора
        """
        
        vector = []
        
        for i in self.matrix[0]:
            vector.append(abs(i))
        
        return max(vector)
    
    def norm_E(self, matrix = None):
        """
        Евклидова норма матрицы
        """
        if matrix == None:
            matrix = self.matrix
            
        temp = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp += abs(matrix[i][j])**2
        
        return math.sqrt(temp)
    
    def norm_I(self):
        """
        Бесконечная норма матрицы
        """
        
        matrix = []
        
        for i in range(self.I):
            temp = 0
            for j in range(self.J):
                temp += abs(self.matrix[i][j])
            matrix.append(temp)

        return max(matrix)
    
    def lu(self, matrix = None):
        """
        LU разложение
        """
        
        if matrix == None:
            matrix = self.matrix
        
        n = len(matrix)
        U = self.copy(matrix)
        L = self.zeroes(n)
        
        for i in range(n):
            for j in range(i, n):
                L[j][i]=U[j][i]/U[i][i];
        
        for k in range(1, n):
            for i in range(k-1, n):
                for j in range(i, n):
                    L[j][i]=U[j][i]/U[i][i]
            for i in range(k, n):
                for j in range(k-1, n):
                    U[i][j]=U[i][j]-L[i][k-1]*U[k-1][j]

        L = self.yoda(L)
        U = self.yoda(U)

        return L, U
    
    def cholesky_decomposition(self):
        """
        Разложение Холецкого
        """
        
        n = self.I
        
        lower = [[0 for x in range(n)]  
                    for y in range(n)]; 
        
        # Разложение матрицы
        try:
            for i in range(n):  
                for j in range(i + 1):  
                    sum1 = 0
                    
                    if (j == i):  
                        for k in range(j): 
                            sum1 += pow(lower[j][k], 2); 
                        lower[j][j] = round(math.sqrt(self.matrix[j][j] - sum1), 2) 
                    else:   
                        for k in range(j):
                            sum1 += (lower[i][k] *lower[j][k]) 
                        if(lower[j][j] > 0): 
                            lower[i][j] = round((self.matrix[i][j] - sum1) / lower[j][j], 2)
            return lower
        except ValueError:
            print("Ошибка в вычислениях. Корень из отрицательного числа не существует")
            return 0
    
    def ax_b(self, b, A = None):
        """
        Решение уровнения AX = B
        """
        if (len(b[0]) > 1):
            print("Неправильный вид вектора B \nВектор B должен быть матрица-столбец")
            return 0
        
        if (A == None):
            A = self.matrix

        if(len(A) != len(b)):
            print("Количество строк матриц A и B должны быть одинаковыми")
            return 0

        if (self.inverse(A) != None):
            X = self.dotAB(A = self.inverse(A), B = b)
            return X
        else:
            print("Матрица вырожденная\nОбратная для неё не существует")
            return 0
    
    def seidel(self, b, eps = 0.0001, A = None):
        """
        Метод Зейделя
        
        eps - точность (условие выхода)
        """
        if (len(b[0]) > 1):
            print("Неправильный вид вектора B \nВектор B должен быть матрица-столбец")
            return 0
        
        if (A == None):
            A = self.matrix
        
        n = len(A)
        x = [.0 for i in range(n)]
        
        try:
            converge = False
            while not converge:
                x_new = self.copy(x)

                for i in range(n):
                    s1 = sum(A[i][j] * x_new[j] for j in range(i))
                    s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                    x_new[i] = (b[i][0] - s1 - s2) / A[i][i]

                converge = math.sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
                x = x_new
            result = self.yoda(x)
            return result
        
        except OverflowError:
            print("Численный результат за пределами разрешенного диапазона")
            return 0
