def handler():
    fish_list = []
    new_fish = [6, 8]
    with open('input.txt') as input_file:
        for line in input_file:
            clean_list = line.strip().split(',')
    
    for fish in clean_list:
        fish_list.append(int(fish))
    
    for i in range(80):
        for index, value in enumerate(fish_list):
            fish_list[index] = value - 1
        for j in range(fish_list.count(-1)):
            fish_list.remove(-1)
            fish_list.extend(new_fish)

    answer = len(fish_list)
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()