#!/usr/bin/env python
# coding: utf-8

import os
import copy
import math

class Matrix(object):
    def __init__(self):
        """
        Constructor
        Конструктор класса Матрица
        """
        
        self.matrix = None
        self.I = 0
        self.J = 0
    
    def __mul__(self, other):
        """
        Matrix multiplication
        перегрузка * (произведение матриц)
        """
        
        if (type(self) == type(other)):
            other = other.matrix
        return self.dot(matrix = other)
    
    def __add__(self, other):
        """
        Addition of matrices
        перегрузка + (сумма матриц)
        """
        
        if (type(self) == type(other)):
            other = other.matrix
        return self.add(matrix = other)
    
    def __sub__(self, other) :
        """
        Subtraction of matrices
        перегрузка - (разность матриц)
        """
        
        if (type(self) == type(other)):
            other = other.matrix
        return self.sub(matrix = other)
    
    def compare(self, other):
        """
        Compares the size of the matrices 
        Returns True if the matrices are the same size
        
        Сравнивает размеры матриц
        Возвращает True, если матрицы одинакового размера
        """
        
        if (type(self) == type(other)):
            other = other.matrix
            
        if (len(self.matrix) == len(other)):
            if (self.size(matrix = self.matrix) == self.size(matrix = other)):
                return True
        return False
    
    def size(self, matrix = None):
        """
        Return True - matrix square NxN
        Return False - matrix is not square MxN
        
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
    
    def get(self):
        """
        Return matrix
        Возращает матрицу
        """
        
        return (self.matrix)
    
    def set(self, matrix):
        """
        Set matrix
        Устанавливает матрицу
        """
        
        self.matrix = matrix
        self.I = len(matrix)
        self.J = len(matrix[0])
    
    def zeroes(self, i = None, j = None):
        if j == None:
            j = i

        A = []

        for i_ in range(i):
            temp = []
            for j_ in range(j):
                temp.append(0)
            A.append(temp)
        return A
    
    def checkvector(self, matrix = None):
        if matrix == None:
            matrix = self.matrix
        
        i = len(matrix)
        
        if (type(matrix[0]) == float):
            return True
        else:
            j = len(matrix[0])
            if(j == 1 and i > 1):
                return True
        
        return False

    def yoda(self, matrix = None, n = 3):
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
    
    def transposition(self, matrix = None):
        """
        The transpose of the matrix
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
    
    def minor(self, i, j, matrix = None):
        """
        Minor of the matrix
        Минор матрицы
        """
        
        if matrix == None:
            matrix = self.matrix
            
        matrix_minor = []
        for row in (matrix[:i]+matrix[i+1:]):
            matrix_minor.append(row[:j] + row[j+1:]) 
        
        return matrix_minor
    
    def add(self, matrix):
        """
        Addition of matrices
        Сумма матриц
        """
        
        if (type(self) == type(matrix)):
            matrix = matrix.matrix
            
        if self.compare(matrix):
            sum_matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append((self.matrix[i][j] + matrix[i][j]))
                sum_matrix.append(temp)
            return sum_matrix
        else:
            # You can not add matrices of different lengths
            print("Нельзя складывать матрицы разной длинны")
            return 0
    
    def sub(self, matrix):
        """
        Subtraction of matrices
        Разность матриц
        """
        
        if (type(self) == type(matrix)):
            matrix = matrix.matrix
            
        if self.compare(matrix):
            sum_matrix = []
            for i in range(len(self.matrix)):
                temp = []
                for j in range(len(self.matrix[i])):
                    temp.append((self.matrix[i][j] - matrix[i][j]))
                sum_matrix.append(temp)
            return sum_matrix
        else:
            # You cannot subtract matrices of different lengths
            print("Нельзя вычитать матрицы разной длинны")
            return 0
    
    def dot(self, matrix):
        """
        Matrix multiplication
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
    
    def dotAn(self, matrix, n):
        """
        Matrix by the number multiplication
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
        Multiplication two given matrices
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
    
    def determinant(self, matrix = None, mul = 1):
        """
        Matrix determinant
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
        
    def eye(self, n = None):
        """
        Create a unit matrix
        Создать единичную матрицу
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
    
    def norm1(self):
        """
        The first norm of the matrix
        Первая норма матрицы
        """
        
        matrix = []
        
        for j in range(self.J):
            temp = 0
            for i in self.matrix:
                temp += abs(i[j])
            matrix.append(temp)
        
        print(matrix)
        return max(matrix)
    
    def norm2(self):
        """
        The second norm of the matrix
        Вторая норма матрицы
        """
        
        t_matrix = self.transposition()
        
        return self.dotAB(t_matrix, self.matrix)
    
    def norm_E(self):
        """
        Euclidean norm of the matrix
        Евклидова норма матрицы
        """
        
        temp = 0
        
        for i in range(self.I):
            for j in range(self.J):
                temp += abs(self.matrix[i][j])**2
        
        print("sqrt("+str(temp)+")")
        return math.sqrt(temp)
    
    def norm_I(self):
        """
        Infinite norm of matrix
        Бесконечная норма матрицы
        """
        
        matrix = []
        
        for i in range(self.I):
            temp = 0
            for j in range(self.J):
                temp += abs(self.matrix[i][j])
            matrix.append(temp)
        
        print(matrix)
        return max(matrix)
    
    def copy(self, matrix = None):
        if matrix == None:
            matrix = self.matrix
        
        i = len(matrix)
        j = len(matrix[0])
        
        result = []
        for i_ in range(i):
            temp = []
            for j_ in range(j):
                temp.append(matrix[i_][j_])
            result.append(temp)
        return result
    
    def lu(self, matrix = None):
        if matrix == None:
            matrix = self.matrix
        
        print("1")
        for i in self.matrix:
            print(i)
        
        n = len(matrix)
        U = self.copy(matrix)
        L = self.zeroes(n)

        print("2")
        for i in self.matrix:
            print(i)
        
        for i in range(n):
            for j in range(i, n):
                L[j][i]=U[j][i]/U[i][i];
        
        print("3")
        for i in self.matrix:
            print(i)
        
        for k in range(1, n):
            for i in range(k-1, n):
                for j in range(i, n):
                    L[j][i]=U[j][i]/U[i][i]
            for i in range(k, n):
                for j in range(k-1, n):
                    U[i][j]=U[i][j]-L[i][k-1]*U[k-1][j]
        print("4")
        for i in self.matrix:
            print(i)
        # yoda = round(x, 3) 
        L = self.yoda(L)
        U = self.yoda(U)

        return L, U
    
    def cholesky_decomposition(self):
        """
        Cholesky Decomposition
        Разложение Холецкого
        """
        
        n = self.I
        
        lower = [[0 for x in range(n)]  
                    for y in range(n)]; 
        
        # Decomposition of matrix
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
    
    def union_matrix(self, matrix = None):
        """
        Union matrix
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
        Inverse matrix
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
    
    def ax_b(self, b, A = None):
        """
        The solution to the equation AX = B
        Решение уровнения AX = B
        """
        
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
        Seidel method
        Метод Зейделя
        
        eps - точность (условие выхода)
        """
        
        if (A == None):
            A = self.matrix
        
        n = len(A)
        x = [.0 for i in range(n)]
        
        try:
            converge = False
            while not converge:
                x_new = copy.copy(x)

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


