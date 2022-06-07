= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Flatten Lists
= = = = = = = = = = = = = = = = = = = = = = = = =
list1 = input().split('|')

result = []

for x in range(len(list1) -1, -1, -1):
    current_el = list1[x].strip().split()
    result.extend(current_el)

print(' '.join(result))

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Matrix Modification
= = = = = = = = = = = = = = = = = = = = = = = = =
def is_valid(row, col, n):
    return row < 0 or col < 0 or row >= n or col >= n

n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == 'END':
        break
    command = line.split()[0]
    row = int(line.split()[1])
    col = int(line.split()[2])
    value = int(line.split()[3])

    if is_valid(row, col, n):
        print(f'Invalid coordinates')
    elif command == 'Add':
        matrix[row][col] += value
    elif command == 'Subtract':
        matrix[row][col] -= value

for each in matrix:
    print(*each, sep=' ')
    
= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Knight Game
= = = = = = = = = = = = = = = = = = = = = = = = =
def knight_count(board, row, col):
    result = 0
    size = len(board)
    all_k = [
        [row + 2, col + 1],
        [row + 2, col - 1],
        [row + 1, col + 2],
        [row + 1, col - 2],
        [row - 2, col + 1],
        [row - 2, col - 1],
        [row - 1, col + 2],
        [row - 1, col - 2]
    ]
    for r, c in all_k:
        if 0 <= r < size and 0 <= c < size and board[r][c] == 'K':
            result += 1
    return result

n = int(input())
matrix = []
removed_k = 0

for _ in range(n):
    matrix.append(list(input()))

while True:
    best_count = 0
    k_row = 0
    k_col = 0
    for x in range(n):
        for y in range(n):
            if matrix[x][y] == '0':
                continue
            k_count = knight_count(matrix, x, y)
            if k_count >= best_count:
                best_count = k_count
                k_row = x
                k_col = y

    if best_count == 0:
        break

    matrix[k_row][k_col] = '0'
    removed_k += 1

print(removed_k)

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Easter Bunny
= = = = = = = = = = = = = = = = = = = = = = = = =


= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Alice in Wonderland
= = = = = = = = = = = = = = = = = = = = = = = = =
def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1

size = int(input())
matrix = []
a_row = 0
a_col = 0
tea = 0

for row in range(size):
    ll = input().split()
    for col in range(len(ll)):
        if ll[col] == 'A':
            a_row = row
            a_col = col
    matrix.append(ll)

while tea < 10:
    matrix[a_row][a_col] = '*'
    direction = input()

    new_row, new_col = get_next_pos(a_row, a_col, direction)
    if new_row < 0 or new_col < 0 or new_row >= size or new_col >= size:
        break

    a_row, a_col = get_next_pos(a_row, a_col, direction)
    if matrix[a_row][a_col] == '.' or matrix[a_row][a_col] == '*':
        continue

    if matrix[a_row][a_col] == 'R':
        break

    tea += int(matrix[a_row][a_col])

matrix[a_row][a_col] = '*'

if tea >= 10:
    print(f'She did it! She went to the party.')
