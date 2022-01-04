from time import perf_counter

KNOWN_VALUES = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

def find_correct_sue(sues):
    possible_sues = []
    for number, known in sues.items():
        possible = True
        for attribute, amount in known.items():
            if KNOWN_VALUES[attribute] != amount:
                possible = False
                break
        if possible:
            possible_sues.append(number)
    
    return possible_sues

def handler():
    start_time = perf_counter()
    sues = {}
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip().rstrip('.')
            list_line = clean_line.split(' ')
            number = int(list_line[1].rstrip(':'))
            key_0 = list_line[2].rstrip(':')
            key_1 = list_line[4].rstrip(':')
            key_2 = list_line[6].rstrip(':')
            val_0 = int(list_line[3].rstrip(','))
            val_1 = int(list_line[5].rstrip(','))
            val_2 = int(list_line[-1])
            sues[number] = {
                key_0: val_0,
                key_1: val_1,
                key_2: val_2
            }

    answer = find_correct_sue(sues)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
