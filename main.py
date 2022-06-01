import modules.util as u

import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Creación de la red
    G, data = u.create_net()
    exit = False
    while exit==False:
        opt = input('Escoge una opcioń:\n'
            '1. Dibujar Grafo\n'
            '2. Ver nodos y sus relaciones\n'
            '3. Consultar\n'
            '4. Centralidad\n'
            '5. Calcular el camino\n'
            '6. Salir\n'
        )
            
        if int(opt) == 1:
            nx.draw_circular(G, with_labels=True, node_color='r', edge_color='b')
            plt.show()
        if int(opt) == 2:
            print(G.edges(data=True))
        if int(opt) == 6:
            exit=True
main()