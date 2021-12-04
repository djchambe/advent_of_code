def handler():
    increases = 0
    count = 0
    previous = 0
    with open('input.txt') as input_file:
        for line in input_file:
            current = int(line)
            if count and current > previous:
                increases += 1
            count += 1
            previous = current
    print(f'Number of increases is {increases}')

if __name__ == '__main__':
    handler()