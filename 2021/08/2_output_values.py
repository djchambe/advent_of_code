def get_digit_map(signal_list):
    digit_map = {
        0: {'length': 6, 'letters': []},
        1: {'length': 2, 'letters': []},
        2: {'length': 5, 'letters': []},
        3: {'length': 5, 'letters': []},
        4: {'length': 4, 'letters': []},
        5: {'length': 5, 'letters': []},
        6: {'length': 6, 'letters': []},
        7: {'length': 3, 'letters': []},
        8: {'length': 7, 'letters': []},
        9: {'length': 6, 'letters': []}
    }
    for signal in signal_list:
        signal_length = len(signal)
        for digit in digit_map:
            if digit['length'] == signal_length:
                digit['letters'].append(signal)
    

def handler():
    output_numbers = []
    with open('input.txt') as input_file:
        for line in input_file:
            signal_and_output_list = line.strip().split('|')
            signal_list = signal_and_output_list[0].split(' ')
            digit_map = get_digit_map(signal_list)
            output_list = signal_and_output_list[1].split(' ')
            output_numbers.append(get_output_number(digit_map, output_list))    

    answer = sum(output_numbers)

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()