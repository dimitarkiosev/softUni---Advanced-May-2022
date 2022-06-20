https://judge.softuni.org/Contests/Practice/Index/3306

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Christmas Elves
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

all_toys = 0
elf_energy = 0
count = 0

elfs = deque()
for x in input().split():
    elfs.append(int(x))
materials = [int(x) for x in input().split()]


while elfs and materials:
    elf = elfs.popleft()
    if elf < 5:
        continue
    count += 1
    material = materials.pop()
    if elf >= material:
        if count % 3 == 0 and count % 5 != 0:
            if elf >= 2*material:
                elf -= 2*material
                all_toys += 2
                elf_energy += 2*material
                elf += 1
                elfs.append(elf)
            else:
                materials.append(material)
                elf = elf * 2
                elfs.append(elf)
        elif count % 3 != 0 and count % 5 == 0:
            elf -= material
            elf_energy += material
            elfs.append(elf)
        elif count % 3 == 0 and count % 5 == 0:
            if elf >= 2*material:
                elf -= 2*material
                elf_energy += 2*material
                elfs.append(elf)
            else:
                materials.append(material)
                elf = elf * 2
                elfs.append(elf)
        else:
            elf -= material
            all_toys += 1
            elf_energy += material
            elf += 1
            elfs.append(elf)
    else:
        materials.append(material)
        elf = elf * 2
        elfs.append(elf)

print(f'Toys: {all_toys}')
print(f'Energy: {elf_energy}')

if elfs:
    print(f'Elves left: {", ".join([str(x) for x in elfs])}')
if materials:
    print(f'Boxes left: {", ".join([str(x) for x in materials])}')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. North Pole Challenge
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
rows, cols = [int(x) for x in input().split(', ')]
matrix = list()
collection = {
    'D': 0,
    'G': 0,
    'C': 0
}
all_items = 0
count_items = 0

for x in range(rows):
    ll = input().split()
    for y in range(len(ll)):
        if ll[y] == 'Y':
            pos_row = x
            pos_col = y
        if ll[y] == 'C' or ll[y] == 'D' or ll[y] == 'G':
            all_items += 1
    matrix.append(ll)

is_collected = False
line = input()
while line != 'End':
    direction = line.split('-')[0]
    steps = int(line.split('-')[1])
    if direction == 'up':
        while steps > 0:
            if pos_row - 1 >= 0:
                matrix[pos_row][pos_col] = 'x'
                if matrix[pos_row - 1][pos_col] in 'CDG':
                    collection[matrix[pos_row - 1][pos_col]] += 1
                    count_items += 1
                matrix[pos_row - 1][pos_col] = 'Y'
                if all_items == count_items:
                    is_collected = True
                    break
                pos_row -= 1
            else:
                matrix[pos_row][pos_col] = 'x'
                if matrix[rows-1][pos_col] in 'CDG':
                    collection[matrix[pos_row - 1][pos_col]] += 1
                    count_items += 1
                matrix[rows - 1][pos_col] = 'Y'
                if all_items == count_items:
                    is_collected = True
                    break
                pos_row = rows - 1
            steps -= 1

    elif direction == 'down':
        while steps > 0:
            if pos_row + 1 < rows:
                matrix[pos_row][pos_col] = 'x'
                if matrix[pos_row + 1][pos_col] in 'CDG':
                    collection[matrix[pos_row + 1][pos_col]] += 1
                    count_items += 1
                matrix[pos_row + 1][pos_col] = 'Y'
                if all_items == count_items:
                    is_collected = True
                    break
                pos_row += 1
            else:
                matrix[pos_row][pos_col] = 'x'
                if matrix[0][pos_col] in 'CDG':
                    collection[matrix[0][pos_col]] += 1
                    count_items += 1
                matrix[0][pos_col] = 'Y'
                if all_items == count_items:
                    is_collected = True
                    break
                pos_row = 0
            steps -= 1

    elif direction == 'left':
        while steps > 0:
            if pos_col - 1 >= 0:
                matrix[pos_row][pos_col] = 'x'
                if matrix[pos_row][pos_col - 1] in 'CDG':
                    collection[matrix[pos_row][pos_col - 1]] += 1
                    count_items += 1
                matrix[pos_row][pos_col - 1] = 'Y'
                if all_items == count_items:
                    is_collected = True
                    break
                pos_col -= 1
            else:
                matrix[pos_row][pos_col] = 'x'
                if matrix[pos_row][cols-1] in 'CDG':
                    collection[matrix[pos_row][cols-1]] += 1
                    count_items += 1
                matrix[pos_row][cols-1] = 'Y'
                if all_items == count_items:
                    is_collected = True
                    break
                pos_col = cols - 1
            steps -= 1
    elif direction == 'right':
        while steps > 0:
            if pos_col + 1 < cols:
                matrix[pos_row][pos_col] = 'x'
                if matrix[pos_row][pos_col + 1] in 'CDG':
                    collection[matrix[pos_row][pos_col + 1]] += 1
                    count_items += 1
                matrix[pos_row][pos_col + 1] = 'Y'
                if all_items == count_items:
                    is_collected = True
                    break
                pos_col += 1
            else:
                matrix[pos_row][pos_col] = 'x'
                if matrix[pos_row][0] in 'CDG':
                    collection[matrix[pos_row][0]] += 1
                    count_items += 1
                matrix[pos_row][0] = 'Y'
                if all_items == count_items:
                    is_collected = True
                    break
                pos_col = 0
            steps -= 1
    if is_collected:
        break
    line = input()

if is_collected:
    print(f'Merry Christmas!')
print("You've collected:")
print(f'- {collection["D"]} Christmas decorations')
print(f'- {collection["G"]} Gifts')
print(f'- {collection["C"]} Cookies')
for each in matrix:
    print(f"{' '.join(each)}")

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. Naughty or Nice
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def count_num(santas, num):
    count = 0
    for each in santas:
        if each[0] == num:
            count += 1
    return count

def count_name(santas, name):
    count = 0
    for each in santas:
        if each[1] == name:
            count += 1
    return count

def naughty_or_nice_list(*args, **kwargs):
    kids = dict()
    santas = args[0]
    for each in range(1,len(args)):
        type_kids = args[each].split('-')[1]
        code_kids = int(args[each].split('-')[0])
        if count_num(santas,code_kids) == 1:
            for x in range(len(santas)):
                if santas[x][0] == code_kids:
                    if type_kids not in kids:
                        kids[type_kids] = list()
                    kids[type_kids].append(santas[x][1])
                    santas.pop(x)
                    break

    for key, value in kwargs.items():
        type_kids = value
        name_kids = key
        if count_name(santas,name_kids) == 1:
            for x in range(len(santas)):
                if santas[x][1] == name_kids:
                    if type_kids not in kids:
                        kids[type_kids] = list()
                    kids[type_kids].append(santas[x][1])
                    santas.pop(x)
                    break

    if santas:
        kids['Not found'] = list()
        for each in santas:
            kids['Not found'].append(each[1])

    sorted_kids = [f'{key}: {", ".join(value)}' for key, value in sorted(kids.items(), key = lambda x: len(x[0]))]
    return '\n'.join(sorted_kids)

print(' - - - - - - - - - - - - - - - - - -')
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(' - - - - - - - - - - - - - - - - - -')
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))
print(' - - - - - - - - - - - - - - - - - -')
print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 