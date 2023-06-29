class Integrante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Crear una lista de objetos Integrante
integrantes = [
    Integrante("Dylan", "Romero"),
    Integrante("María", "González"),
    Integrante("Carlos", "López"),
    # Agrega más nombres y apellidos si es necesario
]

# Imprimir la lista con los nombres y apellidos
for integrante in integrantes:
    nombre = integrante.nombre
    apellido = integrante.apellido
    print(f"{nombre} {apellido}")