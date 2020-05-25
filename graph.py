import sys
import math
import random


class Graph:

    def __init__(self):
        self.city_name_list = []
        self.city_coordinates_list = [[0 for i in range(3)] for i in range(37)]
        self.adjacency_matrix = []
        for i in range(len(self.city_coordinates_list) ):
            self.adjacency_matrix.append([0 for i in range(len(self.city_coordinates_list))])

    def countDistance(self, v1, v2):
        return math.sqrt((float(self.city_coordinates_list[self.city_name_list.index(v1)][1])-float(self.city_coordinates_list[self.city_name_list.index(v2)][1]))**2 + (float(self.city_coordinates_list[self.city_name_list.index(v1)][2])-float(self.city_coordinates_list[self.city_name_list.index(v2)][2]))**2)

    def readFile(self):
        i=0
        #fileinput = open(sys.argv[1], "r")
        fileinput = open("/Users/mateusz/PycharmProjects/alhe/ALHE/cost266.txt", 'r')
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

    def getMinimumDistance(self, idx):
        temp = self.adjacency_matrix[idx]
        temp.sort()
        return temp[1]

    def minSpanningTree(self, beginning):
        vertex_list = [[] for names in range(len(self.city_name_list))]
        queue = []
        visited = [False] * (len(self.city_name_list))
        s = beginning
        queue.append(s)
        cost = 0
        visited[self.city_name_list.index(s)] = True
        while queue:
            s = queue.pop(0)
            for i in range(len(self.city_name_list)):
                if self.city_name_list[i] == s:
                    index = self.adjacency_matrix[i].index(self.getMinimumDistance(i))
                    if not visited[index]:
                        cost += self.getMinimumDistance(i)
                        queue.append(self.city_name_list[index])
                        print(self.city_name_list[index], "->")
                        visited[index] = True
        print(cost)

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
