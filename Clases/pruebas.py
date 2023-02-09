import json

with open("project.geom", "r") as f:
    datos = json.load(f)


class Lvl:
    def __init__(self, lvl_id, H, cols, beams):
        self.lvl_id = lvl_id
        self.H = H
        self.cols = cols
        self.beams = beams

class Beam:
    def __init__(self, lvl_id, beam_id, node_i, node_f):
        self.lvl_id = lvl_id
        self.beam_id = beam_id
        self.node_i = node_i
        self.node_f = node_f

class Column:
    def __init__(self,lvl_id,column_id,node_b,node_t):
        self.lvl_id = lvl_id
        self.column_id = column_id
        self.node_b = node_b
        self.node_t = node_t

class Node:
    def __init__(self,lvl_id, x_dim, y_dim, z_dim):
        self.lvl_id=lvl_id
        self.x_dim=x_dim
        self.y_dim=y_dim
        self.z_dim=z_dim

pisos = []
for lvl_id in datos["pisos"]:
    h = datos["pisos"][lvl_id]
    col = list(datos["col_piso"][lvl_id].keys())
    beam = list(datos["vig_piso"][lvl_id].keys())
    piso = Lvl(lvl_id, h, col, beam)
    pisos.append(piso)


nodos=[]
for n in pisos:
    for b in n.beams:  # b es una viga perteneciente al piso n
        x_dim
        y_dim
        z_dim

vigas = []
for n in pisos:
    for b in n.beams:  # b es una viga perteneciente al piso n
        nodoi = datos["vigas"][b][0]
        nodod = datos["vigas"][b][1]
        viga = Beam(n.lvl_id, b, nodoi, nodod)
        vigas.append(viga)

columnas=[]
for n in pisos:
    for b in n.cols:
        nodob = datos["columnas"][b][0]
        nodot = datos["columnas"][b][1]
        columna = Column(n.lvl_id, b, nodob, nodot)
        columnas.append(columna)
print(columnas[1].__dict__)


