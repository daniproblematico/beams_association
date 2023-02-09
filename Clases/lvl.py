import json
with open("project.geom", "r") as f:
    datos=json.load(f)

class Lvl:
    def __init__(self, lvl_id,H,cols,beams):
        self.lvl_id=lvl_id
        self.H=H
        self.cols=cols
        self.beams=beams

    def Create_levels(self,lvl_id,H,cols,beams,datos):
        pisos = []
        for lvl_id in datos["pisos"]:
            h= datos["pisos"][lvl_id]
            col = list(datos["col_piso"][lvl_id].keys())
            beam = list(datos["vig_piso"][lvl_id].keys())
            piso = Lvl(lvl_id,h,col,beam)
            pisos.append(piso)

        return(pisos)


    def Create_beams(datos, Beam, pisos):
        vigas = []
        for n in pisos:
            for b in n.beams:  # b es una viga perteneciente al piso n
                nodoi = datos["vigas"][b][0]
                nodod = datos["vigas"][b][1]
                viga = Beam(n.lvl_id, b, nodoi, nodod)
                



        



class Beam(Lvl):
    def __init__(self, lvl_id, beam_id, node_i, node_f):
        self.lvl_id=lvl_id
        self.beam_id=lvl_id
        self.node_i=node_i
        self.node_f=node_f
















