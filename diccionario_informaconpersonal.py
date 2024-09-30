#Creación del diccionario informacion_personal
informacion_personal = {
    "nombre": "Christian Peña",
    "edad": 38,
    "ciudad": "Quito",
    "profesion": "Ingeniero de TI"
}

#Acceder al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente
informacion_personal["ciudad"] = "Guaranda"

#Agrega una nueva clave-valor al diccionario que represente la "profesion" de la persona.
informacion_personal["ocupacion"] = "Programador"

# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregarla con un número ficticio
    informacion_personal["telefono"] = "0988888888"

#Eliminación de la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario
print(informacion_personal)