https://judge.softuni.org/Contests/Practice/Index/2812
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Fireworks Show
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

fireworks = deque()
for x in input().split(', '):
    fireworks.append(int(x))
explosives = [int(x) for x in input().split(', ')]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0

is_all_types = False
while fireworks and explosives:
    firework = fireworks[0]
    explosive = explosives[-1]

    if firework <= 0:
        fireworks.popleft()
        continue
    if explosive <= 0:
        explosives.pop()
        continue

    sum = firework + explosive

    if sum % 3 == 0 and sum % 5 != 0:
        palm_fireworks += 1
        fireworks.popleft()
        explosives.pop()
    elif sum % 3 != 0 and sum % 5 == 0:
        willow_fireworks += 1
        fireworks.popleft()
        explosives.pop()
    elif sum % 3 == 0 and sum % 5 == 0:
        crossette_fireworks += 1
        fireworks.popleft()
        explosives.pop()
    else:
        fireworks.popleft()
        fireworks.append(firework-1)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        is_all_types = True
        break

if is_all_types:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f"Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f'Firework Effects left: {", ".join([str(x) for x in fireworks])}')
if explosives:
    print(f'Explosive Power left: {", ".join([str(x) for x in explosives])}')
print(f'Palm Fireworks: {palm_fireworks}')
print(f'Willow Fireworks: {willow_fireworks}')
print(f'Crossette Fireworks: {crossette_fireworks}')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Collecting Coins
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
import math

def next_pos(row, col, direction, size):
    if direction == 'up':
        if row == 0:
            return size - 1, col
        else:
            return row - 1, col
    if direction == 'down':
        if row == size - 1:
            return 0, col
        else:
            return row + 1, col
    if direction == 'left':
        if col == 0:
            return row, size - 1
        else:
            return row, col - 1
    if direction == 'right':
        if col == size - 1:
            return row, 0
        else:
            return row, col + 1

size = int(input())
field = []
p_row = 0
p_col = 0
total_coins = 0
path = list()
for row in range(size):
    ll = input().split()
    for col in range(len(ll)):
        if ll[col] == 'P':
            p_row = row
            p_col = col
    field.append(ll)
path.append([p_row, p_col])

is_end = False
while True:
    command = input()
    if command == 'up' or command == 'down' or command == 'left' or command == 'right':
        n_row, n_col = next_pos(p_row, p_col, command, size)
        if field[n_row][n_col] != 'X':
            coins = int(field[n_row][n_col])
            total_coins += coins
            field[n_row][ n_col] = 'P'
            field[p_row][p_col] = 0
            p_row = n_row
            p_col = n_col
            path.append([p_row, p_col])
        else:
            total_coins = total_coins / 2
            is_end = True
            path.append([n_row, n_col])
            break
        if total_coins >= 100:
            break

if is_end:
    print(f"Game over! You've collected {math.floor(total_coins)} coins.")
elif total_coins >= 100:
    print(f"You won! You've collected {math.floor(total_coins)} coins.")
print(f'Your path:')
for each in path:
    print(f'{each}')


= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. Cupcake Shop
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def stock_availability(inventory_list, *args):
    inv_list = inventory_list
    command = args[0]
    if command == 'delivery':
        for i in range(1,len(args)):
            inv_list.append(args[i])

    if command == 'sell':
        if len(args) == 1:
            inv_list.pop(0)
        else:
            second = str(args[1])
            if second.isdigit():
                for _ in range(int(second)):
                    if inv_list:
                        inv_list.pop(0)
            else:
                for each in args[1:]:
                    while each in inv_list:
                        inv_list.remove(each)

    return inv_list
        
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
print(' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 