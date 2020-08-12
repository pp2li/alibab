import sys

with open('czy_input.txt', 'r') as f:
    n = f.readline().strip()

    alist = list(map(int, f.readline().strip().split(' ')))