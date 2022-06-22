https://judge.softuni.org/Contests/Practice/Index/2828
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Pizza Orders
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

pizzas = deque()
for x in input().split(', '):
    pizzas.append(int(x))
employees = [int(x) for x in input().split(', ')]
pizza_sum = 0
while pizzas and employees:
    if pizzas[0] > 10 or pizzas[0] <= 0:
        pizzas.popleft()
        continue

    pizza = pizzas[0]
    employee = employees[-1]

    if pizza <= employee:
        pizza_sum += pizza
        pizzas.popleft()
        employees.pop()
    if pizza > employee:
        pizza_sum += employee
        pizzas[0] -= employee
        employees.pop()

if employees:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizza_sum}')
    print(f'Employees: {", ".join([str(x) for x in employees])}')
if pizzas:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in pizzas])}')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Darts
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
size = 7
darts = []
players = dict()

all_players = input().split(', ')
for each in all_players:
    players[each] = [501, 0]

for _ in range(size):
    ll = input().split()
    darts.append(ll)

is_win = False
cur_player, oth_player = all_players

while True:
    line = input()[1:-1]
    row = int(line.split(", ")[0])
    col = int(line.split(", ")[1])
    if row < 0 or row > 6 or col < 0 or col > 6:
        pass
    else:
        target = darts[row][col]
        if target.isdigit():
            players[cur_player][0] -= int(target)
        elif target == 'D':
            sum_points = 2 * (int(darts[row][0]) + int(darts[row][6]) + int(darts[0][col]) + int(darts[6][col]))
            players[cur_player][0] -= sum_points
        elif target == 'T':
            sum_points = 3 * (int(darts[row][0]) + int(darts[row][6]) + int(darts[0][col]) + int(darts[6][col]))
            players[cur_player][0] -= sum_points
        elif target == 'B':
            is_win = True

    players[cur_player][1] += 1
    if is_win or players[cur_player][0] <= 0:
        break
    cur_player, oth_player = oth_player, cur_player

print(f'{cur_player} won the game with {players[cur_player][1]} throws!')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. Flights 
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def flights (*args):
    all_flights = dict()
    count = 0
    for each in args:
        count += 1
        if each == 'Finish':
            break
        else:
            if count % 2 != 0:
                key = each
                if each not in all_flights:
                    all_flights[each] = 0
            else:
                all_flights[key] += int(each)

    return all_flights

print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 