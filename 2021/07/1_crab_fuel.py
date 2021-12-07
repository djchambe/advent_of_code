from statistics import median

def handler():
    crab_list = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_list = line.strip().split(',')
    
    for crab in clean_list:
        crab_list.append(int(crab))
    
    converge_point = round(median(crab_list))

    answer = 0
    for crab in crab_list:
        answer += abs(crab-converge_point)

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()