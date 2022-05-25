= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Reverse Numbers
= = = = = = = = = = = = = = = = = = = = = = = = =
original_string = input().split(' ')

s = []
reversed_string = ''

for c in original_string:
    s.append(c)  # push into the stack

while s:
    value = s[-1]  # peek
    reversed_string += value
    s.pop()  # pop the top

print(reversed_string)

- - - - - - - - - - - - - - - - 
numbers = input().split()

while numbers:
    last_number = numbers.pop()
    print(last_number, end=' ')

= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Stacked Queries
= = = = = = = = = = = = = = = = = = = = = = = = =
stack = list()
number_count = int(input())

for _ in range(number_count):
    command = [int(x) for x in input().split()]
    if command[0] == 1:
        stack.append(command[1])
    elif command[0] == 2 and stack:
        stack.pop()
    elif command[0] == 3 and stack:
        print(max(stack))
    elif command[0] == 4 and stack:
        print(min(stack))

rev_stack = []
while stack:
    rev_stack.append(str(stack.pop()))

print(', '.join(rev_stack))

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Fast Food
= = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

food = deque()
quantity = int(input())
all_food = [int(x) for x in input().split()]
print(f'{max(all_food)}')

for x in all_food:
    food.append(str(x))

while food:
    if int(food[0]) > quantity:
        break
    else:
        rem_food = int(food.popleft())
        quantity -= rem_food

if food:
    print(f"Orders left: {' '.join(food)}")
else:
    print(f'Orders complete')

= = = = = = = = = = = = = = = = = = = = = = = = =
04. Fashion Boutique
= = = = = = = = = = = = = = = = = = = = = = = = =
stack = [int(x) for x in input().split()]
rack_size = int(input())
count = 1
rack = rack_size

while stack:
    peek = stack[-1]
    if rack - peek >= 0:
        rack -= stack.pop()
    else:
        rack = rack_size
        count += 1
        rack -= stack.pop()
print(count)

= = = = = = = = = = = = = = = = = = = = = = = = =
05. Truck Tour
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

pumps = deque()
count = int(input())

for _ in range(count):
    pumps.append([int(x) for x in input().split()])

for attempt in range(count):
    trunk = 0
    failed = False
    for petrol, dist in pumps:
        trunk = trunk + petrol - dist
        if trunk < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break

= = = = = = = = = = = = = = = = = = = = = = = = =
06. Balanced Parentheses
= = = = = = = = = = = = = = = = = = = = = = = = =
all_sym = input()

open_br = list()
pairs = {'(': ')', '[': ']', '{': '}'}
balanced = True

for each in all_sym:
    if each in '({[':
        open_br.append(each)
    elif not open_br:
        balanced = False
    else:
        last_br = open_br.pop()
        if pairs[last_br] != each:
            balanced = False

    if not balanced:
        break

if not balanced or open_br:
    print('NO')
else:
    print('YES')

= = = = = = = = = = = = = = = = = = = = = = = = =
07. Robotics
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

def read_robots():
    temp_robots = input().split(';')
    robots = dict()
    for each in temp_robots:
        name = each.split('-')[0]
        time = int(each.split('-')[1])
        robots[name] = time
    return robots

def to_second(hours, minutes, seconds):
    return hours*60*60 + minutes*60 + seconds

def to_hours(my_seconds):
    h = my_seconds // 3600
    m = (my_seconds % 3600) // 60
    s = (my_seconds % 3600) % 60
    return f'{h:02d}:{m:02d}:{s:02d}'
    
robots = read_robots()
av_robots = [key for key in robots.keys()]
working_robots = dict()
start_time = [int(x) for x in input().split(':')]
start_time_in_s = to_second(start_time[0], start_time[1], start_time[2])
products = deque()

while True:
    line = input()
    if line == 'End':
        break
    products.append(line)

while products:
    start_time_in_s = (start_time_in_s + 1) % (24*60*60)
    for key in [k for k in working_robots.keys()]:
        working_robots[key] -= 1
        if working_robots[key] <= 0:
            working_robots.pop(key)
    current_product = products.popleft()
    for robot in av_robots:
        if robot not in working_robots:
            working_robots[robot] = robots[robot]
            print(f'{robot} - {current_product} [{to_hours(start_time_in_s)}]')
            break
    else:
        products.append(current_product)
= = = = = = = = = = = = = = = = = = = = = = = = =
08. Crossroads
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

green = int(input())
free = int(input())

lane_of_cars = deque()
count = 0
crashed = False
while True:
    line = input()
    if line == 'END':
        break
    elif line == 'green':
        gr_time = green
        while lane_of_cars:
            if gr_time > 0:
                car = lane_of_cars.popleft()
                gr_time -= int(len(car))
                count += 1
            if gr_time < 1:
                if (gr_time + free) < 0:
                    crashed = True
                    print(f'A crash happened!')
                    print(f'{car} was hit at {car[gr_time + free]}.')
                break
    else:
        lane_of_cars.append(line)

    if crashed:
        break
if not crashed:
    print(f'Everyone is safe.')
    print(f'{count} total cars passed the crossroads.')

= = = = = = = = = = = = = = = = = = = = = = = = =
09. Key Revolver
= = = = = = = = = = = = = = = = = = = = = = = = =
from collections import deque

bullets = deque()
locks = list()

bullet_price = int(input())
size_of_gun = int(input())
for x in input().split():
    bullets.append(int(x))
locks = [int(x) for x in input().split()]
money = int(input())
count = 0

while bullets:
    if count % size_of_gun == 0 and count > 0:
        print(f'Reloading!')
    if locks:
        cur_bullet = bullets.pop()
        count += 1
        cur_lock = locks[0]
        if cur_bullet <= cur_lock:
            locks.pop(0)
            print(f'Bang!')
        else:
            print(f'Ping!')
    else:
        break

money_earned = money - (count * bullet_price)

if len(locks) > 0:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f'{len(bullets)} bullets left. Earned ${money_earned}')
= = = = = = = = = = = = = = = = = = = = = = = = =
10. Cups and Bottles
= = = = = = = = = = = = = = = = = = = = = = = = =

