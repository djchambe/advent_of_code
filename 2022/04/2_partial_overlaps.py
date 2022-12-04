from time import perf_counter


def evaluate_assignments(pair_assignments):
    if pair_assignments[0] > pair_assignments[2]:
        if (pair_assignments[0] > pair_assignments[3]
            and pair_assignments[1] > pair_assignments[3]):
            return 0
        else:
            return 1
    elif pair_assignments[0] == pair_assignments[2]:
        return 1
    else:
        if pair_assignments[1] < pair_assignments[2]:
            return 0
        else:
            return 1


def handler():
    start_time = perf_counter()
    answer = 0
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            temp_list = clean_line.split(',')
            pair_assignments = []
            for item in temp_list:
                pair_assignments.extend(item.split('-'))
            for index, item in enumerate(pair_assignments):
                pair_assignments[index] = int(item)
            answer += evaluate_assignments(pair_assignments)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
