from graph import Graph

graf = Graph()
graf.readFile()
graf.makeAdjacencyMatrix()

graf.minSpanningTree("Amsterdam")
#route = graf.bruteForce(begin_city='Warsaw')

