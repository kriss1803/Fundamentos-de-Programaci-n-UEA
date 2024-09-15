#Tarea: Tarea: Definición y uso de funciones en programación

#Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo. La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.

#Utiliza como base el ejemplo anterior, donde tenías datos de 3 ciudades durante 4 semanas.

#Tu función debe recibir estos datos como parámetros y calcular la temperatura promedio de cada ciudad.

#Vector ciudades para guardar el nombre de cada ciudad
ciudades = ['Quito', 'Guayaquil', 'Cuenca']

#Matriz 3D con las temperaturas de cada ciudad por semana y día.
temperaturas = [
    [   # Quito
        [   # Semana 1
            {"dia": "Lunes", "temp": 19},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 12},
            {"dia": "Jueves", "temp": 18},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 21},
            {"dia": "Domingo", "temp": 25}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 20},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 22},
            {"dia": "Jueves", "temp": 23},
            {"dia": "Viernes", "temp": 23},
            {"dia": "Sábado", "temp": 22},
            {"dia": "Domingo", "temp": 20}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 22},
            {"dia": "Martes", "temp": 21},
            {"dia": "Miércoles", "temp": 24},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 23},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 20},
            {"dia": "Martes", "temp": 19},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 20},
            {"dia": "Domingo", "temp": 18}
        ]

    ],
    [  # Guayaquil
        [  # Semana 1
            {"dia": "Lunes", "temp": 33},
            {"dia": "Martes", "temp": 34},
            {"dia": "Miércoles", "temp": 34},
            {"dia": "Jueves", "temp": 33},
            {"dia": "Viernes", "temp": 34},
            {"dia": "Sábado", "temp": 34},
            {"dia": "Domingo", "temp": 32}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 35},
            {"dia": "Martes", "temp": 35},
            {"dia": "Miércoles", "temp": 34},
            {"dia": "Jueves", "temp": 35},
            {"dia": "Viernes", "temp": 33},
            {"dia": "Sábado", "temp": 32},
            {"dia": "Domingo", "temp": 33}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 35},
            {"dia": "Martes", "temp": 34},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 35},
            {"dia": "Viernes", "temp": 35},
            {"dia": "Sábado", "temp": 35},
            {"dia": "Domingo", "temp": 34}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 33},
            {"dia": "Martes", "temp": 33},
            {"dia": "Miércoles", "temp": 34},
            {"dia": "Jueves", "temp": 34},
            {"dia": "Viernes", "temp": 34},
            {"dia": "Sábado", "temp": 33},
            {"dia": "Domingo", "temp": 33}
        ]
    ],
    [  # Cuenca
        [  # Semana 1
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 14},
            {"dia": "Viernes", "temp": 15},
            {"dia": "Sábado", "temp": 14},
            {"dia": "Domingo", "temp": 12}
        ],
        [  # Semana 2
            {"dia": "Lunes", "temp": 16},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 17},
            {"dia": "Jueves", "temp": 17},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 21}
        ],
        [  # Semana 3
            {"dia": "Lunes", "temp": 18},
            {"dia": "Martes", "temp": 20},
            {"dia": "Miércoles", "temp": 21},
            {"dia": "Jueves", "temp": 17},
            {"dia": "Viernes", "temp": 17},
            {"dia": "Sábado", "temp": 19},
            {"dia": "Domingo", "temp": 21}
        ],
        [  # Semana 4
            {"dia": "Lunes", "temp": 17},
            {"dia": "Martes", "temp": 16},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 15},
            {"dia": "Viernes", "temp": 18},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 18}
        ]
    ]
]

#Definición de la función para calcular la temperatura promedio de cada ciudad
def promedio_temperaturas(ciudades, temperaturas):
    c=0
    for ciudad in temperaturas:
        print(ciudades[c])
        c=c+1
        x=1
        for semana in ciudad:
            suma = 0
            for dia in semana:
                suma += dia['temp']
            p= suma / 7
            print(f"Semana {x} : {p:.2f}°C")
            x=x+1
        print("\n")

#Llamado de la función para calcular el promedio de temperaturas
print("Promedio de temperaturas por ciudades")
promedio_temperaturas(ciudades, temperaturas)