else:
    print(f"Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=' ')
    
= = = = = = = = = = = = = = = = = = = = = = = = = 
06. Range Day
= = = = = = = = = = = = = = = = = = = = = = = = =
a_row = 0
a_col = 0
all_targets = 0
reached_targets = []
matrix = []

for row in range(5):
    ll = input().split()
    for col in range(5):
        if ll[col] == 'A':
            a_row = row
            a_col = col
        if ll[col] == 'x':
            all_targets += 1
    matrix.append(ll)

count = int(input())
for x in range(count):
    line = input().split()
    command = line[0]
    new_row = 0
    new_col = 0

    if command == 'shoot':
        direction = line[1]
        if direction == 'right':
            for col in range(a_col + 1, 5):
                if matrix[a_row][col] == 'x':
                    reached_targets.append([a_row, col])
                    matrix[a_row][col] = '.'
                    break

        elif direction == 'left':
            for col in range(a_col - 1, -1, -1):
                if matrix[a_row][col] == 'x':
                    reached_targets.append([a_row, col])
                    matrix[a_row][col] = '.'
                    break

        elif direction == 'up':
            for row in range(a_row - 1, -1, -1):
                if matrix[row][a_col] == 'x':
                    reached_targets.append([row, a_col])
                    matrix[row][a_col] = '.'
                    break

        elif direction == 'down':
            for row in range(a_row + 1, 5):
                if matrix[row][a_col] == 'x':
                    reached_targets.append([row, a_col])
                    matrix[row][a_col] = '.'
                    break

    elif command == 'move':
        direction = line[1]
        steps = int(line[2])
        if direction == 'right':
            new_row = a_row
            new_col = a_col + steps
        elif direction == 'left':
            new_row = a_row
            new_col = a_col - steps
        elif direction == 'up':
            new_row = a_row - steps
            new_col = a_col
        elif direction == 'down':
            new_row = a_row + steps
            new_col = a_col

        if 0 <= new_row < 5 and 0 <= new_col < 5 and matrix[new_row][new_col] == '.':
            matrix[new_row][new_col] = 'A'
            matrix[a_row][a_col] = '.'
            a_row = new_row
            a_col = new_col

if len(reached_targets) == all_targets:
    print(f'Training completed! All {all_targets} targets hit.')
else:
    print(f'Training not completed! {all_targets - len(reached_targets)} targets left.')

if reached_targets:
    for each in reached_targets:
        print(each)

= = = = = = = = = = = = = = = = = = = = = = = = = 
07. Present Delivery
= = = = = = = = = = = = = = = = = = = = = = = = =
presents = int(input())
size = int(input())
matrix = []

s_row = 0
s_col = 0
all_nice_kids = 0
nice_kids = 0

for row in range(size):
    ll = [x for x in input().split()]
    for col in range(size):
        if ll[col] == 'S':
            s_row = row
            s_col = col
        elif ll[col] == 'V':
            all_nice_kids += 1
    matrix.append(ll)

out_present = False

while True:
    new_row = 0
    new_col = 0
    line = input()
    
    if line == 'Christmas morning':
        break
    elif line == 'up':
        new_row = s_row - 1
        new_col = s_col
    elif line == 'down':
        new_row = s_row + 1
        new_col = s_col
    elif line == 'left':
        new_row = s_row
        new_col = s_col - 1
    elif line == 'right':
        new_row = s_row
        new_col = s_col + 1

    if 0 <= new_row < size and 0 <= new_col < size:
        matrix[s_row][s_col] = '-'
        s_row = new_row                     # adding new coordinates - row
        s_col = new_col                     # adding new coordinates - col
        house = matrix[s_row][s_col]        # get value of new house

        if house == 'V' and presents > 0:                    # nice kid in house
            presents -= 1
            nice_kids += 1

        elif house == 'C' and presents > 0:                                  # cookies in house - presents for all kids around
            if 0 <= (s_col - 1) < 5 and presents > 0:        # around him - LEFT
                if matrix[s_row][s_col - 1] in 'XV':
                    if matrix[s_row][s_col - 1] == 'V':
                        nice_kids += 1
                    presents -= 1
                    matrix[s_row][s_col - 1] = '-'
            
            if 0 <= (s_col + 1) < 5 and presents > 0:        # around him - RIGHT
                if matrix[s_row][s_col + 1] in 'XV':
                    if matrix[s_row][s_col + 1] == 'V':
                        nice_kids += 1
                    presents -= 1
                    matrix[s_row][s_col + 1] = '-'
                    
            if 0 <= (s_row - 1) < 5 and presents > 0:        # around him - UP
                if matrix[s_row - 1][s_col] in 'XV':
                    if matrix[s_row - 1][s_col] == 'V':
                        nice_kids += 1
                    presents -= 1
                    matrix[s_row - 1][s_col] = '-'

            if 0 <= (s_row + 1) < 5 and presents > 0:        # around him - DOWN
                if matrix[s_row + 1][s_col] in 'XV':
                    if matrix[s_row + 1][s_col] == 'V':
                        nice_kids += 1
                    presents -= 1
                    matrix[s_row + 1][s_col] = '-'
    
    matrix[s_row][s_col] = 'S'

    if presents == 0:
        out_present = True
        break

if out_present:
    print(f'Santa ran out of presents!')

for row in matrix:
    print(*row, sep=' ')

if all_nice_kids == nice_kids:
    print(f'Good job, Santa! {all_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {all_nice_kids - nice_kids} nice kid/s.')
        
= = = = = = = = = = = = = = = = = = = = = = = = =
