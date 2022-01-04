from time import perf_counter
from itertools import permutations

def get_longest_route(routes, cities):
    longest_route_cost = 0
    for route in permutations(cities):
        route_cost = 0
        for i in range(len(route)-1):
            route_cost += routes[route[i]][route[i+1]]
        if route_cost > longest_route_cost:
            longest_route_cost = route_cost
            longest_route = route
    
    return longest_route_cost, longest_route

def handler():
    start_time = perf_counter()
    routes = {}
    cities = set()
    with open('input.txt') as input_file:
        for line in input_file:
            clean_line = line.strip()
            list_line = clean_line.split(' = ')
            cost = int(list_line[-1])
            route = list_line[0].split(' to ')
            city_0 = route[0]
            city_1 = route[1]
            cities.add(city_0)
            cities.add(city_1)
            if routes.get(city_0, ''):
                routes[city_0][city_1] = cost
            else:
                routes[city_0] = {city_1: cost}
            if routes.get(city_1, ''):
                routes[city_1][city_0] = cost
            else:
                routes[city_1] = {city_0: cost}

    answer = get_longest_route(routes, cities)

    print(f'The answer is {answer}')
    print(f'Finished in {perf_counter() - start_time}')

if __name__ == '__main__':
    handler()
