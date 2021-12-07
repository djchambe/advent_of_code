from statistics import median

def evaluate_fuel_needs(number_list, position):
    fuel_count = 0
    for number in number_list:
        steps = abs(position - number)
        fuel_count += round((steps**2 + steps)/2)
    return fuel_count

def handler():
    crab_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_list = line.strip().split(',')
    
    for crab in clean_list:
        crab_list.append(int(crab))

    min_crab = min(crab_list)
    max_crab = max(crab_list)

    for i in range(min_crab, max_crab + 1):
        fuel = evaluate_fuel_needs(crab_list, i)
        try:
            if min_fuel > fuel:
                min_fuel = fuel
        except:
            min_fuel = fuel

    answer = min_fuel

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()