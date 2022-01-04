from time import perf_counter
from json import loads

def get_list_sum(list_input):
    total = 0
    for item in list_input:
        total += get_object_sum(item)
    
    return total

def get_dict_sum(dictionary):
    total = 0
    for key, value in dictionary.items():
        if key == 'red' or value == 'red':
            return 0
        total += get_object_sum(key)
        total += get_object_sum(value)
    
    return total

def get_object_sum(unknown_object):
    if isinstance(unknown_object, dict):
        return get_dict_sum(unknown_object)
    if isinstance(unknown_object, list):
        return get_list_sum(unknown_object)
    if isinstance(unknown_object, str):
        return 0
    if isinstance(unknown_object, int):
        return unknown_object

def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()

    input_object = loads(clean_line)
    answer = get_object_sum(input_object)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
