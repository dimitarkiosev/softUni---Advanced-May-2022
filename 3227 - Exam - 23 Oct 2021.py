https://judge.softuni.org/Contests/Practice/Index/3227
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
01. Aladdin's Gifts - 75%
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
from collections import deque

def is_gift(mm_sum):
    if 100 <= mm_sum <= 199:
        return 'Gemstone'
    elif 200 <= mm_sum <= 299:
        return 'Porcelain Sculpture'
    elif 300 <= mm_sum <= 399:
        return 'Gold'
    elif 400 <= mm_sum <= 499:
        return 'Diamond Jewellery'

magics = deque()
materials = [int(x) for x in input().split()]
for x in input().split():
    magics.append(int(x))
gifts = dict()
count = 0

while magics and materials:
    count += 1
    material = materials.pop()
    magic = magics.popleft()
    mm_sum = material + magic
    if mm_sum < 100:
        if count % 2 == 0:
            material = 2*material
            magic = 3*magic
            mm_sum = material + magic
        else:
            mm_sum = 2*mm_sum
    elif mm_sum > 499:
        mm_sum = mm_sum / 2

    isGift = is_gift(mm_sum)
    if isGift:
        if isGift not in gifts:
            gifts[isGift] = 0
        gifts[isGift] += 1

if ('Gemstone' in gifts and 'Porcelain Sculpture' in gifts) or ('Gold' in gifts and 'Diamond Jewellery' in gifts):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')

if magics:
    print(f'Magic left: {", ".join([str(x) for x in magics])}')

for key, value in sorted(gifts.items(), key = lambda x: x[0]):
    print(f'{key}: {value}')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Ball in the Bucket
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
size = 6
matrix = list()
my_sum = 0

for row in range(size):
    ll = input().split()
    matrix.append(ll)

for _ in range(3):
    line = input()[1:-1]
    row = int(line.split(', ')[0])
    col = int(line.split(', ')[1])
    if row >= 0 and col >= 0 and row < 6 and col < 6:
        if matrix[row][col] == 'B':
            matrix[row][col] = '0'
            for x in range(6):
                my_sum += int(matrix[x][col])

if my_sum < 100:
    print(f'Sorry! You need {100 - my_sum} points more to win a prize.')
elif my_sum < 200:
    print(f"Good job! You scored {my_sum} points, and you've won Football.")
elif my_sum < 300:
    print(f"Good job! You scored {my_sum} points, and you've won Teddy Bear.")
elif my_sum >= 300:
    print(f"Good job! You scored {my_sum} points, and you've won Lego Construction Set.")

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
03. Shopping List
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
def shopping_list(*args, **kwargs):
    budget = args[0]
    result = list()
    if budget < 100:
        return f'You do not have enough budget.'
    count = 0
    products = kwargs
    for key, value in products.items():
        pr_sum = value[0]*value[1]
        if budget >= pr_sum:
            count += 1
            budget -= pr_sum
            result.append(f'You bought {key} for {pr_sum:.2f} leva.')
        if count == 5:
            break

    return '\n'.join(result)

print('- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -')
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
print('- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -')
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
print('- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -')
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
print('- = - = - = - = - = - = - = - = - = - = - = - = - = - = - = -')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 