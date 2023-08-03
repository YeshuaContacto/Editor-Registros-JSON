import json
from helpers import absPath

datos = []
datos.append({
    "nombre": "Hector",
    "empleo": "Instrauctor",
    "email": "hector@ejemplo.com"
})

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

for contacto in contactos:
    datos.append({
        "nombre": contacto[0],
        "empleo": contacto[1],
        "email": contacto[2]
    })

print(datos)
