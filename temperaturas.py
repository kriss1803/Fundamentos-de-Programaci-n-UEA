
#Tarea: Iteración de arreglos multidimensionales con bucles anidados

#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
#Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.

ciudades = ['Quito', 'Guayaquil', 'Cuenca']

#Crear una matriz 3D
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

#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.
c=0
print("Promedio de temperaturas por ciudades")
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