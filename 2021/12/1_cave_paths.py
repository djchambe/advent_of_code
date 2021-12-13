from copy import copy

def find_all_paths(start, end, current_path, paths, connections):
    current_path.append(start)
    if start == end:
        if current_path not in paths:
            paths.append(copy(current_path))
        current_path.pop()
        return paths
    else:
        for vertex in connections[start]:
            if vertex.islower() and vertex in current_path:
                continue
            else:
                paths = find_all_paths(vertex, end, current_path, paths, connections)
    current_path.pop()
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
    
    all_paths = find_all_paths('start', 'end', [], [], connections)

    answer = len(all_paths)

    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()