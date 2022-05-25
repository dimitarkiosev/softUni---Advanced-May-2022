= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Numbers
= = = = = = = = = = = = = = = = = = = = = = = = =
seq1 = set(int(x) for x in input().split())
seq2 = set(int(x) for x in input().split())
n = int(input())

for _ in range(n):
    line = input().split()
    command = line[0]
    target = line[1]
    if command == 'Add':
        if target == 'First':
            seq1 = seq1.union([int(x) for x in line[2:]])
        elif target == 'Second':
            seq2 = seq2.union([int(x) for x in line[2:]])
    elif command == 'Remove':
        if target == 'First':
            seq1 = seq1.difference([int(x) for x in line[2:]])
        elif target == 'Second':
            seq2 = seq2.difference([int(x) for x in line[2:]])
    else:
        print(seq1.issubset(seq2) or seq2.issubset(seq1))

print(*sorted(seq1), sep=", ")
print(*sorted(seq2), sep=", ")

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Expression Evaluator
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

my_string = input().split()

operations = {
    '+' : lambda a, b: a + b,
    '-' : lambda a, b: a - b,
    '*' : lambda a, b: a * b,
    '/' : lambda a, b: a // b,
}
numbers = deque()

for ch in my_string:
    if ch in '+-*/':
        while len(numbers) > 1:
            left = numbers.popleft()
            right = numbers.popleft()
            result = operations[ch](left,right)
            numbers.appendleft(result)
    else:
        numbers.append(int(ch))

print(numbers[0])

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Milkshakes
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milks = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolates and milks and milkshakes < 5:
    choco = chocolates.pop()
    milk = milks.popleft()

    # choco and milk == 0
    if choco <= 0 and milk <= 0:
        continue
    # choco == 0
    if choco <= 0:
        milks.appendleft(milk)
        continue
    # milk == 0
    if milk <= 0:
        chocolates.append(choco)
        continue

    if choco == milk:
        milkshakes += 1
    else:
        milks.append(milk)
        chocolates.append(choco - 5)

if milkshakes == 5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')

if chocolates:
    print(f'Chocolate: {", ".join([str(x) for x in chocolates])}')
else:
    print(f'Chocolate: empty')

if milks:
    print(f'Milk: {", ".join([str(x) for x in milks])}')
else:
    print(f'Milk: empty')

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Honey
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
operators = deque(input().split())

honey = 0

operations = {
    '+' : lambda a, b: a + b,
    '-' : lambda a, b: a - b,
    '*' : lambda a, b: a * b,
    '/' : lambda a, b: a / b
}

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if nectar < bee:
        bees.appendleft(bee)
        continue

    if nectar == 0:
        continue

    operator = operators.popleft()
    honey += abs(operations[operator](bee, nectar))

print(f'Total honey made: {honey}')
if bees:
    print(f'Bees left: {", ".join([str(x) for x in bees])}')
if nectars:
    print(f'Nectar left: {", ".join([str(x) for x in nectars])}')
    
= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Santa's Present Factory
= = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])

presents = {
    400: ['Bicycle', 0],
    150: ['Doll', 0],
    300: ['Teddy bear', 0],
    250: ['Wooden train', 0]
}
while materials and magics:
    material = materials.pop()
    magic = magics.popleft()

    if material == 0 and magic == 0:
        continue
    if material == 0:
        magics.appendleft(magic)
        continue
    if magic == 0:
        materials.append(material)
        continue

    result = material * magic
    if result in presents.keys():
        presents[result][1] += 1
        continue

    if result < 0:
        materials.append(material + magic)
    else:
        materials.append(material + 15)

if (presents[150][1] > 0 and presents[250][1] > 0) or (presents[300][1] > 0 and presents[400][1] > 0):
    print(f'The presents are crafted! Merry Christmas!')
else:
    print(f'No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')
if magics:
    print(f'Magic left: {", ".join([str(x) for x in magics])}')

for toy, count in presents.items():
    if count[1] > 0:
        print(f'{count[0]}: {count[1]}')

= = = = = = = = = = = = = = = = = = = = = = = = = 
06. Paint Color
= = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque
my_string = deque(input().split())
main = ('red', 'yellow', 'blue')
secondary = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}
colors = list()
end_colors = list()

while my_string:
    c2 = ''
    c1 = my_string.popleft()
    if len(my_string) > 0:
        c2 = my_string.pop()
    result = c1+c2
    if result in main or result in secondary.keys():
        colors.append(result)
        continue
    result = c2+c1
    if result in main or result in secondary.keys():
        colors.append(result)
        continue

    c1 = c1[:-1]
    c2 = c2[:-1]
    if c1:
        my_string.insert(len(my_string) // 2, c1)
    if c2:
        my_string.insert(len(my_string) // 2, c2)

for color in colors:
    if color in main:
        end_colors.append(color)
    else:
        if secondary[color][0] in colors and secondary[color][1] in colors:
            end_colors.append(color)

print(end_colors)

= = = = = = = = = = = = = = = = = = = = = = = = = 
