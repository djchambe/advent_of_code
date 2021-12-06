def handler():
    fish_list = []
    fish_dict = {}
    with open('input.txt') as input_file:
        for line in input_file:
            clean_list = line.strip().split(',')
    
    for fish in clean_list:
        fish_list.append(int(fish))

    for i in range(7):
        fish_dict[i] = fish_list.count(i)
    
    for j in range(256):
        for k in range(9):
            fish_dict[k-1] = fish_dict.get(k, 0)
        print(fish_dict)
        fish_dict[6] += fish_dict.get(-1, 0)
        fish_dict[8] = fish_dict.get(-1, 0)
        del fish_dict[-1]
    
    answer = 0
    for _, value in fish_dict.items():
        answer += value
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()