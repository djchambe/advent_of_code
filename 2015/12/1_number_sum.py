from time import perf_counter

def sum_string_numbers(string):
    total = 0
    index = 0
    number_start = None
    while index < len(string):
        if string[index].isdecimal():
            if number_start is None:
                number_start = index
        elif number_start is not None:
            if number_start > 0 and string[number_start-1] == '-':
                total += int(string[number_start-1:index])
            else:
                total += int(string[number_start:index])
            number_start = None
        index += 1

    if number_start is not None:
        if number_start > 0 and string[number_start-1] == '-':
            total += int(string[number_start-1:index])
        else:
            total += int(string[number_start:index])

    return total

def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()

    answer = sum_string_numbers(clean_line)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
