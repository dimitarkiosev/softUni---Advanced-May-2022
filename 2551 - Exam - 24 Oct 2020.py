https://judge.softuni.org/Contests/Practice/Index/2551
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Scheduling
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
jobs =  [int(x) for x in input().split(', ')]
target = int(input())
removed = list()
clock_cycles = 0

is_ready = False
while True:
    min_el = float('inf')
    for x in range(len(jobs)-1,-1,-1):
        if jobs[x] <= min_el and x not in removed:
            min_el = jobs[x]
            min_in = x
    clock_cycles += min_el
    removed.append(min_in)
    if min_in == target:
        is_ready = True
        break

print(clock_cycles)

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Checkmate
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size

my_size = 8
matrix = list()

for row in range(my_size):
    ll = input().split()
    for col in range(len(ll)):
        if ll[col] == 'K':
            king_row = row
            king_col = col
    matrix.append(ll)

queen_list = list()

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
    row = king_row
    col = king_col
    while True:
        row += move[0]
        col += move[1]
        if is_inside(row,col,8):
            if matrix[row][col] == 'Q':
                queen_list.append([row, col])
                break
        else:
            break

if queen_list:
    print(*queen_list, sep='\n')
else:
    print(f'The king is safe!')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. List Pureness
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def best_list_pureness(*args):
    my_list = args[0]
    num_rot = args[1]
    max_sum = -9999999999
    max_rot = 0
    for x in range(num_rot+1):
        my_sum = 0
        for y in range(len(my_list)):
            my_sum += y * my_list[y]
        temp = my_list.pop()
        my_list.insert(0, temp)
        if my_sum > max_sum:
            max_sum = my_sum
            max_rot = x
    return f'Best pureness {max_sum} after {max_rot} rotations'

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 