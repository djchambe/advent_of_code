def handler():
    with open('input.txt') as input_file:
        for line in input_file:
            instructions = line.strip()
    
    y_strings = instructions.split(' ')[-1].strip('y=').split('..')
    y_range = [int(j) for j in y_strings]

    min_y = min(y_range)
    answer = 0
    for i in range(abs(min_y)):
        answer += i
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()