class Vector(object):
    def __init__(self, vector=[]):
        """
        Constructor
        Конструктор класса Вектор
        """
        
        self.vector = vector
    
    def __mul__(self, other):
        """
        Vector multiplication
        перегрузка * (произведение векторов)
        """
        
        if (type(self) == type(other)):
            other = other.vector
        return self.dot(vector = other)
    
    def __add__(self, other):
        """
        Addition of vectors
        перегрузка + (сумма векторов)
        """
        
        if (type(self) == type(other)):
            other = other.vector
        return self.add(vector = other)
    
    def __sub__(self, other):
        """
        Subtraction of vectors
        перегрузка - (разность векторов)
        """
        
        if (type(self) == type(other)):
            other = other.vector
        return self.sub(vector = other)
    
    def compare(self, other):
        """
        Compares the size of the vectors 
        Returns True if the vectors are the same size
        
        Сравнение векторов
        Возвращает True, если вектора одинакового размера
        """
        
        if (type(self) == type(other)):
            other = other.vector
            
        if (len(self.vector) == len(other)):
            return True
        else:
            return False
    
    def get(self):
        """
        Return vector
        Возвращает вектор
        """
        
        return self.vector
    
    def set(self, vector = []):
        """
        Set vector
        Устонавливает вектор
        """
        
        self.vector = vector
    
    def add(self, vector):
        """
        Addition of vectors
        Сумма векторов
        """
        
        if (type(self) == type(vector)):
            vector = vector.vector
        if self.compare(vector):
            temp = []
            for i in range(len(vector)):
                temp.append(self.vector[i] + vector[i])
            return temp
        else:
            print("Размеры векторов не равны")
            return 0
    
    def sub(self, vector):
        """
        Subtraction of vectors
        Разность векторов
        """
        
        if (type(self) == type(vector)):
            vector = vector.vector
        
        if self.compare(vector):
            temp = []
            for i in range(len(vector)):
                temp.append(self.vector[i] - vector[i])
            return temp
        else:
            print("Размеры векторов не равны")
            return 0
    
    def dot(self, vector):
        """
        Vector multiplication
        Произведение векторов
        """
        
        if type(vector) == int or type(vector) == float:
            temp = []
            for i in range(len(self.vector)):
                temp.append(round(self.vector[i] * vector, 2))
            return temp
        else:
            if (type(self) == type(vector)):
                vector = vector.vector
            if self.compare(vector):
                temp = []
                for i in range(len(vector)):
                    temp.append(round(self.vector[i] * vector[i], 2))
                return temp
            else:
                print("Размеры векторов не равны")
                return 0
        
    def norm1(self):
        """
        The first norm of the vector
        Первая норма вектора
        """
        
        result = 0
        for i in self.vector:
            result += abs(i)
        
        return result
    
    def norm2(self):
        """
        The second norm of the vector
        Вторая норма вектора
        """
        
        result = 0
        for i in self.vector:
            result += abs(i**2)
        print("sqrt("+str(result)+")")
        
        return math.sqrt(result)
    
    def norm3(self):
        """
        The third norm of a vector
        Третья норма вектора
        """
        
        vector = []
        
        for i in self.vector:
            vector.append(abs(i))
        
        return max(vector)
