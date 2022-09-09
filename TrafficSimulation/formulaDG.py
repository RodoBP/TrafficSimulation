import numpy as np
import pandas as pd
import networkx as nx

def dijstra(start,end):
    rutas = pd.read_csv("Ejemplo.csv")

    DG = nx.DiGraph()

    for row in rutas.iterrows():
        DG.add_edge(row[1]["Origen"],
                    row[1]["Destino"],
                    Costo=row[1]["Costo"])

    path = list(nx.dijkstra_path(DG, source=start, target=end, weight="Costo"))
    print(path)

    return path