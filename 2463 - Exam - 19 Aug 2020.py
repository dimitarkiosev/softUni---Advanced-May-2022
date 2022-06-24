https://judge.softuni.org/Contests/Practice/Index/2463
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Taxi Express
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

customers = deque()
for x in input().split(', '):
    customers.append(int(x))

taxis = [int(x) for x in input().split(', ')]

all_time = 0

while taxis and customers:
    customer = customers[0]
    taxi = taxis[-1]
    if taxi >= customer:
        all_time += customer
        customers.popleft()
        taxis.pop()
    else:
        taxis.pop()

if customers:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(x) for x in customers])}')
else:
    print(f'All customers were driven to their destinations')
    print(f'Total time: {all_time} minutes')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Minesweeper Generator
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def add_value(row, col, matrix):
    moves = [
    (0, -1),  # LEFT
    (-1, -1),  # UP-LEFT DIAGONAL
    (-1, 0),  # UP
    (-1, 1),  # UP-RIGHT DIAGONAL
    (0, 1),  # RIGHT
    (1, 1),  # DOWN-RIGHT DIAGONAL
    (1, 0),  # DOWN
    (1, -1)  # DOWN-LEFT DIAG
 ]
    for move in moves:
        n_row = int(row) + int(move[0])
        n_col = int(col) + int(move[1])
        if is_inside(n_row, n_col, len(matrix)):
            if matrix[n_row][n_col] != '*':
                matrix[n_row][n_col] += 1

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


my_size = int(input())
matrix = list()

for row in range(my_size):
    ll = list()
    for col in range(my_size):
        ll.append(0)
    matrix.append(ll)

bombs = int(input())

for _ in range(bombs):
    bomb = input()
    coord = bomb[1:-1].split(', ')
    row = int(coord[0])
    col = int(coord[1])
    matrix[row][col] = '*'
    add_value(row, col, matrix)

for each in matrix:
    print(*each, sep=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. Numbers Search
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def numbers_searching(*args):
    num_list = args
    min_n = min(num_list)
    max_n = max(num_list)
    missing = 0
    duplicate = list()
    for x in range(min_n, max_n+1):
        count = 0
        for y in num_list:
            if y == x:
                count += 1
        if count > 1:
            duplicate.append(x)
        if count == 0:
            missing = x

    return [missing, duplicate]

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 