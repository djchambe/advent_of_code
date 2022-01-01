from time import perf_counter

def handler():
    start_time = perf_counter()
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
    
    answer = clean_line.count('(') - clean_line.count(')')

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()