import json
with open("project.geom", "r") as f:
    datos=json.load(f)

class Lvl:
    def __init__(self, id,H,cols,beams):
        self.id=id
        self.H=H
        self.cols=cols
        self.beams=beams


pisos = []

for id in datos["pisos"]:
    h= datos["pisos"][id]
    col = list(datos["col_piso"][id].keys())
    beam = list(datos["vig_piso"][id].keys())
    piso = Lvl(id,h,col,beam)
    pisos.append(piso)

    

class Beam(Lvl, id, node_i,node_f):
    def __init__(self,):
        x=0


columnas = []












#Se hace un for con cada piso
for piso in pisos:
    id= []
    nodoS =[]
    nodoF = []
    #se hace un for con cada id de columna que se guarda en el objeto piso
    for Col in piso.cols:
        #agrega los ids de la columna por piso
        id.append(Col)
        #agrega los nodos iniciales de cada columna por piso
        nodoS.append(list(datos["columnas"][Col])[0])
        #agrega los nodos finales de cada columna por piso
        nodoF.append(list(datos["columnas"][Col])[1])
    #crea un nuevo objeto columna por piso. cada valor es un arreglo de todos los valores recolectados
    col = columna(id,nodoS,nodoF)
    #se agrega el conjunto de colimnas creado por piso. Es decir solo hay 3 elementos
    columnas.append(col)

#print(columnas[0].id)
#print(columnas[1].id)
print((columnas.len()))


#col = Lvl.col(piso[1].cols,)