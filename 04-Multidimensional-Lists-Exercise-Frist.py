= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Diagonals
= = = = = = = = = = = = = = = = = = = = = = = = =
n = int(input())
matrix = []
primary = list()
second = list()
primary_sum = 0
second_sum = 0

for i in range(n):
    ll = [int(x) for x in input().split(', ')]
    matrix.append(ll)

for i in range(n):
    primary.append(str(matrix[i][i]))
    primary_sum += matrix[i][i]
    second.append(str(matrix[i][n - i - 1]))
    second_sum += matrix[i][n - i - 1]

print(f'Primary diagonal: {", ".join(primary)}. Sum: {primary_sum}')
print(f'Secondary diagonal: {", ".join(second)}. Sum: {second_sum}')

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Diagonal Difference
= = = = = = = = = = = = = = = = = = = = = = = = =
n = int(input())
matrix = []
primary = list()
second = list()
primary_sum = 0
second_sum = 0

for i in range(n):
    ll = [int(x) for x in input().split()]
    matrix.append(ll)

for i in range(n):
    primary.append(matrix[i][i])
    second.append(matrix[i][n - i - 1])

diff = abs(sum(primary) - sum(second))

print(diff)

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. 2x2 Squares in Matrix
= = = = = = = = = = = = = = = = = = = = = = = = = 
line = input().split()
n = int(line[0])
m = int(line[1])

matrix = []
count1 = 0

for i in range(n):
    ll = [x for x in input().split()]
    matrix.append(ll)

for i in range(n-1):
    for j in range(m-1):
        if matrix[i][j] == matrix[i+1][j] == matrix[i][j+1] == matrix[i+1][j+1]:
            count1 += 1

print(count1)

= = = = = = = = = = = = = = = = = = = = = = = = =
04. Maximal Sum
= = = = = = = = = = = = = = = = = = = = = = = = = 
line = input().split()
n = int(line[0])
m = int(line[1])

matrix = []
max_matrix = []
max_sum = 0

for i in range(n):
    ll = [int(x) for x in input().split()]
    matrix.append(ll)

for i in range(n-2):
    for j in range(m-2):
        temp_sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
        if temp_sum >= max_sum:
            max_sum = temp_sum
            max_matrix = [
                [str(matrix[i][j]), str(matrix[i][j+1]), str(matrix[i][j+2])],
                [str(matrix[i+1][j]), str(matrix[i+1][j+1]), str(matrix[i+1][j+2])],
                [str(matrix[i+2][j]), str(matrix[i+2][j+1]), str(matrix[i+2][j+2])]
            ]

print(f'Sum = {max_sum}')
for row in max_matrix:
    print(" ".join(row))

= = = = = = = = = = = = = = = = = = = = = = = = =
05. Matrix of Palindromes
= = = = = = = = = = = = = = = = = = = = = = = = = 
letters = 'abcdefghijklmnopqrstuvxyz'
n, m = [int(x) for x in input().split()]
matrix = []

for i in range(n):
    ll = list()
    for j in range(m)
        element = letters[i] + letters[i+j] + letters[i]
        ll.append(element)
    matrix.append(ll)
    
print(matrix)

= = = = = = = = = = = = = = = = = = = = = = = = =
06. Matrix Shuffling
= = = = = = = = = = = = = = = = = = = = = = = = =
def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols

n, m = [int(x) for x in input().split()]
matrix = []

for i in range(n):
    ll = [int(x) for x in input().split()]
    matrix.append(ll)

while True:
    line = input().split()
    if line[0] == 'END':
        break
    elif len(line) != 5 or line[0] != 'swap':
        print(f'Invalid input!')
    elif line[0] == 'swap':
        row_index = int(line[1])
        col_index = int(line[2])
        row_index_2 = int(line[3])
        col_index_2 = int(line[4])
        if is_outside(row_index, col_index, n, m) or is_outside(row_index_2, col_index_2, n, m):
            print(f'Invalid input!')
        else:
            a = matrix[row_index][col_index]
            matrix[row_index][col_index] = matrix[row_index_2][col_index_2]
            matrix[row_index_2][col_index_2] = a
            for row in matrix:
                print(" ".join([str(x) for x in row]))

= = = = = = = = = = = = = = = = = = = = = = = = =
07. Snake Moves
= = = = = = = = = = = = = = = = = = = = = = = = = 
n, m = [int(x) for x in input().split()]
word = input()
matrix = []
indx = 0

for i in range(n):
    ll = [None] * m
    if i % 2 == 0:
        for col in range(m):
            ll[col] = word[indx % len(word)]
            indx += 1
    else:
        for col in range(m):
            ll[m - col - 1] = word[indx % len(word)]
            indx += 1
    print(''.join(ll))

= = = = = = = = = = = = = = = = = = = = = = = = =
08. Bombs
= = = = = = = = = = = = = = = = = = = = = = = = = 

= = = = = = = = = = = = = = = = = = = = = = = = =
09. Miner
= = = = = = = = = = = = = = = = = = = = = = = = = 

= = = = = = = = = = = = = = = = = = = = = = = = =
10. Radioactive Mutate Vampire Bunnies
= = = = = = = = = = = = = = = = = = = = = = = = = 

= = = = = = = = = = = = = = = = = = = = = = = = =
