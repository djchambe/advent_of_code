def handler():
    total = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()

    answer = 0
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()
