from time import perf_counter


def handler():
    start_time = perf_counter()
    directories = {}
    file_path = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            line_elements = clean_line.split()
            if line_elements[0] == '$':
                if line_elements[1] == 'cd':
                    if line_elements[2] == '..':
                        file_path.pop()
                    else:
                        file_path.append(line_elements[2])
                        directories['|'.join(file_path)] = 0
            elif line_elements[0].isnumeric():
                for i in range(len(file_path)):
                    directories['|'.join(file_path[:i+1])] += int(line_elements[0])
    
    answer = 0
    for directory_size in directories.values():
        if directory_size <= 100000:
            answer += directory_size

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')


if __name__ == '__main__':
    handler()
