from time import perf_counter

def handler():
    start_time = perf_counter()
    code_count = 0
    string_count = 0
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            code_count += len(clean_line)
            new_line = clean_line.replace('\\\\', '%').replace('\\"', '*').replace('"', '')
            hex_count = new_line.count('\\x')
            new_line = new_line.replace('\\x', '')
            string_count += len(new_line) - hex_count

    answer = code_count - string_count

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
