# WORLD-CRAFT ASCII: REDES DE CRIATURAS
> **Ferney Vanegas Hernández**

> **Misión TIC 2022**

> **Reto 7**

## **Contexto**
El juego de WorldCraft ASCII es la sensanción actual. Para completar su dinamismo, se precisa que las criaturas del juego puedan establecer una relación específica entre ellas.

## PROBLEMA (I)
### **El Problema**
Dada una masiva cantidad de criaturas, establecer  una red de relaciones específicas entre ellas.
### **Objetivos**
* Realizar la construcción de un documento contenedor de la información de criatruas y relaciones entre ellas
* Construir, según el documento, una red de criaturas señalando sus relaciones.
* Sobre la red construida, generar funciones de búsqueda, centralidad y rutas
### **Interesados**
* Los jugadores y aficionados del juego WorldCraft ASCII
### **Restricciones**
* Los datos deben ser tomados de un archivo de texto
* Cada línea del texto debe tener la siguiente información:
    * 'Tipo relación', 'Criatura origen', 'Lista de criaturas de contacto'
* Debe haber al menos 100 líneas 

## DEFINICIÓN (D)
### **Información Suministrada**
* Debe crearse una red en Python
* La información debe ser cargada de un archivo de texto
* Sobre la arquitectura de cada línea del archivo de texto ('Tipo relación', 'Criatura origen', 'Lista de criaturas de contacto'):
    * Solo hay 3 tipos de relaciones: _Amigo_, _Enemigo_ y '_Neutro_'.
    * El nombre de la criatura que es una cadena de caracteres
    * Por último viene una lista separada por comas de otros nombres de criaturas
* Los nodos de la red son los nombres de las criaturas
* Las relaciones deben llevar el tipo de relación (en sus atributos).
* [_NetworkX Reference_](https://networkx.org/documentation/stable/_downloads/networkx_reference.pdf)
### **Información Requerida**
* Conocimiento de manejo de estructuras de datos _Redes_ en lenguaje Python
* Conocimiento de librerías en Python
### **Subproblemas**
* Construir un fichero con la información estructurada y suficiente
* Crear la red al realizar el cargue masivo de la información
* Brindar al usuario la forma de realizar búsquedas y trazar distancias

## ESTRATEGIA (E)
### **Ejemplo**
![Ejemplo](img/Ej.jpg 'Ejemplo 1')
### **Estratégia**
1. Construir un archivo de texto con la información estructurada, según las especificaciones (valerme de herramientas de ofimática para hacerlo más sencillo)
2. Construir un algoritmo que lea la información del archivo y con ella cree una red de criaturas y sus relaciones
3. Construir un método para consultar contactos (dado el nombre de una criatura listar todos los nodos con los que tiene relación)
4. Construir un método para calcular la centralidad (encontrar el nodo mas importante de la red)
5. Construir un método para que, dados dos nombres de dos criaturas, calcule si hay un camino entre ambos (una ruta para llegar desde uno hasta el otro)

## ALGORITMOS (A)
### **Algoritmo create_net**
*Parámetros: Ninguno* 
* Funcion G<-create_net()
    * Leer archivo
    * Dimensionar data
    * /*crear_grafo es una función de externa*/
    * G = Llamar crear_grafo()
    * Para cada i<-0 hasta número_lineas_archivo con Paso 1 Hacer:
        * /*agregar_nodo es una función de externa*/
        * Llamar agregar_nodo(archivo[i])
        * data[i] = archivo[i]
    * FinPara
    * Para cada l<-0 hasta Llamar longitud[data] con paso 1 Hacer:
        * Para cada i<-2 hasta Llamar logitud[l] con paso 1 Hacer:
            * /*agregar_relacion es una función de externa*/
            * G = Llamar agregar_relacion(data[l], data[i], relacion=data[0]) 
        * FinPara
    * FinPara
    * Retornar G
* FinFuncion
***
### **Algoritmo clear_line**
*Parametros: line*
* Funcion
    * Para cada i<-0 hasta Llamar longitud(line) con paso 1 Hacer:
        * /*eliminar_de_linea es una función de externa*/
        * Si line[i] == '' Entonces:
            * Llamar eliminar_de_linea(line[i])
        * FinSi
    * FinPara
* FinFuncion
***
### **Algoritmo search_neighbors**
*Parámetros: G, node*
* Funcion bool <- search_neighbors()
    * /*todas_las_relaciones es una función de externa*/
    * Si Escribir Llamar todas_las_relaciones(G, none)
        * Retorne True
    * Si no
        * Retorne False
    * FinSi
* FinFuncion
***
### **Algoritmo centrality**
*Parámetros: G*
* Funcion centrality()
    * /*obtener_centralidad es una función de externa*/
    * nodes = Llamar obtener_centralidad(G)
    * /*max y obtener_llave son funciones de externas*/
    * max_key = Llamar max(nodes, key=Llamar obtener_llave())
    * Escribir El nodo más importante de la red es max_key
* FinFuncion
***
### **Algoritmo path**
*Parámetros: G, source, target*
* Funcion path
    * /*encontrar_caminos es una función de externa*/
    * Si Escribir Llamar encontrar_caminos(G, source, target)
        * Retorne True
    * Si no
        * Retorne False
    * FinSi
* FinFuncion
***
### **Algoritmo main**
*Parámetros: Ninguno*
* Funcion main()
    * G = Llamar create_net()
    * exit = False
    * Mientras exit == False Haga:
        * Escribir 1. Dibugar Grafo
        * Escribir 2. Ver nodos y relaciones
        * Escribir 3: Consultar
        * Escribir 4: Centralidad
        * Escribir 5: Calcular camino
        * Escribir 6: Salir
        * Leer opt
        * Si opt == 1 Entonces:
            * /*dibujar_grafo es una función de externa*/
            * Llamar dibujar_grafo(G)
        * FinSi
        * Si opt == 2 Entonces:
        * /*escribir_relaciones es una función de externa*/
            * Llamar escribir_relaciones(G)
        * FinSi
        * Si opt == 3 Entonces:
            * Leer node
            * Llamar search_neighbors(G, node)
        * FinSi
        * Si opt == 4 Entonces:
            * Llamar centrality(G)
        * FinSi
        * Si opt == 5 Entonces:
            * Leer origen
            * Leer destino
            * Llamar path(G, origen, destino)
        * FinSi
        * Si opt == 6 Entonces:
            * exit = True
        * FinSi
    * FinMientras
* FinFuncion