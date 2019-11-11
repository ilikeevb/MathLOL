#!/usr/bin/env python
# coding: utf-8

import os
from mathlol import Vector, Matrix

def read_vector():
    os.system('clear')
    
    try:
        x = os.listdir("data/vector")
    except:
        print("Папка не найдена")
        return 0
    
    for i in range(len(x)):
        print(i+1, x[i])
        
    ReadFile = open("data/vector/" + x[int(input("Open: "))-1], 'r')
    string = ReadFile.read()

    vector = []

    string = string.split("!")
    for i in range(1, len(string)):
        vector.append(float(string[i]))
    
    os.system('clear')
    return vector

def input_vector():
    os.system("clear")    
    
    vector = []
        
    x = "EasterEgg"
    while (x!=""):
        try:
            os.system("clear")
            if(len(vector)>=1):
                x = input(str(vector)[:-1]+", ")
            else:
                x = input("[ ")
            if (x!=""): 
                vector.append(float(x))
        except ValueError:
            pass
    os.system("clear") 
    return vector

def save_vector(vector):
    try:
        with open("data/vector/"+ input("Name: ") +".txt", 'w') as f:
            for i in range(len(vector)):
                f.write("!"+str(vector[i]))
        print("Successfully Save")
    except:
        print("Не удалось сохранить файл")
        
def VectorReadInput():
    print("1. Read")
    print("2. Input")
    
    x = int(input())
    if(x == 1):
        return(read_vector())
    if(x == 2):
        return(input_vector())
    
def VectorAction():
    exit = False
    
    temp = Vector()
    temp.set(vector=VectorReadInput())
    
    while(exit == False):
        print("\n")
        print("1. Show Vector")
        print("2. Norm 1")
        print("3. Norm 2")
        print("4. Norm 3")
        print("5. Save")
        print("\n0. Exit")

        x = int(input())
        os.system('clear')
        if(x == 1):
            print("Vector: ", temp.get())
        elif(x == 2):
            print("Norm 1: ", temp.norm1())
        elif(x == 3):
            print("Norm 2: ", temp.norm2())
        elif(x == 4):
            print("Norm 3: ", temp.norm3())
        elif(x == 5):
            save_vector(temp.vector)
        elif(x == 0):
            exit = True
        else:
            print("No correct input")

def input_matrix():
    os.system("clear")    
    
    I = int(input("Число строк: "))
    J = int(input("Число столбцов: "))
    
    matrix = []
        
    for i in range(I):
        tempMatrix = []
        for j in range(J):
            os.system("clear")
            try:
                if (len(matrix) >= 1):
                    for i in matrix:
                        print(i)
                if (len(tempMatrix) >= 1):
                    x = float(input(str(tempMatrix)[:-1]+", "))
                else:
                    x = float(input("[ "))
                tempMatrix.append(x)
            except ValueError:
                pass
        matrix.append(tempMatrix)    
        
    os.system("clear")
    return matrix

def read_matrix():
    #читать матрицу из файла
    os.system('clear')
    
    try:    
        x = os.listdir("data/matrix")
    except:
        print("Папка data/matrix/ не найдена")
        return 0
    
    for i in range(len(x)):
        print(i+1, (x[i].split("."))[0])
    
    matrix = []
    
    ReadFile = open("data/matrix/" + x[int(input("Open: "))-1], 'r')
    string = ReadFile.read()
    string = string.split("?")

    for i in range(1, len(string)):
        temp = []
        str_temp = string[i].split("!")
        for j in range(1, len(str_temp)):
            temp.append(float(str_temp[j]))
        matrix.append(temp)
    
    os.system('clear')      
    return matrix
    
def save_matrix(matrix):
    #сохранить матрицу в файл
    try:
        with open("data/matrix/"+ input("Save. File name: ") +".txt", 'w') as f:
            for item in matrix:
                f.write("?")
                for i in item:
                    f.write("!"+str(i))
        print("Successfully Save")
    except:
        print("Не удалось сохранить файл")
def MatrixReadInput():
    print("1. Read")
    print("2. Input")
    
    x = int(input())
    if(x == 1):
        return(read_matrix())
    if(x == 2):
        return(input_matrix())
    
def MatrixAction():
    exit = False
    
    temp = Matrix()
    matrix = MatrixReadInput()
    temp.set(matrix)
    
    while(exit == False):
        print("\n")
        print("1. Show Matrix")
        print("2. Norm 1")
        print("3. Norm 2")
        print("4. Norm E")
        print("5. Norm I")
        print("6. LU")
        print("7. Determinant")
        print("8. Inverse")
        print("9. AX = B")
        print("121. Save")
        print("\n0. Exit")

        x = int(input())
        os.system('clear')
        if(x == 1):
            print("Matrix: ")
            for i in temp.matrix:
                print(i)
        elif(x == 2):
            print("Norm 1: ", temp.norm1())
        elif(x == 3):
            print("Norm 2: ")
            result = temp.norm2()
            for i in result:
                print(i)
        elif(x == 4):
            print("Norm E: ", temp.norm_E())
        elif(x == 5):
            print("Norm I: ", temp.norm_I())
        elif(x == 121):
            save_matrix(temp.matrix)
        elif(x == 6):
            result = temp.lu()
            print("L", "\t\t"*temp.J, "U")
            for i in range(len(result[0])):
                print(result[0][i], "\t\t", result[1][i])
        elif(x == 7):
            print("Determinant: ", temp.determinant())
        elif(x == 8):
            print("Inverse:")
            if(temp.inverse() != 0):
                for i in temp.inverse():
                    print(i)
        elif(x == 9):
            B = input_matrix()
            result = temp.ax_b(B = B)
            if(result != 0):
                for i in result:
                    print(i)
        elif(x == 0):
            exit = True
        else:
            print("No correct input")

os.system("clear")

print("MathLOL v1.0")
print("By Ilikeev Bilal and Gainullin Fidan")
print("\n")

x = ""
while(x != "0"):
    print("1. Vector")
    print("2. Matrix")
    print("\n0. Exit")
    
    x = input()

    if(x == "1"):
        os.system('clear')
        VectorAction()
    elif(x == "2"):
        os.system('clear')
        MatrixAction()
    elif(x == "0"):
        os.system('clear')
        print("May the Force be with you!")
    else:
        print("No correct input!")
input()
