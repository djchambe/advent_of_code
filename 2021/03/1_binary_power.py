def handler():
    count_dict = {}
    with open('input.txt') as input_file:
        for line in input_file:
            for index, digit in enumerate(line.strip()):
                if not isinstance(count_dict.get(index, ""), dict):
                    count_dict[index] = {}
                value = int(digit)
                if not isinstance(count_dict[index].get(value, ""), int):
                    count_dict[index][value] = 1
                else:
                    count_dict[index][value] += 1
    gamma_string = ''
    epsilon_string = ''
    print(f'{count_dict}')
    for index in range(len(count_dict)):
        if count_dict[index].get(0, 0) > count_dict[index].get(1, 0):
            gamma_string += '0'
            epsilon_string += '1'
        else:
            gamma_string += '1'
            epsilon_string += '0'
    gamma = int(gamma_string, 2)
    epsilon = int(epsilon_string, 2)
    answer = gamma * epsilon
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()