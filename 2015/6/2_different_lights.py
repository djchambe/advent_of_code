from time import perf_counter

def follow_instructions(instructions):
    lights = []
    for k in range(1000):
        lights.append([0]*1000)
    for instruction in instructions:
        direction = instruction[0]
        start_x = instruction[1]
        start_y = instruction[2]
        end_x = instruction[3]
        end_y = instruction[4]
        y_diff = 1 if start_y <= end_y else -1
        x_diff = 1 if start_x <= end_x else -1
        for i in range(start_y, end_y + y_diff, y_diff):
            for j in range(start_x, end_x + x_diff, x_diff):
                if direction == 'on':
                    lights[i][j] += 1
                elif direction == 'off':
                    lights[i][j] = max(0, lights[i][j] - 1)
                elif direction == 'toggle':
                    lights[i][j] += 2
                else:
                    print(f'Bad direction {direction}')

    return lights

def handler():
    start_time = perf_counter()
    instructions = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            list_line = clean_line.split(' ')
            if list_line[1][0].isdigit():
                instruction = 0
                range_1 = 1
            else:
                instruction = 1
                range_1 = 2
            range_1_list = [int(x) for x in list_line[range_1].split(',')]
            range_2_list = [int(x) for x in list_line[-1].split(',')]
            instructions.append([list_line[instruction], range_1_list[0], range_1_list[1], range_2_list[0], range_2_list[1]])

    lights = follow_instructions(instructions)
    answer = 0
    for row in lights:
        answer += sum(row)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()