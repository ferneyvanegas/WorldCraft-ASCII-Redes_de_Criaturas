import networkx as nx
import modules.util as u

def create_net():
    '''
    Parameters
    ----------
    Return
    ----------
    * G: networkx
        Una red de nodos (criaturas) con sus respectivas relaciones
    * data: list
        Una lista con cada línea del archivo leído
    '''
    file = open('repo/data.txt')
    data = []
    G = nx.Graph()

    for line in file:
        # Se lee línea por línea del archivo de texto
        l = line.strip().split(',')
        # Limpieza de vacíos
        l = u.clear_line(l)
        # Se crea una copia para posteriormente hacer las relaciones
        data.append(l)
        # Los nodos están ubicados en la posicioń 1 de la línea
        G.add_node(l[1])
        
    file.close()

    # Adicion de ejes individuales
    for l in data:
        '''
            l[0] : Tipo de relación
            l[1] : Nodo A (Criatura origen)
            l[i] : Nodo B
        '''
        for i in range(2, len(l), 1):
            G.add_edge(l[1], l[i], relation=l[0])
        
    
    return G, data

def clear_line(line:list):
    '''
    Parameters
    ----------
    * line:list
        Un listado con nombres de criaturas, y también con espacios vacíos
    ----------
    Return
    ----------
    * line: list
        Un listado con nombres de criaturas, sin espacios
    '''
    # Limpiar listado de vacíos (La construcción del archivo dejó vacíos)
    for i in range((len(line)-1), -1, -1): 
        if line[i] == '':
            line.pop(i)
    return line

def search_neighbors(G, node):
    try:
        print(list(nx.all_neighbors(G,node)))
        return True
    except:
        return False

def centrality(G):
    nodes = nx.degree_centrality(G)
    max_key = max(nodes, key=nodes.get)
    print('******************************')
    print('*****Nodos y Centralidad******')
    print('******************************')
    for key in nodes:
        print(f'{key} : {nodes[key]}')
    print('******************************')
    print(f'El nodo más importante de la red es:')
    print(f'{max_key} : {nodes[max_key]}')
    print('******************************')

def path(G, source, target):
    try:
        print(list(nx.all_shortest_paths(G, source, target)))
        return True
    except:
        return False