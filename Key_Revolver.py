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
