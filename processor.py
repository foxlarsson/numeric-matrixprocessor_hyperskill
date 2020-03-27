def choose_action():
    options = '''
            1. Add matrices
            2. Multiply matrix by a constant
            3. Multiply matrices
            4. Transpose matrix
            0. Exit
            Your choice: '''
    return input(options)


def choose_transposition():
    options = '''
            1. Main diagonal
            2. Side diagonal
            3. Vertical line
            4. Horizontal line
            Your choice: '''
    return input(options)


def get_num_rows_and_columns():
    return map(int, input().split())


def construct_matrix(num_rows, num_columns):
    matrix = []
    for row in range(num_rows):
        matrix.append([float(i) for i in input().split()])
    return matrix


def check_matrices_for_sum(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return False


def check_matrices_for_multiplication(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return False


def add_matrices(matrix_a, matrix_b):
    num_rows = len(matrix_a)
    matrix_sum = []
    for row in range(num_rows):
        matrix_sum.append(list(map(lambda x, y: x + y, matrix_a[row], matrix_b[row])))
    return matrix_sum


def multiply_matrix_by_scalar(matrix):
    scalar = float(input('Enter constant: '))
    num_rows = len(matrix)
    matrix_multiplied = []
    for row in range(num_rows):
        matrix_multiplied.append([item * scalar for item in matrix[row]])
    return matrix_multiplied


def multiply_matrices(matrix_a, matrix_b):
    num_rows_a = len(matrix_a)
    num_columns_a = len(matrix_a[0])
    num_columns_b = len(matrix_b[0])
    matrices_multiplied = []
    for row in range(0, num_rows_a):
        new_row = []
        for column in range(0, num_columns_b):
            dot_product = 0
            for index in range(0, num_columns_a):
                dot_product += matrix_a[row][index] * matrix_b[index][column]
            new_row.append(dot_product)
        matrices_multiplied.append(new_row)
    return matrices_multiplied


def transpose_vertical(matrix):
    for row in matrix:
        row.reverse()
    return matrix


def transpose_horizontal(matrix):
    matrix.reverse()
    return matrix


def transpose_main_diagonal(matrix):
    matrix_transposed = []
    for column in range(0, len(matrix[0])):
        matrix_transposed.append([])
        for row in range(0, len(matrix)):
            matrix_transposed[column].append(matrix[row][column])
    return matrix_transposed


def transpose_side_diagonal(matrix):
    matrix_transposed = transpose_horizontal(transpose_vertical(transpose_main_diagonal(matrix)))
    return matrix_transposed


def print_matrix(matrix):
    print('The result is: ')
    if matrix[0][0].is_integer():
        for row in range(len(matrix)):
            print(*(int(item) for item in matrix[row]), sep=' ')
    else:
        for row in range(len(matrix)):
            print(*matrix[row])


def main():
    while True:
        action = choose_action()
        # exit
        if action == '0':
            return False
        # add matrices
        elif action == '1':
            rows_a, columns_a = map(int, input('Enter size of first matrix: ').split())
            print('Enter first matrix: ')
            matrix_a = construct_matrix(rows_a, columns_a)
            rows_b, columns_b = map(int, input('Enter size of second matrix: ').split())
            print('Enter second matrix: ')
            matrix_b = construct_matrix(rows_b, columns_b)
            if check_matrices_for_sum(matrix_a, matrix_b) is False:
                print('ERROR: The operation cannot be performed: number of rows and columns in both matrices should '
                      'match for addition')
            else:
                matrix_sum = add_matrices(matrix_a, matrix_b)
                print_matrix(matrix_sum)
        # multiply matrix by scalar
        elif action == '2':
            rows, columns = map(int, input('Enter size of matrix: ').split())
            print('Enter matrix: ')
            matrix = construct_matrix(rows, columns)
            matrix_multiplied = multiply_matrix_by_scalar(matrix)
            print_matrix(matrix_multiplied)
        # multiply matrices
        elif action == '3':
            rows_a, columns_a = map(int, input('Enter size of first matrix: ').split())
            print('Enter first matrix: ')
            matrix_a = construct_matrix(rows_a, columns_a)
            rows_b, columns_b = map(int, input('Enter size of second matrix: ').split())
            print('Enter second matrix: ')
            matrix_b = construct_matrix(rows_b, columns_b)
            if check_matrices_for_multiplication(matrix_a, matrix_b) is False:
                print('ERROR: the number of columns in matrix one must match the number of rows '
                      'in matrix two for multiplication')
            else:
                matrices_multiplied = multiply_matrices(matrix_a, matrix_b)
                print_matrix(matrices_multiplied)
        elif action == '4':
            transposition_type = choose_transposition()
            rows, columns = map(int, input('Enter matrix size: ').split())
            print('Enter matrix: ')
            matrix = construct_matrix(rows, columns)
            if transposition_type == '1':
                matrix_transposed = transpose_main_diagonal(matrix)
            elif transposition_type == '2':
                matrix_transposed = transpose_side_diagonal(matrix)
            elif transposition_type == '3':
                matrix_transposed = transpose_vertical(matrix)
            elif transposition_type == '4':
                matrix_transposed = transpose_horizontal(matrix)
            print_matrix(matrix_transposed)


main()
