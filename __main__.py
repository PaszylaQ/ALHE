from graph import Graph

graf = Graph()
graf.readFile()
graf.makeAdjacencyMatrix()

#print(graf.city_name_list)
#print(graf.adjacency_matrix)

#print(len(graf.adjacency_matrix))
#print(len(graf.adjacency_matrix[0]))

#print(graf.getMinimumDistance(6))

route = graf.bruteForce(begin_city='Warsaw')








#graf.minSpanningTree("Athens")