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
    rows_a = int(input("Number of Rows: " ))
    column_a = int(input("Number of Columns: "))

    print("Input the elements of Matrix A:")
    matrix_a= [[int(input()) for i in range(column_a)] for i in range(rows_a)]

    print("Matrix A is: ")
    for n in matrix_a:
        print(n)
    
    #the number of columns of first matrix should be equal to the number of rows of second matrix
    print("Matrix B:")
    rows_a = int(input("Number of Rows: " ))
    column_b = int(input("Number of Columns: "))
    if (column_a == rows_a):
        print("Input the elements of Matrix B:")

        matrix_b = [[int(input()) for i in range(column_b)] for i in range(column_a)]
        print("Matrix B is:")
        for n in matrix_b:
            print(n)
            
        result=[[0 for i in range(column_b)] for i in range(rows_a)]

        for i in range(len(matrix_a)): #iterating row A
            for j in range(len(matrix_b[0])): #iterating column B
                for k in range(len(matrix_b)): #iterating row B
                    result [i][j]+=matrix_a[i][k]*matrix_b[k][j]
        print("\nProduct of the Matrices: ")
        for r in result:
            print(r)
    else:
        print("Multiplication not possible. \nThe number of columns in the 1st matrix should be equal to the number of rows in the 2nd matrix.")

if __name__ == '__main__':
    global choice 
    choice = int(input("Matrix Operations: \n[1]Addition [2]Subtraction [3]Multiplication \nChoose which operation to do: " ))
    if (choice == 1):
        print("\nMATRIX ADDITION")
        add_sub()
    elif (choice == 2):
        print("\nMATRIX SUBTRACTION")
        add_sub()
    elif (choice == 3):
        print("\nMATRIX MULTIPLICATION")
        multiply()


