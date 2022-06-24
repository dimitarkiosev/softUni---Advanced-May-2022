https://judge.softuni.org/Contests/Practice/Index/2720
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Matching
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

males = [int(x) for x in input().split()]
females = deque()
matchesCount = 0

for x in input().split():
    females.append(int(x))

while males and females:
    male = males[-1]
    female = females[0]

    if male <= 0:
        males.pop()
        continue
    if male % 25 == 0:
        males.pop()
        continue

    if female <= 0:
        females.popleft()
        continue

    if female % 25 == 0:
        females.popleft()
        continue

    if male == female:
        males.pop()
        females.popleft()
        matchesCount += 1
    else:
        females.popleft()
        males[-1] -= 2

print(f'Matches: {matchesCount}')
if males:
    print(f"Males left: {', '.join([str(x) for x in reversed(males)])}")
else:
    print(f'Males left: none')

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print(f'Females left: none')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Game of Words
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def get_next(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1

def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size

my_string = input()
my_size = int(input())
matrix = list()

for x in range(my_size):
    ll= list()
    temp_ll = input()
    for each in temp_ll:
        ll.append(each)
    for y in range(len(ll)):
        if ll[y] == 'P':
            p_row = x
            p_col = y
    matrix.append(ll)

num_com = int(input())

for _ in range(num_com):
    command = input()
    n_row, n_col = get_next(p_row, p_col, command)
    if is_inside(n_row, n_col, my_size):
        if matrix[n_row][n_col] != '-':
            my_string = my_string + matrix[n_row][n_col]
        matrix[n_row][n_col] = 'P'
        matrix[p_row][p_col] = '-'
        p_row, p_col = n_row, n_col
    else:
        my_string = my_string[:-1]

print(my_string)
for row in matrix:
    print(*row, sep='')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. Magic Triangle
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def get_magic_triangle(n):
    triangle = [[1], [1, 1]]
    for x in range(n-2):
        prev = triangle[-1]
        next = []
        for y in range(len(prev)+1):
            if y == 0:
                next.append(prev[0])
            elif y != len(prev):
                next.append(prev[y-1] + prev[y])
            else:
                next.append(prev[-1])
        triangle.append(next)

    return triangle

print(get_magic_triangle(5))

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 