from time import perf_counter

def race(reindeer, time):
    max_distance = 0
    for name, stats in reindeer.items():
        cycle = stats['cycle']
        pace = stats['pace']
        run_limit = stats['run_limit']
        distance = (time // cycle) * pace * run_limit + min(time % cycle, run_limit) * pace
        if distance > max_distance:
            max_distance = distance
            best_reindeer = name
    
    return max_distance, best_reindeer

def handler():
    start_time = perf_counter()
    reindeer = {}
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip().rstrip('.')
            list_line = clean_line.split(' ')
            name = list_line[0]
            pace = int(list_line[3])
            run_limit = int(list_line[6])
            rest = int(list_line[-2])
            reindeer[name] = {
                'pace': pace,
                'run_limit': run_limit,
                'cycle': run_limit + rest
            }

    answer = race(reindeer, 2503)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
