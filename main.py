'''
    Desarrollado por: Ferney Vanegas Hernández
    Misión TIC 2022
    Versión : 1.0.3
    Título: Reto 7
    *****************************************************
    Observaciones: 
    *****************************************************
        * Se toma como base el documento: NetworkX Reference - Release 2.8.2
        * Fuente: https://networkx.org/documentation/stable/_downloads/networkx_reference.pdf
        * Al referenciar una página en el código (Ej: Pag: 204), hace referencia al documento pdf anteriormente citado
    *****************************************************
    Colores:
    *****************************************************
        OK = '\033[92m' #GREEN
        WARNING = '\033[93m' #YELLOW
        FAIL = '\033[91m' #RED
        RESET = '\033[0m' #RESET COLOR
        Fuente: https://www.delftstack.com/es/howto/python/python-print-colored-text/
'''

# Importaciones externas
import networkx as nx
import matplotlib.pyplot as plt
# Importaciones locales
import modules.util as u

def main():
    G = u.create_net() # Creación de la red
    exit = False # Flag
    while exit == False:
        opt = input('\033[93m*******************************\n'
            'Escoge una opcioń:\n'
            '*******************************\033[0m\n'
            '1. Dibujar Grafo\n'
            '2. Ver nodos y sus relaciones\n'
            '3. Consultar\n'
            '4. Centralidad\n'
            '5. Calcular el camino\n'
            '6. Salir\n'
            '\033[93m*******************************\033[0m\n\033[92m-> '
        )
            
        if int(opt) == 1:
            # Dibujar el grafo (draw_circular = Modo circular)
            nx.draw_circular(G, with_labels=True, node_color='r', edge_color='b')
            plt.show()
        if int(opt) == 2:
            # Presentar los nodos y sus relaciones (el atributo data=True permite ver las relaciones)
            # print(G.edges(data=True)) # Pág: 205
            for i in G.edges(data=True):
                if i[2]['relation'] == 'Amigo':
                    print(f'\033[92m{i[0]} y {i[1]} son {i[2]["relation"] }s')
                if i[2]['relation'] == 'Enemigo':
                    print(f'\033[91m{i[0]} y {i[1]} son {i[2]["relation"] }s\033[92m')
                if i[2]['relation'] == 'Neutro':
                    print(f'\033[0m{i[0]} y {i[1]} son {i[2]["relation"] }s\033[92m')
        if int(opt) == 3:
            node = input('Ingresa el nombre de un nodo:\n')
            if not u.search_neighbors(G, node):
                print('\033[91mError: El nodo especificado no está en el grafo :(...\n')
        if int(opt) == 4:
            u.centrality(G)
        if int(opt) == 5:
            source = input('Ingresa el nombre del nodo de Origen:\n')
            target = input('Ingresa el nombre del nodo de Destino:\n')
            if not u.path(G, source, target):
                print('\033[91mError! El nodo de destino no puede ser alcanzado por el nodo de origen \n') # Pág 578
        if int(opt) == 6:
            exit=True
main()