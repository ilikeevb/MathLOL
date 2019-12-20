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
    
    try:
        I = int(input("Число строк: "))
    except:
        print("Некорректный ввод")
        print("Число строк = 3")
        I = 3
    try:
        J = int(input("Число столбцов: "))
    except: 
        print("Некорректный ввод")
        print("Число столбцов = 3")
        J = 3
        
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
        x = os.listdir("data/")
    except:
        print("Папка data/ не найдена")
        return 0
    
    for i in range(len(x)):
        print(i+1, (x[i].split("."))[0])
    
    matrix = []
    
    try:
        ReadFile = open("data/" + x[int(input("Имя файла: "))-1], 'r')
    except:
        print("Некорректный ввод!")
        return read_matrix()
    
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
        filename = ("data/"+ input("Сохранение. Имя файла: ") +".txt")
        with open(filename, 'w') as f:
            for item in matrix:
                f.write("?")
                for i in item:
                    f.write("!"+str(i))
        print("Файл " + filename.split(".")[0] + " сохранён")
    except:
        print("Не удалось сохранить файл")

def MatrixReadInput():
    print("Когда мы писали этот код,")
    print("только мы и Бог понимали как работает программа.")
    print("Теперь только Бог знает как он работает...")
    print("")
    
    print("1. Открыть файл")
    print("2. Ввести матрицу")
    
    x = " "
    while(x != "1" or x != "2"):
        x = input()
        if(x == "1"):
            return(read_matrix())
        if(x == "2"):
            return(input_matrix())

def matrix_menu(temp):
    print("\n")
    print("1. Вывести матрицу")
    print("2. 1 норма")
    print("3. 2 норма")
    print("4. Евклидова норма")
    print("5. Бесконечная норма")
    print("6. LU разложение")
    print("7. Определитель")
    print("8. Обратная матрица")
    print("9. AX = B")
    print("10. Метод Зейделя")
    print("11. Метод Холецкого")
    print("12. Число обусловленности")
    print("\n")
    print("121. Сохранить матрицу")
    print("\n0. Выйти")

    x = input()
    os.system(comand)
    if(x == "1"):
        print("Матрица: ")
        for i in temp.matrix:
            print(i)
    elif(x == "2"):
        print("1 норма: ", temp.norm1())
    elif(x == "3"):
        print("2 норма: ")
        result = temp.norm2()
        for i in result:
            print(i)
    elif(x == "4"):
        print("Евклидова норма: ", temp.norm_E())
    elif(x == "5"):
        print("Бесконечная норма: ", temp.norm_I())
    elif(x == "121"):
        save_matrix(temp.matrix)
    elif(x == "6"):
        result = temp.lu()
        print("L: ")
        for i in range(len(result[0])):
            print(result[0][i])
        print("\n")
        print("U: ")
        for i in range(len(result[1])):
            print(result[1][i])
    elif(x == "7"):
        print("Определитель: ", temp.determinant())
    elif(x == "8"):
        print("Обратная матрица:")
        if(temp.inverse() != 0):
            for i in temp.inverse():
                print(i)
    elif(x == "9"):
        b = input_matrix()
        result = temp.ax_b(b = b)
        if(result != 0):
            for i in result:
                print(i)
    elif(x == "10"):
        b = input_matrix()
        result = temp.seidel(b = b)
        if(result != 0):
            for i in result:
                print(i)
    elif(x == "11"):
        result = temp.cholesky_decomposition()
        print(result)
    elif(x == "12"):
        result = temp.condition_number()
        print(result)
    elif(x == "0"):
        return True
    else:
        print("Некорректный ввод")
    return False

def vector_menu(temp):
    print("\n")
    print("1. Вывести вектор")
    print("2. 1 норма")
    print("3. 2 норма")
    print("4. 3 норма")
    
    print("121. Сохранить вектор")
    print("\n0. Выйти")

    x = input()
    os.system(comand)
    if(x == "1"):
        print("Вектор: ")
        for i in temp.matrix:
            print(i)
    elif(x == "2"):
        print("1 норма: ", temp.norm1_vector())
    elif(x == "3"):
        print("2 норма: ", temp.norm2_vector())   
    elif(x == "4"):
        print("3 норма: ", temp.norm3_vector())
    elif(x == "121"):
        save_matrix(temp.matrix)
    elif(x == "0"):
        return True
    else:
        print("Некорректный ввод")
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
