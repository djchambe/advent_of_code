from datetime import datetime

def add(first, second, registers):
    if second in registers:
        value = registers[second]
    else:
        value = int(second)
    registers[first] += value

    return registers

def mul(first, second, registers):
    if second in registers:
        value = registers[second]
    else:
        value = int(second)
    registers[first] *= value

    return registers

def div(first, second, registers):
    if second in registers:
        value = registers[second]
    else:
        value = int(second)
    registers[first] = registers[first] // value

    return registers

def mod(first, second, registers):
    if second in registers:
        value = registers[second]
    else:
        value = int(second)
    registers[first] = registers[first] % value

    return registers

def eql(first, second, registers):
    if second in registers:
        value = registers[second]
    else:
        value = int(second)
    registers[first] = 1 if registers[first] == value else 0

    return registers

def execute_instructions(instructions, model_number):
    inp_count = 0
    registers = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    for instruction in instructions:
        operation = instruction[0]
        first = instruction[1]
        if operation == 'inp':
            registers['w'] = int(model_number[inp_count])
            inp_count += 1
        else:
            second = instruction[2]
            if operation == 'add':
                registers = add(first, second, registers)
            elif operation == 'mul':
                registers = mul(first, second, registers)
            elif operation == 'div':
                registers = div(first, second, registers)
            elif operation == 'mod':
                registers = mod(first, second, registers)
            elif operation == 'eql':
                registers = eql(first, second, registers)

    return registers['z']

def determine_highest_model_number(scalars_x, scalars_y, dependencies):
    model_number = [0]*14
    for index, value in enumerate(dependencies):
        if value is None:
            if model_number[index] == 0:
                model_number[index] = 9
        else:
            digit = min(9, 9 - scalars_x[value] - scalars_y[index])
            model_number[index] = digit
            if digit == 9:
                model_number[value] = 9 + scalars_x[value] + scalars_y[index]
    
    return ''.join([str(digit) for digit in model_number])

def get_dependencies(scalars_x):
    dependencies = [None]*14
    for index, scalar in enumerate(scalars_x):
        if scalar < 0:
            tracker = 0
            for i in range(index, -1, -1):
                if scalars_x[i] < 0:
                    tracker -= 1
                else:
                    tracker += 1
                if tracker == 0:
                    dependencies[i] = index
                    break
    
    return dependencies

def find_highest_model_number(instructions, scalars_x, scalars_y):
    dependencies = get_dependencies(scalars_x)
    highest_model_number = determine_highest_model_number(scalars_x, scalars_y, dependencies)
    check = execute_instructions(instructions, highest_model_number)
    if check == 0:
        return highest_model_number
    return f"Solver didn't work, gave {highest_model_number} but check is {check}"

def handler():
    print(f'Start: {datetime.now()}')
    instructions = []
    scalars_x = []
    scalars_y = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.rstrip()
            instruction = clean_line.split(' ')
            instructions.append(instruction)
            if instruction[0] == 'add' and instruction[1] == 'x':
                try:
                    scalars_x.append(int(instruction[2]))
                except:
                    pass
            elif instruction[0] == 'add' and instruction[1] == 'y':
                try:
                    scalars_y.append(int(instruction[2]))
                except:
                    pass
    
    important_scalars_y = []
    for index in range(2, len(scalars_y), 3):
        important_scalars_y.append(scalars_y[index])
    
    answer = find_highest_model_number(instructions, scalars_x, important_scalars_y)
    
    print(f'The answer is {answer}')
    print(f'End: {datetime.now()}')

if __name__ == '__main__':
    handler()
