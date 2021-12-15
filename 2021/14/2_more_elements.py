from collections import deque
from math import ceil

def get_extreme_elements(polymer_dict):
    element_dict = {}
    max_element = 0
    min_element = False
    for chain in polymer_dict:
        for character in list(chain):
            if element_dict.get(character, 0):
                element_dict[character] += polymer_dict[chain]
            else:
                element_dict[character] = polymer_dict[chain]
    for _, element_count in element_dict.items():
        actual_count = ceil(element_count / 2.0)
        if actual_count > max_element:
            max_element = actual_count
        if not min_element or min_element > actual_count:
            min_element = actual_count
    return max_element, min_element

def apply_insertions(polymer_dict, insertions):
    new_polymer = {}
    for chain in polymer_dict:
        insertion = insertions[chain]
        new_chain_1 = f'{chain[0]}{insertion}'
        new_chain_2 = f'{insertion}{chain[1]}'
        if new_polymer.get(new_chain_1, ''):
            new_polymer[new_chain_1] += polymer_dict[chain]
        else:
            new_polymer[new_chain_1] = polymer_dict[chain]
        if new_polymer.get(new_chain_2, ''):
            new_polymer[new_chain_2] += polymer_dict[chain]
        else:
            new_polymer[new_chain_2] = polymer_dict[chain]
    return new_polymer

def get_polymer_dict(polymer):
    polymer_dict = {}
    chain = deque(maxlen=2)
    for character in polymer:
        chain.append(character)
        if len(chain) == 2:
            chain_string = ''.join(chain)
            if polymer_dict.get(chain_string, 0):
                polymer_dict[chain_string] += 1
            else:
                polymer_dict[chain_string] = 1
    return polymer_dict

def handler():
    polymer = []
    insertions = {}
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            if not clean_line:
                continue            
            elif not polymer:
                polymer = list(clean_line)
            else:
                insertion_list = clean_line.split(' -> ')
                insertions[insertion_list[0]] = insertion_list[1]
    
    polymer_dict = get_polymer_dict(polymer)
    
    for _ in range(40):
        polymer_dict = apply_insertions(polymer_dict, insertions)
    
    max_element, min_element = get_extreme_elements(polymer_dict)

    answer = max_element - min_element
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()