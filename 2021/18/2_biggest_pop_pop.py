import json
from math import ceil
from copy import deepcopy
from datetime import datetime

def get_magnitude(number):
    while isinstance(number, list):
        if all(isinstance(x, int) for x in number):
            indices = []
        else:
            for a in range(len(number)):
                if isinstance(number[a], list):
                    if all(isinstance(x, int) for x in number[a]):
                        indices = [a]
                        break
                    for b in range(len(number[a])):
                        if isinstance(number[a][b], list):
                            if all(isinstance(x, int) for x in number[a][b]):
                                indices = [a,b]
                                break
                            for c in range(len(number[a][b])):
                                if isinstance(number[a][b][c], list):
                                    indices = [a,b,c]
                                    break
        value = get_value(number, indices)
        magnitude = value[0]*3 + value[1]*2
        number = replace_value(number, indices, magnitude)
    return number

def replace_value(number, indices, replacement):
    if not len(indices):
        number = replacement
    elif len(indices) == 1:
        number[indices[0]] = replacement
    elif len(indices) == 2:
        number[indices[0]][indices[1]] = replacement
    elif len(indices) == 3:
        number[indices[0]][indices[1]][indices[2]] = replacement
    elif len(indices) == 4:
        number[indices[0]][indices[1]][indices[2]][indices[3]] = replacement
    elif len(indices) == 5:
        number[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]] = replacement
    elif len(indices) == 6:
        number[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]][indices[5]] = replacement
    else:
        print(f'Error, too many indices {indices}')
    return number

def add_digits(number, indices, addend):
    if len(indices) == 1:
        number[indices[0]] += addend
    elif len(indices) == 2:
        number[indices[0]][indices[1]] += addend
    elif len(indices) == 3:
        number[indices[0]][indices[1]][indices[2]] += addend
    elif len(indices) == 4:
        number[indices[0]][indices[1]][indices[2]][indices[3]] += addend
    elif len(indices) == 5:
        number[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]] += addend
    elif len(indices) == 6:
        number[indices[0]][indices[1]][indices[2]][indices[3]][indices[4]][indices[5]] += addend
    else:
        print(f'Error, too many indices {indices}')
    return number

def get_actual_indices(number, indices):
    actual_indices = []
    sample_number = number
    for index in indices:
        try:
            sample_number = sample_number[index]
        except:
            return actual_indices
        actual_indices.append(index)
    
    return actual_indices

def get_value(number, indices):
    return_number = number
    for index in indices:
        try:
            return_number = return_number[index]
        except:
            return return_number
    return return_number

def get_right_indices(number, indices):
    if sum(indices) == len(indices):
        return None
    right_indices = []
    for index, value in enumerate(indices):
        right_indices.append(value)
        if value == 0:
            shift_index = index
    for index, value in enumerate(right_indices):
        if index == shift_index:
            right_indices[index] = 1
        if index > shift_index:
            right_indices[index] = 0
    while isinstance(get_value(number, right_indices), list):
        right_indices.append(0)
    
    return get_actual_indices(number, right_indices)

def get_left_indices(number, indices):
    if sum(indices) == 0:
        return None
    left_indices = []
    for index, value in enumerate(indices):
        left_indices.append(value)
        if value == 1:
            shift_index = index
    for index, value in enumerate(left_indices):
        if index == shift_index:
            left_indices[index] = 0
        elif index > shift_index:
            left_indices[index] = 1
    while isinstance(get_value(number, left_indices), list):
        left_indices.append(1)

    return get_actual_indices(number, left_indices)

def split(number, indices):
    split_number = get_value(number, indices)
    split_1 = split_number // 2
    split_2 = ceil(split_number/2)
    replacement_value = [split_1, split_2]
    return replace_value(number, indices, replacement_value)
    
def explode(number, indices):
    left_indices = get_left_indices(number, indices)
    right_indices = get_right_indices(number, indices)
    exploder_value = get_value(number, indices)
    if left_indices is not None:
        number = add_digits(number, left_indices, exploder_value[0])
    if right_indices is not None:
        number = add_digits(number, right_indices, exploder_value[1])
    return replace_value(number, indices, 0)

def evaluate_number(number):
    for a in range(len(number)):
        if isinstance(number[a], list):
            for b in range(len(number[a])):
                if isinstance(number[a][b], list):
                    for c in range(len(number[a][b])):
                        if isinstance(number[a][b][c], list):
                            for d in range(len(number[a][b][c])):
                                if isinstance(number[a][b][c][d], list):
                                    return 'explode', [a,b,c,d]
    for a in range(len(number)):
        if isinstance(number[a], int) and number[a] > 9:
            return 'split', [a]
        elif isinstance(number[a], list):
            for b in range(len(number[a])):
                if isinstance(number[a][b], int) and number[a][b] > 9:
                    return 'split', [a,b]
                elif isinstance(number[a][b], list):
                    for c in range(len(number[a][b])):
                        if isinstance(number[a][b][c], int) and number[a][b][c] > 9:
                            return 'split', [a,b,c]
                        elif isinstance(number[a][b][c], list):
                            for d in range(len(number[a][b][c])):
                                if number[a][b][c][d] > 9:
                                    return 'split', [a,b,c,d]
    return '', ''

def perform_reduction(number):
    operation = 'reduce'
    while operation:
        operation, indices = evaluate_number(number)
        if operation == 'explode':
            number = explode(number, indices)
        elif operation == 'split':
            number = split(number, indices)
    return number

def handler():
    print(f'Start: {datetime.now()}')
    number_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            number_list.append(json.loads(clean_line))
    
    answer = 0
    for index, value in enumerate(number_list):
        for index_2, value_2 in enumerate(number_list):
            if index == index_2:
                continue
            reduced = perform_reduction([deepcopy(value), deepcopy(value_2)])
            magnitude = get_magnitude(reduced)
            if magnitude > answer:
                answer = magnitude

    print(f'The answer is {answer}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()
