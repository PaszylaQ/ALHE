import sys
import math

class Graph:

    def __init__(self):
        self.city_name_list = []
        self.city_coordinates_list = [[0 for i in range(3)] for i in range(37)]
        self.adjacency_matrix = []
        for i in range(len(self.city_coordinates_list) - 1):
            self.adjacency_matrix.append([0 for i in range(len(self.city_coordinates_list)-1)])

    def countDistance(self, v1, v2):
        return math.sqrt((float(self.city_coordinates_list[self.city_name_list.index(v1)][1])-float(self.city_coordinates_list[self.city_name_list.index(v2)][1]))**2 + (float(self.city_coordinates_list[self.city_name_list.index(v1)][2])-float(self.city_coordinates_list[self.city_name_list.index(v2)][2]))**2)

    def readFile(self):
        i=0
        fileinput = open(sys.argv[1], "r")
        #fileinput = open("/Users/maciekpaszylka/Desktop/cost266.txt", 'r')
        f1 = fileinput.readlines()
        for line in f1:
            if not line.startswith(")"):
                while line.startswith(" "):
                    words_in_line = line.split(" ")
                    self.city_name_list.append(words_in_line[2])
                    self.city_coordinates_list[i][0]= words_in_line[2]
                    self.city_coordinates_list[i][1] = words_in_line[4]
                    self.city_coordinates_list[i][2] = words_in_line[5]
                    i+=1
                    break
            else:
                break

    def makeAdjacencyMatrix(self):
        for k in range(len(self.city_name_list)-1):
            for j in range(len(self.city_name_list)-1):
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





