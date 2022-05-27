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

= = = = = = = = = = = = = = = = = = = = = = = = =
06. Matrix Shuffling
= = = = = = = = = = = = = = = = = = = = = = = = = 

= = = = = = = = = = = = = = = = = = = = = = = = =
07. Snake Moves
= = = = = = = = = = = = = = = = = = = = = = = = = 

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