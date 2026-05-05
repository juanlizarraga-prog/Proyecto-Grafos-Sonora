from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import FileResponse  

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#ESTRUCTURAS DE DATOS
class Ciudad(BaseModel):
    nombre: str
    x: float
    y: float

class Colindancia(BaseModel):
    origen: str
    destino: str
    distancia: float
    peaje: float

class GrafoData:
    def __init__(self):
        self.nodos = {} 
        self.aristas = {} 

    def agregar_ciudad(self, nombre, x, y):
        self.nodos[nombre] = {"x": x, "y": y}

    def eliminar_ciudad(self, nombre):
        if nombre in self.nodos:
            del self.nodos[nombre]
            self.aristas = {k: v for k, v in self.aristas.items() if nombre not in k}

    def agregar_arista(self, u, v, d, p):
        clave = tuple(sorted((u, v)))
        self.aristas[clave] = {"distancia": d, "peaje": p}

    def calcular_ruta(self, origen, destino, tipo="distancia"):
        if origen not in self.nodos or destino not in self.nodos: return None
        adj = {n: {} for n in self.nodos}
        for (u, v), datos in self.aristas.items():
            peso = datos[tipo]
            adj[u][v] = peso
            adj[v][u] = peso

        distancias = {n: float('inf') for n in self.nodos}
        distancias[origen] = 0
        padres = {n: None for n in self.nodos}
        no_visitados = list(self.nodos.keys())

        while no_visitados:
            u = min(no_visitados, key=lambda n: distancias[n])
            no_visitados.remove(u)
            if distancias[u] == float('inf') or u == destino: break
            
            for v, peso in adj[u].items():
                if distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso
                    padres[v] = u

        ruta = []
        curr = destino
        while curr:
            ruta.insert(0, curr)
            curr = padres[curr]
        
        return {"ruta": ruta, "total": distancias[destino]}

#CARGA DATOS
grafo = GrafoData()

#nodos
grafo.agregar_ciudad("Hermosillo", 499, 456)
grafo.agregar_ciudad("Guaymas", 503, 476)
grafo.agregar_ciudad("Obregón", 547, 509)
grafo.agregar_ciudad("Pitiquito", 444, 422)
grafo.agregar_ciudad("Caborca", 426, 378)
grafo.agregar_ciudad("Puerto Peñasco", 394, 352)
grafo.agregar_ciudad("Quiriego", 571, 520)
grafo.agregar_ciudad("Yécora", 589, 488)
grafo.agregar_ciudad("Villa Pesqueira", 544, 456)
grafo.agregar_ciudad("Tubutama", 471, 365)
grafo.agregar_ciudad("Cananea", 532, 370)
grafo.agregar_ciudad("Agua Prieta", 580, 366)
grafo.agregar_ciudad("Nogales", 498, 362)
grafo.agregar_ciudad("Magdalena", 502, 388)
grafo.agregar_ciudad("Altar", 450, 361)
grafo.agregar_ciudad("Villa Hidalgo", 571, 404)
grafo.agregar_ciudad("Arizpe", 532, 398)
grafo.agregar_ciudad("Opodepe", 510, 413)
grafo.agregar_ciudad("Aconchi", 531, 424)
grafo.agregar_ciudad("Empalme", 512, 505)
grafo.agregar_ciudad("Etchojoa", 551, 551)
grafo.agregar_ciudad("Huatabampo", 572, 564)
grafo.agregar_ciudad("Álamos", 594, 549)
grafo.agregar_ciudad("Navojoa", 568, 544)
grafo.agregar_ciudad("SLRC", 346, 327)

