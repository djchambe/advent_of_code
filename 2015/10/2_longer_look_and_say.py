from time import perf_counter

def look_and_say(number):
    new_number_list = []
    index = 0
    current_digit = ''
    current_digit_count = 0
    while index < len(number):
        if number[index] == current_digit:
            current_digit_count += 1
            index += 1
            continue
        if index > 0:
            new_number_list.append(str(current_digit_count))
            new_number_list.append(current_digit)
        current_digit = number[index]
        current_digit_count = 1
        index += 1

    new_number_list.append(str(current_digit_count))
    new_number_list.append(current_digit)
    
    return ''.join(new_number_list)

def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            number = line.strip()

    for _ in range(50):
        number = look_and_say(number)
    
    answer = len(number)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
