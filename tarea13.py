temperaturas = [
    [   # Riobamba
        [   # Semana 1
            {"dia": "Lunes", "temp": 43},
            {"dia": "Martes", "temp": 54},
            {"dia": "Miércoles", "temp": 62},
            {"dia": "Jueves", "temp": 73},
            {"dia": "Viernes", "temp": 97},
            {"dia": "Sábado", "temp": 18},
            {"dia": "Domingo", "temp": 35}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 56},
            {"dia": "Martes", "temp": 99},
            {"dia": "Miércoles", "temp": 13},
            {"dia": "Jueves", "temp": 31},
            {"dia": "Viernes", "temp": 67},
            {"dia": "Sábado", "temp": 49},
            {"dia": "Domingo", "temp": 53}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 47},
            {"dia": "Martes", "temp": 71},
            {"dia": "Miércoles", "temp": 65},
            {"dia": "Jueves", "temp": 92},
            {"dia": "Viernes", "temp": 38},
            {"dia": "Sábado", "temp": 21},
            {"dia": "Domingo", "temp": 55}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 65},
            {"dia": "Martes", "temp": 89},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 19},
            {"dia": "Viernes", "temp": 43},
            {"dia": "Sábado", "temp": 57},
            {"dia": "Domingo", "temp": 71}
        ]
    ],
    [   # Cuenca
        [   # Semana 1
            {"dia": "Lunes", "temp": 28},
            {"dia": "Martes", "temp": 84},
            {"dia": "Miércoles", "temp": 98},
            {"dia": "Jueves", "temp": 40},
            {"dia": "Viernes", "temp": 63},
            {"dia": "Sábado", "temp": 75},
            {"dia": "Domingo", "temp": 39}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 34},
            {"dia": "Martes", "temp": 56},
            {"dia": "Miércoles", "temp": 67},
            {"dia": "Jueves", "temp": 87},
            {"dia": "Viernes", "temp": 18},
            {"dia": "Sábado", "temp": 89},
            {"dia": "Domingo", "temp": 91}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 51},
            {"dia": "Martes", "temp": 75},
            {"dia": "Miércoles", "temp": 58},
            {"dia": "Jueves", "temp": 79},
            {"dia": "Viernes", "temp": 62},
            {"dia": "Sábado", "temp": 65},
            {"dia": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 75},
            {"dia": "Martes", "temp": 47},
            {"dia": "Miércoles", "temp": 59},
            {"dia": "Jueves", "temp": 81},
            {"dia": "Viernes", "temp": 44},
            {"dia": "Sábado", "temp": 72},
            {"dia": "Domingo", "temp": 29}
        ]
    ],
    [   # Puyo
        [   # Semana 1
            {"dia": "Lunes", "temp": 54},
            {"dia": "Martes", "temp": 62},
            {"dia": "Miércoles", "temp": 57},
            {"dia": "Jueves", "temp": 87},
            {"dia": "Viernes", "temp": 97},
            {"dia": "Sábado", "temp": 45},
            {"dia": "Domingo", "temp": 89}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 54},
            {"dia": "Martes", "temp": 61},
            {"dia": "Miércoles", "temp": 33},
            {"dia": "Jueves", "temp": 76},
            {"dia": "Viernes", "temp": 97},
            {"dia": "Sábado", "temp": 28},
            {"dia": "Domingo", "temp": 11}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 65},
            {"dia": "Martes", "temp": 76},
            {"dia": "Miércoles", "temp": 32},
            {"dia": "Jueves", "temp": 45},
            {"dia": "Viernes", "temp": 79},
            {"dia": "Sábado", "temp": 56},
            {"dia": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 76},
            {"dia": "Martes", "temp": 82},
            {"dia": "Miércoles", "temp": 54},
            {"dia": "Jueves", "temp": 67},
            {"dia": "Viernes", "temp": 52},
            {"dia": "Sábado", "temp": 87},
            {"dia": "Domingo", "temp": 65}
        ]
    ]
]





# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["Riobamba","Cuenca","Puyo"]
for ciudad_idx, ciudad in enumerate(temperaturas):
        for semana_idx, semana in enumerate(ciudad):
             suma_temperaturas= sum([dia["temp"]for dia in semana])
             promedio = suma_temperaturas / len(semana)

             print(f"promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f}grados")
