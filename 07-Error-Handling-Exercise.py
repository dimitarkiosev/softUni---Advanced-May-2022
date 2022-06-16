01. Numbers Dictionary
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f'The variable number must be an integer')
    line = input()

line = input()
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])
    except KeyError:
        print(f'Number does not exist in dictionary')
    line = input()

line = input()
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched]
    except KeyError:
        print(f'Number does not exist in dictionary')
    line = input()

print(numbers_dictionary)

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
02. Email Validator
= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

valid_domain = ['.com', '.bg', '.org', '.net']

while True:
    my_email = input()
    if my_email == 'End':
        break

    domain = '.' + my_email.split('.')[-1]
    if len(my_email.split('@')) != 2:
        raise MustContainAtSymbolError('Email must contain @')
    elif len(my_email.split('@')[0]) < 5:
        raise NameTooShortError('Name must be more than 4 characters')
    elif domain not in valid_domain:
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domain)}')
    else:
        print(f'Email is valid')

= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
