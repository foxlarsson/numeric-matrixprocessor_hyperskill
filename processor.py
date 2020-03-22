def build_matrix(rows):
    matrix = []
    for item in range(rows):
        matrix.append([int(i) for i in input().split()])
    return matrix


def get_num_rows_and_columns():
    return map(int, input().split())


def construct_matrices():
    num_rows_a, num_columns_a = get_num_rows_and_columns()
    matrix_a = build_matrix(num_rows_a)
    num_rows_b, num_columns_b = get_num_rows_and_columns()
    matrix_b = build_matrix(num_rows_b)
    return matrix_a, matrix_b


def check_matrix_alignment(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return False


def add_matrices(matrix_a, matrix_b):
    num_rows = len(matrix_a)
    matrix_sum = []
    for row in range(num_rows):
        matrix_sum.append(list(map(lambda x, y: x + y, matrix_a[row], matrix_b[row])))
    return matrix_sum


def print_matrix(matrix):
    for row in range(len(matrix)):
        print(*matrix[row])


def main():
    matrix_a, matrix_b = construct_matrices()
    if check_matrix_alignment(matrix_a, matrix_b) is False:
        print('ERROR')
        exit()
    matrix_sum = add_matrices(matrix_a, matrix_b)
    print_matrix(matrix_sum)


main()
