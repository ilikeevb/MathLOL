#!/usr/bin/env python
# coding: utf-8

import os
from sys import platform
from mathlol import mathlol

def naruto():
    naruto = ["══════════════█▒════════▒█▒══════════════════",
    "═════════════▒███▒═══▒██▒▒█════█████═════════",
    "═════════════█▒▒▒█▒═██▒▒▒▒█▒████▒▒█▒═════════",
    "════════════▒█▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒▒█══════════",
    "══════███══▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████▒═══",
    "══════██▒█▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒═══",
    "══════██▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█═════",
    "══════▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████▒═",
    "══██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███",
    "══███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒═",
    "════██▒▒▒▒▒▒▒▒▒▒████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██═══",
    "═════▒█▒▒▒▒██████████████▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒██▒",
    "═════▒█▒▒█████████████████▒▒██▒█████▒▒▒▒▒▒███",
    "═════█▒▒██████████████████▒▒██▒██████▒▒▒▒█▒══",
    "═════█▒▒███████████████████▒█████████████════",
    "════▒██████████▒▒████▒▒████▒█████████████════",
    "════███████████▒█████▒▒██████████████████════",
    "════▒▒▒██████████████▒▒▒██████████████▒▒█════",
    "════════███████▒█████▒▒███████████▒▒▒██▒█▒═══",
    "════════▒████████████████████▒▒▒▒▒▒▒▒█▒▒██═══",
    "══════════███████████▒██▒▒▒▒▒▒▒▒▒▒████▒▒███══",
    "══════════▒█▒▒██▒▒▒▒▒█▒▒▒█████▒▒▒▒▒██▒▒▒███▒═",
    "═══════════█▒▒▒███▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒█▒▒███▒",
    "═══════════██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒██▒▒▒████",
    "════════════██▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒███═███",
    "═██════███══██▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒█▒▒███▒═██",
    "▒███══▒█▒█▒══██▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒██████▒═█",
    "▒█▒█▒═▒█▒█▒═══██▒▒██▒▒▒████▒▒▒▒▒▒████████████",
    "═█▒▒█══█▒▒█════██▒████████▒▒▒▒▒██████████████",
    "═▒█▒▒█═█▒▒█══════█████▒██▒▒▒█████████████████",
    "══▒█▒▒▒█▒▒█▒═══════▒█████████████████████████",
    "══▒█▒▒▒█▒▒▒█══════════▒▒▒═▒██████████████████",
    "═█▒▒█▒▒▒▒▒▒▒█══════════════▒█████████████████",
    "▒█▒▒█▒▒▒▒██▒██════════════███████████████████",
    "▒█▒▒█▒▒▒▒▒▒▒▒█▒══════════████████████████████",
    "▒█▒██▒████▒▒▒▒█═════════█████████████████████",
    "▒█▒████▒█▒▒▒▒▒█════════██████████████████████",
    "═█▒▒█▒▒▒█▒▒▒▒▒█═══════▒██████████████████████",
    "═▒█▒▒▒▒▒▒█▒▒████═════████████████████████████",
    "═███▒▒▒▒▒▒▒██████════████████████████████████",
    "═█████▒▒█████████════████████████████████████",
    "▒█████████████████▒══████████████████████████",
    "▒██████████████████▒═▒███████████████████████",
    "═████████████████████████████████████████████",
    "═══██████████████████████████████████████████"]
    for i in naruto:
        print(i)

def input_matrix():
    os.system(comand)    
    
    I = int(input("Число строк: "))
    J = int(input("Число столбцов: "))
    
    matrix = []
        
    for i in range(I):
        tempMatrix = []
        for j in range(J):
            os.system(comand)
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
        
    os.system(comand)
    return matrix

def read_matrix():
    #читать матрицу из файла
    os.system(comand)
    
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
    
    os.system(comand)   
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
    print("Когда мы писали этот код,")
    print("только мы и Бог понимали как работает программа.")
    print("Теперь только Бог знает как он работает...")
    print("")
    
    print("1. Открыть файл")
    print("2. Ввести матрицу")
    
    x = int(input())
    if(x == 1):
        return(read_matrix())
    if(x == 2):
        return(input_matrix())

def matrix_menu(temp):
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
    print("10. Zeidel")
    print("11. Cholevsky")
    print("12. Число обусловленности")
    print("\n")
    print("121. Save")
    print("\n0. Exit")

    x = int(input())
    os.system(comand)
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
        print("L", " \t "*temp.J, "U")
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
        b = input_matrix()
        result = temp.ax_b(b = b)
        if(result != 0):
            for i in result:
                print(i)
    elif(x == 10):
        b = input_matrix()
        result = temp.seidel(b = b)
        if(result != 0):
            for i in result:
                print(i)
    elif(x == 11):
        result = temp.cholesky_decomposition()
        print(result)
    elif(x == 12):
        result = temp.condition_number()
        print(result)
    elif(x == 0):
        return True
    else:
        print("No correct input")
    return False

def vector_menu(temp):
    print("\n")
    print("1. Show Vector")
    print("2. Norm 1")
    print("3. Norm 2")
    print("4. Norm 3")
    
    print("121. Save")
    print("\n0. Exit")

    x = int(input())
    os.system(comand)
    if(x == 1):
        print("Matrix: ")
        for i in temp.matrix:
            print(i)
    elif(x == 2):
        print("Norm 1: ", temp.norm1_vector())
    elif(x == 3):
        print("Norm 2: ", temp.norm2_vector())   
    elif(x == 4):
        print("Norm 3: ", temp.norm3_vector())
    elif(x == 121):
        save_matrix(temp.matrix)
    elif(x == 0):
        return True
    else:
        print("No correct input")
    return False
def MatrixAction():
    exit = False
    
    temp = mathlol()
    matrix = MatrixReadInput()
    temp.set(matrix)
    
    while(exit == False):
        if temp.checkvector():
            exit = vector_menu(temp)
        else:
            exit = matrix_menu(temp)


if platform == "linux" or platform == "linux2":
	comand = "clear"
else: comand = "cls"

os.system(comand)

print("MathLOL v1.0")
print("By Ilikeev Bilal and Gainullin Fidan")
print("\n")

naruto()

x = ""
while(x != "0"):
    print("Нажмите любую кнопку чтобы продолжить")
    print("\n0. Выйти")
    
    x = input()

    if(x == "0"):
        os.system(comand)
        print("May the Force be with you!")
    else:
        os.system(comand)
        MatrixAction()
input()
