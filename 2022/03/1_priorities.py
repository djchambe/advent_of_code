from time import perf_counter


def evaluate_rucksack(rucksack):
    compartment_split = int(len(rucksack) / 2)
    compartment_0 = rucksack[:compartment_split]
    compartment_1 = rucksack[compartment_split:]
    for character in compartment_0:
        if character in compartment_1:
            return character
    print(f'Could not find commonality between {compartment_0} and {compartment_1}')


def get_priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1


def handler():
    start_time = perf_counter()
    error_item_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            error_item_list.append(evaluate_rucksack(clean_line))

    answer = 0
    for item in error_item_list:
        answer += get_priority(item)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
