from time import perf_counter

def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
    
    floor = 0
    answer = 0

    for character in clean_line:
        answer += 1
        if character == '(':
            floor += 1
        elif character == ')':
            floor -= 1
        if floor == -1:
            break

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()