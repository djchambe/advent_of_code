def handler():
    output_list = []
    notable_lengths = [2, 3, 4, 7]
    with open('input.txt') as input_file:
        for line in input_file:
            signal_and_output_list = line.strip().split('|')
            single_output_list = signal_and_output_list[1].split(' ')
            output_list.extend(single_output_list)
    
    length_list = [len(x) for x in output_list]

    answer = 0

    for length in notable_lengths:
        answer += length_list.count(length)

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()