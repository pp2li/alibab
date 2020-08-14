import sys

# with open('czy_input.txt', 'r') as f:
#     N, d = list(map(int, f.readline().strip().split(' ')))
#     matrix = [list(map(int, f.readline().strip().split(' '))) for _ in range(N)]

N, d = list(map(int, sys.stdin.readline().strip().split(' ')))
matrix = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(N)]

def dream(matrix, N, d):
    if N == 0:
        return -1
    max_matrix = matrix[0][0]
    for idx in range(N):
        for jdx in range(N):
            if matrix[idx][jdx] % d != 0:
                return -1
            if max_matrix < matrix[idx][jdx]:
                max_matrix = matrix[idx][jdx]

    output_num = 0
    for idx in range(N):
        for jdx in range(N):
            output_num += (max_matrix - matrix[idx][jdx]) / d
    return output_num


print dream(matrix, N, d)
