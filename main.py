'''
    Desarrollado por: Ferney Vanegas Hernández
    Misión TIC 2022
    Versión : 1.0.2
    Título: Reto 7
'''

import networkx as nx
import matplotlib.pyplot as plt

import modules.util as u

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
        if int(opt) == 3:
            node = input('Ingresa el nombre de un nodo:\n')
            if not u.search_neighbors(G, node):
                print('El nodo especificado no está en el grafo :(...\n')
        if int(opt) == 4:
            u.centrality(G)
        if int(opt) == 5:
            source = input('Ingresa el nombre del nodo de Origen:\n')
            target = input('Ingresa el nombre del nodo de Destino:\n')
            if not u.path(G, source, target):
                # https://networkx.org/documentation/stable/_downloads/networkx_reference.pdf
                # Pag 578
                print('Error! El nodo de destino no puede ser alcanzado por el nodo de origen \n')
        if int(opt) == 6:
            exit=True
main()