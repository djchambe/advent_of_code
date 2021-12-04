def recursion(numbers_list, digit, oxygen):
    count_list = [0, 0]
    for number in numbers_list:
        count_list[int(number[digit])] += 1
    if count_list[0] > count_list[1]:
        if oxygen:
            value = 0
        else:
            value = 1
    else:
        if oxygen:
            value = 1
        else:
            value = 0
    new_list = []
    for number in numbers_list:
        if int(number[digit]) == value:
            new_list.append(number)
    return new_list

def handler():
    all_numbers = []
    with open('input.txt') as input_file:
        for line in input_file:
            all_numbers.append(line.strip())
    oxygen_numbers = all_numbers
    co2_numbers = all_numbers

    oxygen_count = 0
    while len(oxygen_numbers) > 1:
        oxygen_numbers = recursion(oxygen_numbers, oxygen_count, True)
        oxygen_count += 1
    
    co2_count = 0
    while len(co2_numbers) > 1:
        co2_numbers = recursion(co2_numbers, co2_count, False)
        co2_count += 1
    
    oxygen = int(oxygen_numbers[0], 2)
    co2 = int(co2_numbers[0], 2)

    answer = oxygen * co2
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()