from time import perf_counter

FORBIDDEN_CHARACTERS = ['i', 'l', 'o']
TRIPLETS = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'pqr', 'qrs', 'rst',
    'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']
NEXT_CHARACTER = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g',
    'g': 'h', 'h': 'j', 'i': 'j', 'j': 'k', 'k': 'm', 'l': 'm', 'm': 'n',
    'n': 'p', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u',
    'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}

def increment_password(password):
    password_list = list(password)
    password_list.reverse()
    new_password = []
    carry = False
    for index, character in enumerate(password_list):
        if index == 0 or carry:
            new_password.append(NEXT_CHARACTER[password_list[index]])
            carry = new_password[-1] == 'a'
        else:
            new_password.append(character)
    new_password.reverse()

    return ''.join(new_password)

def find_valid_password(password):
    while True:
        three_straight = False
        two_pairs = False
        one_pair = ''
        for index, character in enumerate(password):
            if index < len(password) - 2:
                if password[index:index+3] in TRIPLETS:
                    three_straight = True
            if index < len(password) - 1:
                if character == password[index+1]:
                    double = f'{character}{character}'
                    if one_pair and double != one_pair:
                        two_pairs = True
                    else:
                        one_pair = double
        if three_straight and two_pairs:
            return password
        else:
            password = increment_password(password)

def clean_up_password(password):
    new_password = []
    for character in password:
        if character in FORBIDDEN_CHARACTERS:
            new_password.append(NEXT_CHARACTER[character])
        else:
            new_password.append(character)
    
    return ''.join(new_password)

def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            password = line.strip()

    clean_password = clean_up_password(password)
    answer = find_valid_password(clean_password)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
