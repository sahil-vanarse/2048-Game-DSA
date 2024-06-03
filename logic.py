import random

def start_game():
    matrix = [[0 for _ in range(4)] for _ in range(4)]
    return matrix

def add_two2(matrix):
    row = random.randint(0, 3)
    col = random.randint(0, 3)
    while matrix[row][col] != 0:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
    matrix[row][col] = 2

def get_current_state(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 2048:
                return 'WON'

    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return 'Game Not Finished Yet'

    for i in range(3):
        for j in range(3):
            if matrix[i][j] == matrix[i + 1][j] or matrix[i][j] == matrix[i][j + 1]:
                return 'Game Not Finished Yet'

    for j in range(3):
        if matrix[3][j] == matrix[3][j + 1]:
            return 'Game Not Finished Yet'

    for i in range(3):
        if matrix[i][3] == matrix[i + 1][3]:
            return 'Game Not Finished Yet'

    return 'LOST'

def compress(matrix):
    new_matrix = [[0 for _ in range(4)] for _ in range(4)]
    changed = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_matrix[i][pos] = matrix[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_matrix, changed

def merge(matrix):
    changed = False
    for i in range(4):
        for j in range(3):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                matrix[i][j] *= 2
                matrix[i][j + 1] = 0
                changed = True
    return matrix, changed

def reverse(matrix):
    new_matrix = []
    for i in range(4):
        new_matrix.append(matrix[i][::-1])
    return new_matrix

def transpose(matrix):
    new_matrix = [[matrix[j][i] for j in range(4)] for i in range(4)]
    return new_matrix

def move_left(matrix):
    compressed_matrix, changed1 = compress(matrix)
    merged_matrix, changed2 = merge(compressed_matrix)
    final_matrix, _ = compress(merged_matrix)
    return final_matrix, changed1 or changed2

def move_right(matrix):
    reversed_matrix = reverse(matrix)
    compressed_matrix, changed1 = compress(reversed_matrix)
    merged_matrix, changed2 = merge(compressed_matrix)
    compressed_matrix, _ = compress(merged_matrix)
    final_matrix = reverse(compressed_matrix)
    return final_matrix, changed1 or changed2

def move_up(matrix):
    transposed_matrix = transpose(matrix)
    compressed_matrix, changed1 = compress(transposed_matrix)
    merged_matrix, changed2 = merge(compressed_matrix)
    compressed_matrix, _ = compress(merged_matrix)
    final_matrix = transpose(compressed_matrix)
    return final_matrix, changed1 or changed2

def move_down(matrix):
    transposed_matrix = transpose(matrix)
    reversed_matrix = reverse(transposed_matrix)
    compressed_matrix, changed1 = compress(reversed_matrix)
    merged_matrix, changed2 = merge(compressed_matrix)
    compressed_matrix, _ = compress(merged_matrix)
    reversed_matrix = reverse(compressed_matrix)
    final_matrix = transpose(reversed_matrix)
    return final_matrix, changed1 or changed2

def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

# Example usage
# matrix = start_game()
# add_two2(matrix)
# add_two2(matrix)

# print_matrix(matrix)

# inputs = [int(ele) for ele in input().split()]
# for ele in inputs:
#     if ele == 1:
#         matrix, changed = move_up(matrix)
#     elif ele == 2:
#         matrix, changed = move_down(matrix)
#     elif ele == 3:
#         matrix, changed = move_left(matrix)
#     elif ele == 4:
#         matrix, changed = move_right(matrix)
#     else:
#         print("Invalid move. Please enter 1, 2, 3, or 4.")
#         continue

#     if changed:
#         add_two2(matrix)
#     print_matrix(matrix)

#     state = get_current_state(matrix)
#     if state != 'Game Not Finished Yet':
#         print(state)
#         break
