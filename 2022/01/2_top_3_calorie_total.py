from time import perf_counter

def handler():
    start_time = perf_counter()
    calorie_list = []
    current_calories = 0
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            if clean_line:
                current_calories += int(clean_line)
            else:
                calorie_list.append(current_calories)
                current_calories = 0

    answer = 0
    for i in range(3):
        answer += max(calorie_list)
        calorie_list.remove(max(calorie_list))

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
