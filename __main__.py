from graph import Graph

graf = Graph()
graf.readFile()
graf.makeAdjacencyMatrix()

route = graf.bruteForce(begin_city='Warsaw')

