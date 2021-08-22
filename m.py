import random

def add_sub():
     rows = int(input("Input the number of rows of the matrices: " ))
     column = int(input("Input the number of columns of the matrices: "))

     print("\nInput the elements of Matrix A:")
     matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
     print("Matrix A is: ")
     for n in matrix_a:
         print(n)

     print("\nInput the elements of Matrix B:")
     matrix_b= [[int(input()) for i in range(column)] for i in range(rows)]
     print("Matrix B is: ")
     for n in matrix_b:
         print(n)

     result=[[0 for i in range(column)] for i in range(rows)]

     for i in range(rows):
         for j in range(column):
             if (choice == 1):
                 result[i][j] = matrix_a[i][j]+matrix_b[i][j]
             elif (choice == 2):
                 result[i][j] = matrix_a[i][j]-matrix_b[i][j]

     if (choice == 1): 
         print("\nSum of the Matrices: ")
     elif (choice == 2): 
         print("\nDifference of the Matrices: ")

     for r in result:
         print(r)

    
def multiply(): #Num of columns in Matrix A = Num of rows in Matrix B
    print("Matrix A:")
    numRows1=int(input("Number of Rows: "))
    numCols1=int(input("Number of Columns: "))
    print("Enter elements of Matrix A:")
    matrix_a = [[random.random() for col in range(numCols1)] for row in range(numRows1)]
    for i in range(numRows1):
        for j in range(numCols1):
            matrix_a[i][j]=int(input())
    print("Matrix A is:")
    for a in matrix_a:
        print(a)
    
    print("\nMatrix B:")
    numRows2=int(input ("Number of Rows: "))
    numCols2=int(input ("Number of Columns: "))  
    if (numCols1==numRows2):
        print("Enter elements of Matrix B:")
        matrix_b = [[random.random() for col in range(numCols2)] for row in range(numRows2)]
        for i in range(numRows2):
            for j in range(numCols2):
                matrix_b[i][j]=int(input())
        print("Matrix B is:")
        for b in matrix_b:
            print(b)
        results=[[random.random()for col in range(numCols2)]for row in range(numRows1)]

        print("\nProduct of the Matrices: ")
        for i in range(numRows1):
            for j in range(numCols2):
                results[i][j]=0
                for k in range(numCols1):
                    results[i][j]+=matrix_a[i][k]*matrix_b[k][j]
        for r in results:
            print(r)
    else:
        print("\nMatrix multiplication is not possible for these matrices. \nThe number of columns in the 1st matrix should be equal to the number of rows in the 2nd matrix.")

if __name__ == '__main__':
    print("MATRIX OPERATIONS PROGRAM")
    inputU = 1
    while (inputU != 0):
        global choice 
        choice = int(input("Matrix Operations: [1]Addition [2]Subtraction [3]Multiplication \nChoose which operation to do: " ))
        if (choice == 1):
            print("\nMATRIX ADDITION")
            add_sub()
        elif (choice == 2):
            print("\nMATRIX SUBTRACTION")
            add_sub()
        elif (choice == 3):
            print("\nMATRIX MULTIPLICATION")
            multiply()
        inputU=int(input ("Do you want to continue the program?[0]No [1]Yes: "))  
        

