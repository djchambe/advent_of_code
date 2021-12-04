from collections import deque

def handler():
    numbers = deque(maxlen=4)
    increases = 0
    with open('input.txt') as input_file:
        for line in input_file:
            numbers.append(int(line))
            if len(numbers) == 4 and numbers[0] < numbers[-1]:
                increases += 1
    print(f'Number of increases is {increases}')

if __name__ == '__main__':
    handler()