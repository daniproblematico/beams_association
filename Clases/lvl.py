class Lvl:
    def __init__(self, id,H,cols,beams):
        self.id=id
        self.H=H
        self.cols=cols
        self.beams=beams


import json
with open("project.geom", "r") as f:
    datos=json.load(f)

for i in range(len(datos["pisos"])):
    i=Lvl(enumerate(datos["pisos"])[i])
