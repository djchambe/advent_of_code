from time import perf_counter
from copy import deepcopy

MAX_VALUE = 65535

def get_wire_value(wires, wire):
    if isinstance(wire, int):
        return wire
    if isinstance(wires[wire], int):
        return wires[wire]
    instructions = wires[wire]
    if len(instructions) == 1:
        wires[wire] = get_wire_value(wires, instructions[0])
    elif len(instructions) == 2:
        wires[wire] = get_wire_value(wires, instructions[-1]) ^ MAX_VALUE
    elif 'LSHIFT' in instructions:
        wires[wire] = get_wire_value(wires, instructions[0]) << get_wire_value(wires, instructions[-1])
    elif 'RSHIFT' in instructions:
        wires[wire] = get_wire_value(wires, instructions[0]) >> get_wire_value(wires, instructions[-1])
    elif 'AND' in instructions:
        wires[wire] = get_wire_value(wires, instructions[0]) & get_wire_value(wires, instructions[-1])
    elif 'OR' in instructions:
        wires[wire] = get_wire_value(wires, instructions[0]) | get_wire_value(wires, instructions[-1])

    return wires[wire]

def handler():
    start_time = perf_counter()
    wires = {}
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            list_line = clean_line.split(' -> ')
            wires[list_line[-1]] = [
                int(x) if x.isdigit() else x for x in list_line[0].split(' ')]

    wires_copy = deepcopy(wires)
    wires_copy['b'] = get_wire_value(wires, 'a')
    answer = get_wire_value(wires_copy, 'a')

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
