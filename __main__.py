from graph import Graph
import sys

if len(sys.argv) == 2:
    file = sys.argv[1]
else:
    file = 'cost266.txt'

graf = Graph(file)
graf.readFile()
graf.makeAdjacencyMatrix()


graf.a_star("Warsaw")
graf.bruteForce("Warsaw", routes=1000000)

