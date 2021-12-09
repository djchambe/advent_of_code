from copy import copy

def clean_up_digit_list(digit, digit_map):
    if len(digit_map[digit]['letters']) != 1:
        print(f'Fix {digit} algorithm, {digit_map}')
    for entry in digit_map:
        if entry != digit and digit_map[digit]['letters'][0] in digit_map[entry]['letters']:
            digit_map[entry]['letters'].remove(digit_map[digit]['letters'][0])
    return digit_map

def get_digit_letters_reverse(digit, compare, digit_map):
    digit_letters = copy(digit_map[digit]['letters'])
    for letter_group in digit_letters:
        compare_group_list = list(digit_map[compare]['letters'][0])
        for letter in letter_group:
            if letter not in compare_group_list:
                digit_map[digit]['letters'].remove(letter_group)
                break
    digit_map = clean_up_digit_list(digit, digit_map)
    return digit_map

def get_digit_letters(digit, compare, digit_map):
    digit_letters = copy(digit_map[digit]['letters'])
    for letter_group in digit_letters:
        letter_group_list = list(letter_group)
        for letter in digit_map[compare]['letters'][0]:
            if letter not in letter_group_list:
                digit_map[digit]['letters'].remove(letter_group)
                break
    digit_map = clean_up_digit_list(digit, digit_map)
    return digit_map

def get_digit_map(signal_list):
    digit_map = {
        0: {'length': 6, 'letters': [], 'contains': [1, 7]},
        1: {'length': 2, 'letters': [], 'contains': []},
        2: {'length': 5, 'letters': [], 'contains': []},
        3: {'length': 5, 'letters': [], 'contains': [1, 7]},
        4: {'length': 4, 'letters': [], 'contains': [1]},
        5: {'length': 5, 'letters': [], 'contains': []},
        6: {'length': 6, 'letters': [], 'contains': [5]},
        7: {'length': 3, 'letters': [], 'contains': [1]},
        8: {'length': 7, 'letters': [], 'contains': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]},
        9: {'length': 6, 'letters': [], 'contains': [1, 3, 4, 5, 7]}
    }
    for signal in signal_list:
        signal_length = len(signal)
        for digit, info in digit_map.items():
            if info['length'] == signal_length:
                info['letters'].append(signal)
    digit_map = get_digit_letters(9, 4, digit_map)
    digit_map=  get_digit_letters(0, 1, digit_map)
    if len(digit_map[6]['letters']) != 1:
        print(f'Fix 6 algorithm, {digit_map}')
    digit_map = get_digit_letters_reverse(5, 6, digit_map)
    digit_map = get_digit_letters(3, 1, digit_map)
    if len(digit_map[2]['letters']) != 1:
        print(f'Fix 2 algorithm, {digit_map}')
    
    return digit_map

def get_output_number(digit_map, output_list):
    digit_list = []
    for number_string in output_list:
        number_string_list = list(number_string)
        number_string_list.sort()
        for digit, info in digit_map.items():
            digit_string_list = list(info['letters'][0])
            digit_string_list.sort()
            if number_string_list == digit_string_list:
                digit_list.append(digit)
                break
    if len(digit_list) != 4:
        print(f'{digit_list} is not four digits long')
    output_number = 0
    for index, digit in enumerate(digit_list):
        output_number += 10**(3-index)*digit
    return output_number

def handler():
    output_numbers = []
    with open('input.txt') as input_file:
        for line in input_file:
            signal_and_output_list = line.strip().split('|')
            signal_list = signal_and_output_list[0].split(' ')
            digit_map = get_digit_map(signal_list)
            output_list = signal_and_output_list[1].strip().split(' ')
            output_numbers.append(get_output_number(digit_map, output_list))    

    answer = sum(output_numbers)

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()