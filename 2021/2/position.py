def handler():
    depth = 0
    horizontal = 0
    with open('input.txt') as input_file:
        for line in input_file:
            instruction_list = line.split(' ')
            if instruction_list[0] == 'forward':
                horizontal += int(instruction_list[1])
            elif instruction_list[0] == 'down':
                depth += int(instruction_list[1])
            elif instruction_list[0] == 'up':
                depth -= int(instruction_list[1])
    answer = depth * horizontal
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()