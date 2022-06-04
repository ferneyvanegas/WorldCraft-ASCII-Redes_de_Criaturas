import networkx as nx
import matplotlib.pyplot as plt

def create_net():
    '''
    Parameters
    ----------
    Return
    ----------
    * G: networkx
        Una red de nodos (criaturas) con sus respectivas relaciones
    '''
    file = open('repo/data.txt') # Podría ser un csv, pero también un txt es opción y el requisito estaba abierto
    data = []
    G = nx.Graph()

    for line in file: # Se lee línea por línea del archivo de texto
        '''
            Nota: Se precisa purificar cada línea, por cuanto el archivo fue formado con herramientas 
            de ofimática que ponían caracteres adicionales, espacios, etc...
        '''
         # =====================================
        # Puficación del la líńea
        # =====================================
        l = line.strip().split(',') # strip: borra espacios al final | split: crea lista con datos separados por coma
        l = clear_line(l) # Limpieza de vacíos
        # =====================================      
        data.append(l) # Se crea una copia para posteriormente hacer las relaciones        
        G.add_node(l[1]) # Se agregan nodos. Los nodos están ubicados en la posicioń 1 de la línea
        
    file.close() # Se cierra el archivo

    # Adicion de ejes (relaciones dirigidas)
    for l in data:
        '''
            l[0] : Tipo de relación
            l[1] : Nodo A (Criatura origen)
            l[i] : Nodo B (Criatura destino)
        '''
        for i in range(2, len(l), 1):
            G.add_edge(l[1], l[i], relation=l[0]) # Se agregan las relaciones a la red

    return G

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
    # Limpiar línea de vacíos (La construcción del archivo dejó vacíos)
    for i in range((len(line)-1), -1, -1): 
        if line[i] == '':
            line.pop(i)
    return line

def search_neighbors(G, node):
    '''
    Parameters
    ----------
    * G: networkx
        Una red de nodos (criaturas) con sus respectivas relaciones
    * node: str
        El nombre de un nodo
    ----------
    Returns
    ----------
    * :bool
        True: Si logró encontrar el nodo y sus nodos relacionados | False: Si no logró encontrar el nodo
    '''
    
    try:
        print('*******************************\n'
            f'Nodos relacionados con {node}\n'
            '*******************************')
        for i in list(nx.all_neighbors(G,node)): # Pág. 707
            # Relación específica | Pag. 24
            # G.get_edge_data(node, i) devuelve un diccionario con la relacion entre los nodos
            if G.get_edge_data(node, i)["relation"] == 'Amigo':
                print(f'\033[92m* {i} - {G.get_edge_data(node, i)["relation"]}')
            if G.get_edge_data(node, i)["relation"] == 'Enemigo':
                print(f'\033[91m* {i} - {G.get_edge_data(node, i)["relation"]}\033[92m')
            if G.get_edge_data(node, i)["relation"] == 'Neutro':
                print(f'\033[0m* {i} - {G.get_edge_data(node, i)["relation"]}\033[92m')
        return True
    except:
        return False

def centrality(G):
    '''
    Parameters
    ----------
    * G: networkx
        Una red de nodos (criaturas) con sus respectivas relaciones
    ----------
    Returns
    ----------
    '''
    nodes = nx.degree_centrality(G) # Pag: 226 | Se obtiene un diccionario con la centralidad de cada nodo

    # Se puede descomentar las líneas del 107 al 115 para ver los resultados obtenidos con degree_centrality
    ''' print('******************************')
    print('*****Nodos y Centralidad******')
    print('******************************')
    for key in nodes:
        print(f'{key} : {nodes[key]}')
    print('******************************')
    print(f'El nodo más importante de la red es:')
    print(f'{max_key} : {nodes[max_key]}')
    print('******************************') '''

    '''
    La funcion max encuentra el mayor de una secuencia. 
    Con .get() obtengo la llave de cada item del diccionario y la paso como parámetro a max
    Fuente: https://www.delftstack.com/es/howto/python/find-max-value-in-dictionary-python/
    '''
    max_key = max(nodes, key=nodes.get) 

    print(f'El nodo más importante de la red es:')
    print('******************************')
    print(f'{max_key}')
    print('******************************') 

def path(G, source, target):
    '''
    Parameters
    ----------
    * G: networkx
        Una red de nodos (criaturas) con sus respectivas relaciones
    * source: str
        El nombre de un nodo origen
    * target: str
        El nombre de un nodo destino
    ----------
    Returns
    ----------
    * :bool
        True: Si logró encontrar rutas entre el origen y el destino | 
        False: Si no se puede alcanzar el destino desde el origen.
    '''
    try:

        # all_shortest_paths entrega todas las rutas entre el origen y el destino
        # print(list(nx.all_shortest_paths(G, source, target))) # Pag: 577
        print('****************************************************************************\n'
            f'Los caminos para llegar de {source} hasta {target} son\n'
            '****************************************************************************')
        for i in list(nx.all_shortest_paths(G, source, target)):
            for j in i:
                print(
                    f'\033[93m-||\033[92m', 
                    f'\033[92m {j} \033[92m', 
                    f'\033[93m||-\033[92m', 
                    end='')
            # Dibujar cada uno de los caminos
            subpath = G.subgraph(i)
            nx.draw(subpath, with_labels=True, node_color='r', edge_color='b')
            plt.show()
 
            print('\n****************************************************************************')
       
        return True
    except:
        return False