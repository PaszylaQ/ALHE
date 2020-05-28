from graph import Graph

graf = Graph()
graf.readFile()
graf.makeAdjacencyMatrix()

#graf.minSpanningTree("Oslo")

graf.a_star("Krakow")
# graf.bruteForce("Krakow")
# route = graf.bruteForce(begin_city='Warsaw')
