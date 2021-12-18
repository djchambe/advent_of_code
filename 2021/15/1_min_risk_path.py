def find_lowest_risks(risk_dict, start):
    unvisited = list(risk_dict.keys())
    while unvisited:
        current = None
        for point in unvisited:
            if current is None:
                current = point
            elif risk_dict[point]['shortest'] < risk_dict[current]['shortest']:
                current = point
        for connection in risk_dict[current]['connections']:
            route_value = risk_dict[current]['shortest'] + risk_dict[connection]['value']
            if route_value < risk_dict[connection]['shortest']:
                risk_dict[connection]['shortest'] = route_value
        unvisited.remove(current)

    return risk_dict

def get_risk_graph(risk_lists):
    risk_dict = {}
    x_len = len(risk_lists[0])
    y_len = len(risk_lists)
    max_risk = 9 * x_len * y_len
    for i in range(y_len):
        for j in range(x_len):
            connections = []
            if i - 1 >= 0:
                connections.append((i - 1, j))
            if i + 1 < y_len:
                connections.append((i + 1, j))
            if j - 1 >= 0:
                connections.append((i, j - 1))
            if j + 1 < x_len:
                connections.append((i, j + 1))
            risk_dict[i, j] = {
                'connections': connections,
                'value': int(risk_lists[i][j]),
                'shortest': max_risk
            }
    risk_dict[0, 0]['shortest'] = 0

    return risk_dict, x_len, y_len

def handler():
    risk_lists = []
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            risk_lists.append(list(clean_line))
    
    risk_dict, x_len, y_len = get_risk_graph(risk_lists)

    risk_dict = find_lowest_risks(risk_dict, (0, 0))

    answer = risk_dict[x_len - 1, y_len -1]['shortest']
    
    print(f'The answer is {answer}')

if __name__ == '__main__':
    handler()