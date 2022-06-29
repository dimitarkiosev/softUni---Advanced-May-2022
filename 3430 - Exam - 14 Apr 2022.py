https://judge.softuni.org/Contests/Practice/Index/3430
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Ramen Shop
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

customer = deque()
ramen = [int(x) for x in input().split(', ')]
for x in input().split(', '):
    customer.append(int(x))

while customer and ramen:
    cur_customer = customer[0]
    cur_ramen = ramen[-1]
    if cur_customer == cur_ramen:
        customer.popleft()
        ramen.pop()
    elif cur_customer >= cur_ramen:
        ramen.pop()
        customer[0] -= cur_ramen
    elif cur_customer <= cur_ramen:
        customer.popleft()
        ramen[-1] -= cur_customer

if not customer:
    print(f'Great job! You served all the customers.')
elif not ramen:
    print(f"Out of ramen! You didn't manage to serve all customers.")

if ramen:
    print(f"Bowls of ramen left: {', '.join(map(str, ramen))}")
if customer:
    print(f"Customers left: {', '.join(map(str, customer))}")

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Martian Explorer
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def next_pos(row, col, direction):
    if direction == 'up':
        if row == 0:
            return 5, col
        else:
            return row - 1, col
    if direction == 'down':
        if row == 5:
            return 0, col
        else:
            return row + 1, col
    if direction == 'left':
        if col == 0:
            return row, 5
        else:
            return row, col - 1
    if direction == 'right':
        if col == 5:
            return row, 0
        else:
            return row, col + 1

size = 6
mars = []
m_row = 0
m_col = 0
deposits = {'W': 0, 'M': 0, 'C': 0}

for row in range(size):
    ll = input().split()
    for col in range(len(ll)):
        if ll[col] == 'E':
            m_row = row
            m_col = col
    mars.append(ll)

all_commands = input().split(', ')

for command in all_commands:
    m_row, m_col = next_pos(m_row, m_col, command)
    new_position = mars[m_row][m_col]
    if new_position == 'W':
        print(f'Water deposit found at ({m_row}, {m_col})')
        deposits['W'] += 1
    if new_position == 'M':
        print(f'Metal deposit found at ({m_row}, {m_col})')
        deposits['M'] += 1
    if new_position == 'C':
        print(f'Concrete deposit found at ({m_row}, {m_col})')
        deposits['C'] += 1
    if new_position == 'R':
        print(f'Rover got broken at ({m_row}, {m_col})')
        break
    mars[m_row][m_col] = '-'

if deposits['W'] > 0 and deposits['M'] > 0 and deposits['C'] > 0:
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')


= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. Words Sorting
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def words_sorting(*args):
    word_dict = dict()
    for x in args:
        ch_sum = 0
        if x not in word_dict:
            word_dict[x] = 0
        for ch in x:
            ch_sum += ord(ch)
        word_dict[x] = ch_sum
    value_sum = 0
    for key, value in word_dict.items():
        value_sum += value
    if value_sum % 2 == 0:
        result = [f'{key} - {value}' for key, value in sorted(word_dict.items(), key = lambda x: x[0])]
    else:
        result = [f'{key} - {value}' for key, value in sorted(word_dict.items(), key = lambda x: -x[1])]
    return '\n'.join(result)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
