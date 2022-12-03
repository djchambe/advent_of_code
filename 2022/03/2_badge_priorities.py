from time import perf_counter


def evaluate_rucksacks(rucksacks):
    badge_items = []
    for i in range(0, 300, 3):
        for character in rucksacks[i]:
            if character in rucksacks[i+1] and character in rucksacks[i+2]:
                badge_items.append(character)
                break
    
    if len(badge_items) != len(rucksacks) / 3:
        print(f'Not enough badge items')

    return badge_items


def get_priority(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    return ord(item) - ord('a') + 1


def handler():
    start_time = perf_counter()
    rucksack_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            rucksack_list.append(clean_line)

    badge_items = evaluate_rucksacks(rucksack_list)

    answer = 0
    for item in badge_items:
        answer += get_priority(item)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
