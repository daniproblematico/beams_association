

import json
with open("project.geom", "r") as f:
    datos=json.load(f)
print(datos.values)


import json
with open("project.geom", "r") as f:
    datos=json.load(f)

for i in range(len(datos["pisos"])):
    print (i)