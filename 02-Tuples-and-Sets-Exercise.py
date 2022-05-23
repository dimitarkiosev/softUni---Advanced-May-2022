= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# TUPLEs
линейна структура от данни, които са непроменяеми (immutable)
не може да се ползва:
    .append()
    .insert()
    .pop()

tt = (1, 2, 3)
tt = tuple(3)
tt = (1, ) # single element tuple

methods
- count    tt.count(x) - return number of x
- index    tt.index(x) - return index of first x
           tt.index(x,1) - намери х от индекс 1 надясно

opetation
- in       print(1 in tt)
loops       for x in tt:
                print(x)
                
list comprehesions
[print(x) for x in tt]

other objects
print(f'{", ".join(map(str,tt))}'
print(f'{len(tt)}')

tuple concatenation
tt + (9,10)  # (1, 2, 3, 9, 10)

Tuple Unpacking
x, y, z = tt

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# SETs
- search, add, remove is VERY FAST
- contain only UNIQUE values
- UNORDERed

ss = {1, 2, 3, 4, 5}
ss = set() # set не може да се прави така ss = {}, това е dict

ss.add()
ss.remove()
len(ss)
in


= = = = = = = = = = = = = = = = = = = = = = = = = 
01. Unique Usernames
= = = = = = = = = = = = = = = = = = = = = = = = =
n = int(input())
names = set()

for _ in range(n):
    name = input()
    names.add(name)

[print(name) for name in names]

    
= = = = = = = = = = = = = = = = = = = = = = = = = 
02. Sets of Elements
= = = = = = = = = = = = = = = = = = = = = = = = =
n, m = input().split()

set1 = set()
set2 = set()

for _ in range(int(n)):
    set1.add(int(input()))
for _ in range(int(m)):
    set2.add(int(input()))

set3 = set1.intersection(set2)
[print(x) for x in set3]

= = = = = = = = = = = = = = = = = = = = = = = = = 
03. Periodic Table
= = = = = = = = = = = = = = = = = = = = = = = = =
n = int(input())
elements = set()

for _ in range(n):
    line = input().split()
    for each in line:
        elements.add(each)
        
[print(element) for element in elements]

= = = = = = = = = = = = = = = = = = = = = = = = = 
04. Count Symbols
= = = = = = = = = = = = = = = = = = = = = = = = =
my_text = input()

dd = dict()
ss = set()

for x in my_text:
    if x not in dd.keys():
        dd[x] = 0
    dd[x] += 1
    ss.add(x)

for x in sorted(ss):
    print(f'{x}: {dd[x]} time/s')

= = = = = = = = = = = = = = = = = = = = = = = = = 
05. Longest Intersection
= = = = = = = = = = = = = = = = = = = = = = = = = 
n = int(input())

set1 = set()
set2 = set()
big_size = 0
big_set = []

for _ in range(n):
    set1.clear()
    set2.clear()
    l1, l2 = input().split('-')
    l1a, l1b = l1.split(',')
    for x in range(int(l1a), int(l1b)+1):
        set1.add(x)
    l2a, l2b = l2.split(',')
    for x in range(int(l2a), int(l2b)+1):
        set2.add(x)

    set3 = set1.intersection(set2)
    if big_size <= len(set3):
        big_size = len(set3)
        big_set = list(set3)

print(f'Longest intersection is {big_set} with length {big_size}')
    
= = = = = = = = = = = = = = = = = = = = = = = = = 
06. Battle of Names
= = = = = = = = = = = = = = = = = = = = = = = = = 
n = int(input())
odd = set()
even = set()

for x in range(1,n+1):
    name = input()
    value_name = 0
    for ch in name:
        value_name += ord(ch)
    value_name = int(value_name / x)
    if value_name % 2 == 0:
        even.add(value_name)
    else:
        odd.add(value_name)

if sum(even) == sum(odd):
    set3 = even.union(odd)
elif sum(odd) > sum(even):
    set3 = odd.difference(even)
elif sum(even) > sum(odd):
    set3 = even.symmetric_difference(odd)
    
list_set3 = [str(element) for element in set3]

print(', '.join(list_set3))

= = = = = = = = = = = = = = = = = = = = = = = = = 