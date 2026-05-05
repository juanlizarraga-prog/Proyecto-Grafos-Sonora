Sistema de Rutas del Estado de Sonora
Este proyecto es una aplicación web interactiva que utiliza la Teoría de Grafos para calcular las rutas óptimas entre diversas ciudades del estado de Sonora, México. Permite encontrar el camino más corto en distancia (km) o el más económico en términos de casetas (peajes).

Características
Visualización Interactiva: Mapa de Sonora con nodos (ciudades) y aristas (carreteras) renderizados con Cytoscape.js.

Algoritmo de Dijkstra: Implementado para encontrar rutas mínimas basadas en dos criterios: Distancia y Peaje.

Gestión de Datos: Posibilidad de agregar o eliminar ciudades y conexiones desde la interfaz.

Backend de Alto Rendimiento: Desarrollado con FastAPI.

Requisitos
Para ejecutar este proyecto, necesitas tener instalado Python 3.8 o superior y las siguientes librerías:

Bash

pip install fastapi uvicorn pydantic

Archivos del Proyecto

Para que la aplicación funcione correctamente, asegúrate de mantener los siguientes archivos en la misma carpeta:

main.py: Lógica del servidor y algoritmos de grafos.

index.html: Interfaz de usuario y visualización.

mapa-sonora.jpg: Imagen de fondo para el mapa.

Ejecución

Paso 1: Iniciar el servidor local

Abre una terminal en la carpeta del proyecto y ejecuta:

Bash

uvicorn main:app --reload
Paso 2: Abrir la aplicación
Una vez que el servidor esté corriendo, abre tu navegador y dirígete a:
http://localhost:8000


Nota: Asegúrate de que en el archivo index.html, la variable API esté configurada como vacía: const API = "";.

Desarrollado para la materia de Análisis de Algoritmos - ITSON.
