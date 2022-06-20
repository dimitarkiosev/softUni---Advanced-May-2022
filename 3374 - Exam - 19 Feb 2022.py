https://judge.softuni.org/Contests/Practice/Index/3374#0

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Flowers Finder
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

words = ['rose', 'tulip', 'lotus', 'daffodil']

vowels = deque()
for x in input().split():
    vowels.append(x)
consonants = input().split()

is_find = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for i in range(len(words)):
        for ch in words[i]:
            if vowel == ch:
                words[i] = words[i].replace(ch, "")
                if words[i] == "":
                    is_find = True
                    break
            if consonant == ch:
                words[i]= words[i].replace(ch, "")
                if words[i] == "":
                    is_find = True
                    break
    if is_find:
        break

if not is_find:
    print(f'Cannot find any word!')
else:
    if words[0] == "":
        print(f'Word found: rose')
    elif words[1] == "":
        print(f'Word found: tulip')
    elif words[2] == "":
        print(f'Word found: lotus')
    elif words[3] == "":
        print(f'Word found: daffodil')

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')
if consonants:
    print(f'Consonants left: {" ".join(consonants)}')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Pawn Wars
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
size = 8
chessboard = []
rows_list = ['8', '7', '6', '5', '4', '3', '2', '1']
cols_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b_row = 0
b_col = 0
w_row = 0
w_col = 0

for row in range(size):
    ll = input().split()
    for col in range(len(ll)):
        if ll[col] == 'w':
            w_row = row
            w_col = col
        if ll[col] == 'b':
            b_row = row
            b_col = col
    chessboard.append(ll)

is_end = False
end_row = 0
end_col = 0
white_player = 1
black_player = 0

while True:
    if white_player:
        if b_row == w_row - 1 and (b_col == w_col + 1 or b_col == w_col - 1):
            chessboard[w_row][w_col] = '-'
            chessboard[b_row][b_col] = 'w'
            w_row, w_col = b_row, b_col
            end_row, end_col = w_row, w_col
            is_end = True
        else:
            chessboard[w_row][w_col] = '-'
            w_row -= 1
            chessboard[w_row][w_col] = 'w'
            if w_row == 0:
                end_row, end_col = w_row, w_col
                is_end = True
    elif black_player:
        if w_row == b_row + 1 and (w_col == b_col + 1 or w_col == b_col - 1):
            chessboard[b_row][b_col] = '-'
            chessboard[w_row][w_col] = 'b'
            b_row, b_col = w_row, w_col
            end_row, end_col = b_row, b_col
            is_end = True
        else:
            chessboard[b_row][b_col] = '-'
            b_row += 1
            chessboard[b_row][b_col] = 'b'
            if b_row == 7:
                end_row, end_col = b_row, b_col
                is_end = True
    if is_end:
        break
    if white_player:
        white_player = 0
        black_player = 1
    else:
        white_player = 1
        black_player = 0

if white_player:
    player = 'White'
else:
    player = 'Black'

if b_row == 7 or w_row == 0:
    print(f'Game over! {player} pawn is promoted to a queen at {cols_list[end_col]}{rows_list[end_row]}.')
else:
    print(f'Game over! {player} win, capture on {cols_list[end_col]}{rows_list[end_row]}.')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. Springtime 
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def start_spring(**kwargs):
    all_elements = dict()
    result = list()
    for key, value in kwargs.items():
        if value not in all_elements:
            all_elements[value] = list()
        all_elements[value].append(key)

    sorted_elements = sorted(all_elements.items(), key = lambda x: (-len(x[1]), x[0]))
    for key, value in sorted_elements:
        result.append(f'{key}:')
        sorted_value = [f'-{each}' for each in sorted(value)]
        for each in sorted_value:
            result.append(each)
    return '\n'.join(result)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 