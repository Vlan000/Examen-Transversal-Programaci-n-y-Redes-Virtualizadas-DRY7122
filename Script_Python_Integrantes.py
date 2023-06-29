integrantes = [
    "Dylan Romero",
    "Alan Walker",
    "Tobey maguire",
    # Agrega más nombres y apellidos si es necesario
]

# Recorrer la lista de integrantes y dividir los nombres y apellidos
lista_nombres_apellidos = []
for integrante in integrantes:
    nombre_apellido = integrante.split()
    lista_nombres_apellidos.append(nombre_apellido)

# Imprimir la lista con los nombres y apellidos
for nombre_apellido in lista_nombres_apellidos:
    print(nombre_apellido)