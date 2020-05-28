import sys
import math
import random


class Graph:

    def __init__(self):
        self.city_name_list = []
        self.city_coordinates_list = [[0 for i in range(3)] for i in range(37)]
        self.adjacency_matrix = []
        self.distance_list = []
        for i in range(len(self.city_coordinates_list)):
            self.adjacency_matrix.append([0 for i in range(len(self.city_coordinates_list))])

    def countDistance(self, v1, v2):
        return math.sqrt((float(self.city_coordinates_list[self.city_name_list.index(v1)][1])-float(self.city_coordinates_list[self.city_name_list.index(v2)][1]))**2 + (float(self.city_coordinates_list[self.city_name_list.index(v1)][2])-float(self.city_coordinates_list[self.city_name_list.index(v2)][2]))**2)

    def readFile(self):
        i = 0
        # fileinput = open(sys.argv[1], "r")
        # fileinput = open("/Users/mateusz/PycharmProjects/alhe/ALHE/cost266.txt", 'r')
        fileinput = open("/Users/maciekpaszylka/Desktop/cost266.txt", 'r')

        f1 = fileinput.readlines()
        for line in f1:
            if not line.startswith(")"):
                while line.startswith(" "):
                    words_in_line = line.split(" ")
                    self.city_name_list.append(words_in_line[2])
                    self.city_coordinates_list[i][0] = words_in_line[2]
                    self.city_coordinates_list[i][1] = words_in_line[4]
                    self.city_coordinates_list[i][2] = words_in_line[5]
                    i += 1
                    break
            else:
                break

    def makeAdjacencyMatrix(self):
        for k in range(len(self.city_name_list)):
            for j in range(len(self.city_name_list)):
                self.adjacency_matrix[k][j] = self.countDistance(self.city_name_list[k], self.city_name_list[j])
                self.adjacency_matrix[j][k] = self.countDistance(self.city_name_list[k], self.city_name_list[j])

    def minSpanningTree(self, beginning, notVisited):
        s = beginning
        vertex_list = []
        for i in range(len(notVisited)):
            vertex_list.append(self.city_name_list[notVisited[i]])
        vertex_list.append(s)
        visited = [False for i in range(len(self.city_name_list))]
        for i in range(len(notVisited)):
            visited[notVisited[i]] = True
        cost = 0
        while len(vertex_list) != 37:
            queue = []
            temp = []
            for i in range(len(self.city_name_list)):
                if self.city_name_list[i] != s and self.city_name_list[i] not in vertex_list:
                    queue.append(self.city_name_list[i])
            for j in range(len(queue)):
                temp.append(self.countDistance(queue[j], s))
            idx = queue.index(queue[temp.index(min(temp))])

            if not visited[self.city_name_list.index(queue[idx])]:
                visited[self.city_name_list.index(queue[idx])] = True
                vertex_list.append(queue[idx])
                s = queue[idx]
                cost += min(temp)
        return cost

    def a_star(self, begin_city):

        def calculate_cost(path):

            distance = 0
            if len(path) == 1:
                return 0
            for i in range(len(path) - 1):
                city1 = path[i]
                city2 = path[i + 1]
                distance += self.adjacency_matrix[city1][city2]

            return distance

        def closest_not_visited(n, not_visited_cities):

            distance2 = 10000
            result2 = -1
            for city2 in not_visited_cities:
                y = self.adjacency_matrix[n][city2]

                if y < distance2 and y != 0:
                    distance2 = y
                    result2 = city2
            #print("distance2", distance2)
            return distance2, result2

        path = []

        if begin_city in self.city_name_list:
            beginIndex = self.city_name_list.index(begin_city)
        else:
            print("No such city")
            return

        not_visited = [x for x in range(len(self.city_name_list))]
        not_visited.remove(beginIndex)

        path.append(beginIndex)

        while len(not_visited) > 1:
            shortest = 10000
            next_city = -1
            for city in not_visited:
                score = 0

                score += calculate_cost(path)                       # these 2 are g(n)
                score += self.adjacency_matrix[city][path[-1]]      # distance between last added to path and current city

                distance, result = closest_not_visited(city, not_visited)

                score += distance
                score += self.adjacency_matrix[result][path[0]]

                score += self.minSpanningTree(self.city_name_list[city], not_visited)

                if score < shortest:
                    shortest = score
                    next_city = city
            #print("nextcity", next_city)
            path.append(next_city)
            not_visited.remove(next_city)

        path.append(not_visited[0])
        path.append(path[0])

        print("Path found:")
        for x in path:
            print(self.city_name_list[x])
        print("Score:", calculate_cost(path))



    def bruteForce(self, begin_city='Amsterdam'):

        beginIndex = 0

        if begin_city in self.city_name_list:
            beginIndex = self.city_name_list.index(begin_city)

        cities = [x for x in range(len(self.city_name_list))]
        cities.remove(beginIndex)
        random.shuffle(cities)

        routes = list(map(list, self.permutations(cities)))
        for x in routes:
            x.insert(0, beginIndex)
            x.insert(len(routes), beginIndex)

        def calculate_cost():
            nonlocal routes
            travel_costs = []

            for route in routes:
                distance = 0

                for i in range(len(route) - 1):
                    city1 = route[i]
                    city2 = route[i+1]
                    distance += self.adjacency_matrix[city1][city2]

                travel_costs.append(distance)

            smallest_cost = min(travel_costs)
            shortest = (routes[travel_costs.index(smallest_cost)], smallest_cost)

            print("Best found route is:")
            for x in routes[0]:
                print(self.city_name_list[x])
            print("With cost", shortest[1])

            return shortest

        return calculate_cost()

    #from itertools, generates "routes" number of permutations
    def permutations(self, iterable, r=None, routes=500000):
        # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
        # permutations(range(3)) --> 012 021 102 120 201 210
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return
        indices = list(range(n))
        cycles = list(range(n, n-r, -1))
        yield tuple(pool[i] for i in indices[:r])
        counter = 0
        print("Calculating", routes, "routes...")
        while n:
            counter += 1
            if counter == routes:
                return
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    yield tuple(pool[i] for i in indices[:r])
                    break
            else:
                return