#aristas
grafo.agregar_arista("Hermosillo", "Guaymas", 138, 103)
grafo.agregar_arista("Hermosillo", "Pitiquito", 267, 253)
grafo.agregar_arista("Hermosillo", "Villa Pesqueira", 110, 0)
grafo.agregar_arista("Guaymas", "Empalme", 15, 0)
grafo.agregar_arista("Guaymas", "Obregón", 128, 103)
grafo.agregar_arista("Empalme", "Obregón", 115, 103)
grafo.agregar_arista("Empalme", "Hermosillo", 145, 103)
grafo.agregar_arista("Obregón", "Navojoa", 68, 103)
grafo.agregar_arista("Obregón", "Quiriego", 90, 0)
grafo.agregar_arista("Navojoa", "Álamos", 52, 0)
grafo.agregar_arista("Navojoa", "Etchojoa", 20, 0)
grafo.agregar_arista("Etchojoa", "Huatabampo", 15, 0)
grafo.agregar_arista("Etchojoa", "Obregón", 80, 103)
grafo.agregar_arista("Huatabampo", "Navojoa", 32, 0)
grafo.agregar_arista("Huatabampo", "Álamos", 82, 0)
grafo.agregar_arista("Álamos", "Quiriego", 110, 0)
grafo.agregar_arista("Quiriego", "Yécora", 180, 0)
grafo.agregar_arista("Yécora", "Hermosillo", 280, 0)
grafo.agregar_arista("Yécora", "Villa Pesqueira", 230, 0)
grafo.agregar_arista("Villa Pesqueira", "Aconchi", 115, 0)
grafo.agregar_arista("Aconchi", "Arizpe", 60, 0)
grafo.agregar_arista("Aconchi", "Opodepe", 80, 0)
grafo.agregar_arista("Opodepe", "Hermosillo", 140, 0)
grafo.agregar_arista("Opodepe", "Magdalena", 100, 0)
grafo.agregar_arista("Magdalena", "Hermosillo", 190, 103)
grafo.agregar_arista("Magdalena", "Nogales", 88, 103)
grafo.agregar_arista("Magdalena", "Altar", 80, 0)
grafo.agregar_arista("Nogales", "Cananea", 86, 0)
grafo.agregar_arista("Nogales", "Agua Prieta", 160, 0)
grafo.agregar_arista("Cananea", "Agua Prieta", 83, 0)
grafo.agregar_arista("Cananea", "Arizpe", 110, 0)
grafo.agregar_arista("Agua Prieta", "Villa Hidalgo", 200, 0)
grafo.agregar_arista("Villa Hidalgo", "Arizpe", 150, 0)
grafo.agregar_arista("Villa Hidalgo", "Cananea", 220, 0)
grafo.agregar_arista("Altar", "Tubutama", 40, 0)
grafo.agregar_arista("Altar", "Pitiquito", 25, 0)
grafo.agregar_arista("Tubutama", "Magdalena", 70, 0)
grafo.agregar_arista("Tubutama", "Pitiquito", 50, 0)
grafo.agregar_arista("Pitiquito", "Caborca", 15, 0)
grafo.agregar_arista("Pitiquito", "Puerto Peñasco", 180, 0)
grafo.agregar_arista("Caborca", "Puerto Peñasco", 175, 0)
grafo.agregar_arista("Caborca", "Altar", 35, 0)
grafo.agregar_arista("Puerto Peñasco", "Magdalena", 250, 0)
grafo.agregar_arista("Puerto Peñasco", "SLRC", 251, 119)


#ENDPOINTS WEB

#Enviar el HTML
@app.get("/")
def mostrar_pagina():
    return FileResponse("index.html")

#Enviar la imagen de fondo (Verifica que el nombre coincida con tu archivo)
@app.get("/mapa-sonora.jpg")
def enviar_imagen():
    return FileResponse("mapa-sonora.jpg")

#Enviar los datos del grafo
@app.get("/data")
def get_data():
    nodes = [{"data": {"id": n}, "position": {"x": d["x"], "y": d["y"]}} for n, d in grafo.nodos.items()]
    edges = [{"data": {"id": f"{u}-{v}", "source": u, "target": v, "dist": d["distancia"], "peaje": d["peaje"]}} 
             for (u,v), d in grafo.aristas.items()]
    return {"nodes": nodes, "edges": edges}

#ENDPOINTS DE MODIFICACIÓN
@app.post("/ciudad")
def add_ciudad(c: Ciudad):
    grafo.agregar_ciudad(c.nombre, c.x, c.y)
    return {"status": "ok"}

@app.post("/arista")
def add_arista(a: Colindancia):
    grafo.agregar_arista(a.origen, a.destino, a.distancia, a.peaje)
    return {"status": "ok"}

@app.delete("/ciudad/{nombre}")
def del_ciudad(nombre: str):
    grafo.eliminar_ciudad(nombre)
    return {"status": "ok"}

@app.get("/ruta")
def get_ruta(origen: str, destino: str, criterio: str):
    return grafo.calcular_ruta(origen, destino, criterio)