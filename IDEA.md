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
### **algoritmo main**
*Parámetros: Ninguno*
* Funcion main()
    * /*Las funciones abrir, eliminar_vacios y graficar son propias de las librerías a usar*/
    * file = Llamar abrir(path_archivo)
    * Llamar eliminar_vacios(file)
    * Llamar graficar(file)
* FinFuncion