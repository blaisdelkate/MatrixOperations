def add_sub():
    rows = int(input("Enter the number of rows : " ))
    column = int(input("Enter the number of columns: "))
        
    print("\nEnter the elements of First Matrix:")
    matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
    print("First Matrix is: ")
    for n in matrix_a:
        print(n)

    print("\nEnter the elements of Second Matrix:")
    matrix_b= [[int(input()) for i in range(column)] for i in range(rows)]
    for n in matrix_b:
        print(n)
        
    result=[[0 for i in range(column)] for i in range(rows)]

    for i in range(rows):
        for j in range(column):
            if (choice == 1):
                result[i][j] = matrix_a[i][j]+matrix_b[i][j]
            elif (choice == 2):
                result[i][j] = matrix_a[i][j]-matrix_b[i][j]

    print("\nSum of the Matrices: ")
    for r in result:
        print(r)

def multiply():
    # Program to multiply two matrices using nested loops
    #Num of columns in Matrix A = Num of rows in Matrix B
    # take a 3x3 matrix
    A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]

    # take a 3x4 matrix
    B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]
        
    result = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

    # iterating by row of A
    for i in range(len(A)):

        # iterating by column by B
        for j in range(len(B[0])):

            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    for r in result:
        print(r)

if __name__ == '__main__':
    global choice 
    choice = int(input("Matrix Operations: \n[1]Addition [2]Subtraction [3]Multiplication \nChoose which operation to do: " ))
    if (choice == 1):
        add_sub()
    elif (choice == 3):
        multiply()


