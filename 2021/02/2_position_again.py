def handler():
    depth = 0
    horizontal = 0
    aim = 0
    with open('input.txt') as input_file:
        for line in input_file:
            instruction_list = line.split(' ')
            instruction = instruction_list[0]
            value = int(instruction_list[1])
            if instruction == 'forward':
                horizontal += value
                depth += aim * value
            elif instruction == 'down':
                aim += value
            elif instruction == 'up':
                aim -= value
    answer = depth * horizontal
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()