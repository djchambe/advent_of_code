from math import prod

def perform_operation(type_id, values):
    if type_id == '000':
        return sum(values)
    if type_id == '001':
        return prod(values)
    if type_id == '010':
        return min(values)
    if type_id == '011':
        return max(values)
    if type_id == '101':
        compare = values[0] > values[1]
    elif type_id == '110':
        compare = values[0] < values[1]
    elif type_id == '111':
        compare = values[0] == values[1]
    if compare:
        return 1
    else:
        return 0

def evaluate_operator(bin_string, type_id, values):
    length_type = bin_string[0]
    sub_values = []
    if int(length_type):
        sub_packets = int(bin_string[1:12], 2)
        bin_string = bin_string[12:]
        for _ in range(sub_packets):
            bin_string, sub_values = evaluate_packet(bin_string, sub_values)
    else:
        bits = int(bin_string[1:16], 2)
        new_string = bin_string[16:16 + bits]
        while new_string and int(new_string, 2):
            new_string, sub_values = evaluate_packet(new_string, sub_values)
        bin_string = bin_string[16 + bits:]
    values.append(perform_operation(type_id, sub_values))

    return bin_string, values

def evaluate_literal(bin_string, values):
    continuation = 1
    value = ''
    while int(continuation):
        continuation = bin_string[0]
        value += bin_string[1:5]
        bin_string = bin_string[5:]
    values.append(int(value, 2))

    return bin_string, values

def evaluate_packet(bin_string, values):
    if not bin_string or not int(bin_string, 2):
        return bin_string, values
    type_id = bin_string[3:6]
    if type_id == '100':
        bin_string, values = evaluate_literal(bin_string[6:], values)
    else:
        bin_string, values = evaluate_operator(bin_string[6:], type_id, values)

    return bin_string, values

def handler():
    with open('input.txt') as input_file:
        for line in input_file:
            hex_string = line.strip()
    
    bin_string = bin(int(hex_string, 16))[2:].zfill(len(hex_string)*4)

    values = []
    _, values = evaluate_packet(bin_string, values)
    answer = values[0]
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()