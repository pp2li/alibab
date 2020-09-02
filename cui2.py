import sys


# with open('czy_input.txt', 'r') as f:
#     N = int(f.readline().strip())
#     red_list = []
#     blue_list = []
#     child = []
#     for idx in range(N):
#         temp = list(map(int, f.readline().strip().split()))
#
#         if temp[1] == 1:
#             red_list.append((idx+1, temp[0]))
#         if temp[1] == 2:
#             blue_list.append((idx+1, temp[0]))

import sys
N = int(sys.stdin.readline().strip())
red_list = []
blue_list = []
child = []
for idx in range(N):
    temp = list(map(int, sys.stdin.readline().strip().split()))

    if temp[1] == 1:
        red_list.append((idx+1, temp[0]))
    if temp[1] == 2:
        blue_list.append((idx+1, temp[0]))


def find_max3(alist):
    _max = [0, 0, 0]
    _index = [-1, -1, -1]
    for idx in range(3):
        for child, num in alist:
            if _max[idx] < num and child not in set(_index):
                _max[idx] = num
                _index[idx] = child
    return _index, sum(_max)


def find_max(red_list, blue_list):
    if len(red_list) <3 and len(blue_list) < 3:
        return 'null', 'null', 'null'

    redindex, red_sum = find_max3(red_list)

    blueindex, blue_sum = find_max3(blue_list)
    if red_sum > blue_sum:
        return redindex, red_sum, 1
    if red_sum < blue_sum:
        return blueindex, blue_sum, 2

    if red_sum == blue_sum:
        if min(redindex) < min(blueindex):
            return redindex, red_sum, 1
        if min(redindex) > min(blueindex):
            return blueindex, blue_sum, 2


indexoutput, sum_output, cat = find_max(red_list, blue_list)
if sum_output == 'null':
    print 'null'
else:
    print ' '.join(map(str, indexoutput[::-1]))
    print cat
    print sum_output











