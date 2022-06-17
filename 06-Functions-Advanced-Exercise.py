01. Negative vs Positive
= = = = = = = = = = = = = = = = = = = = = = = = =
def pos_neg(*args):
    sum_pos = 0
    sum_neg = 0
    for x in args:
        if x > 0:
            sum_pos += x
        else:
            sum_neg += x
    return sum_pos sum_neg


ll = [int(x) for x in input().split()]

pos_sum, neg_sum = pos_neg(ll)
print(pos_sum)
print(neg_sum)

if pos_sum > abs(neg_sum):
    print(f'The positives are stronger than the negatives')
else:
    print(f'The negatives are stronger than the positives')

= = = = = = = = = = = = = = = = = = = = = = = = =
02. Keyword Arguments Length
= = = = = = = = = = = = = = = = = = = = = = = = =
def kwargs_length(**kwargs):
    return len(kwargs)

= = = = = = = = = = = = = = = = = = = = = = = = =
03. Even or Odd
= = = = = = = = = = = = = = = = = = = = = = = = =
def even_odd(*args):
    ll = []
    if args[-1] == 'even':
        for x in args[:-1]:
            if x % 2 == 0:
                ll.append(x)
    if args[-1] == 'odd':
        for x in args[:-1]:
            if x % 2 != 0:
                ll.append(x)
    return ll

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

= = = = = = = = = = = = = = = = = = = = = = = = =
04. Numbers Filter
= = = = = = = = = = = = = = = = = = = = = = = = =
def even_odd_filter(**kwargs):
    result = {}

    for key, value in kwargs.items():
        parity = 0 if key == 'even' else 1
        filtered = [x for x in value if x % 2 == parity]
        result[key] = filtered

    return dict(sorted(result.items(), key = lambda x: len(x[1]), reverse = True))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

= = = = = = = = = = = = = = = = = = = = = = = = =
05. Concatenate
= = = = = = = = = = = = = = = = = = = = = = = = =
def concatenate(*args, **kwargs):
    print(args)
    print(kwargs)

    result = ''

    for v in args:
        result = result + v

    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key, value)

    return result

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))

= = = = = = = = = = = = = = = = = = = = = = = = =
06. Function Executor
= = = = = = = = = = = = = = = = = = = = = = = = =
def func_executor(*args):
    result = []
    for func_r, func_p in args:
        func_result = func_r(*func_p)
        result.append(f'{func_r.__name__} - {func_result}')

    return '\n'.join(result)

def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))

= = = = = = = = = = = = = = = = = = = = = = = = =
07. Grocery
= = = = = = = = = = = = = = = = = = = = = = = = =
def grocery_store(**kwargs):
    result = [f'{key}: {value}' for key, value in sorted(kwargs.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))]
    return '\n'.join(result)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))

= = = = = = = = = = = = = = = = = = = = = = = = =
08. Age Assignment
= = = = = = = = = = = = = = = = = = = = = = = = =
def age_assignment(*args, **kwargs) :
    ages = dict()
    for each in args:
        ages[each] = kwargs[each[0]]
    result = [f'{name} is {age} years old.' for name, age in sorted(ages.items(), key = lambda x: x[0])]
    return '\n'.join(result)

print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

= = = = = = = = = = = = = = = = = = = = = = = = =
09. Recursion Palindrome
= = = = = = = = = = = = = = = = = = = = = = = = =
def palindrome(word, idx):
    for x in range(len(word)):
        if word[x] != word[len(word)-x-1]:
            return False
        if x >= len(word) // 2:
            return True

def palindrome2(word, idx):
    if idx >= len(word) // 2:
        return f'{word} is a palindrome'

    if word[idx] != word[len(word)-idx-1]:
        return f'{word} is not a palindrome'

    return palindrome2(word, idx + 1)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))

print(palindrome2("abcba", 0))
print(palindrome2("peter", 0))

= = = = = = = = = = = = = = = = = = = = = = = = =
10. Fill the Box*
= = = = = = = = = = = = = = = = = = = = = = = = =

= = = = = = = = = = = = = = = = = = = = = = = = =
11. Math Operations*
= = = = = = = = = = = = = = = = = = = = = = = = =
def math_operations(*args, **kwargs):
    dd = kwargs
    for x in range(len(args)):
        if x % 4 == 0:
            dd['a'] += args[x]
        elif x % 4 == 1:
            dd['s'] -= args[x]
        elif x % 4 == 2 and args[x] != 0:
            dd['d'] /= args[x]
        elif x % 4 == 3:
            dd['m'] *= args[x]
    sorted_kw = [f'{key}: {value:.1f}' for key, value in sorted(dd.items(), key = lambda x: (-x[1], x[0]))]
    return '\n'.join(sorted_kw)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))

= = = = = = = = = = = = = = = = = = = = = = = = =
