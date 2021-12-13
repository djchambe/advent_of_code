from copy import copy

def small_dup(path):
    small_caves = [cave for cave in path if cave.islower()]
    return len(small_caves) != len(set(small_caves))

def find_all_paths(start, end, current_path, connections):
    current_path.append(start)
    if start == end:
        return [current_path]
    paths = []
    for vertex in connections[start]:
        if vertex.islower() and vertex in current_path and small_dup(current_path):
            continue
        else:
            paths.extend(find_all_paths(vertex, end, current_path.copy(), connections))
    return paths

def handler():
    connections = {}
    with open('input.txt') as input_file:
        for line in input_file:
            edge = line.strip().split('-')
            for index, vertex in enumerate(edge):
                if (edge[index-1] != 'start' and
                    vertex != 'end'):
                    if connections.get(vertex, ""):
                        connections[vertex].append(edge[index-1])
                    else:
                        connections[vertex] = [edge[index-1]]
    
    all_paths = find_all_paths('start', 'end', [], connections)

    answer = len(all_paths)

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()