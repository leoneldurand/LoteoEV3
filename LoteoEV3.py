# Definición de variables globales
num_filas = 4
num_columnas = 5
precio_por_hectarea = 1000000

# Inicializar matriz de lotes disponibles
lotes_disponibles = [[' ' for _ in range(num_columnas)] for _ in range(num_filas)]

# Lista de lotes seleccionados por los clientes
lotes_seleccionados = []

# Lista de clientes
clientes = []

# Función para mostrar la disponibilidad de lotes
def mostrar_disponibilidad_lotes():
    print("Lotes Disponibles:")
    for fila in lotes_disponibles:
        for lote in fila:
            print('[X]' if lote == 'X' else '[ ]', end=' ')
        print()

# Función para seleccionar un lote
def seleccionar_lote():
    while True:
        fila = int(input("Ingrese la fila del lote: "))
        columna = int(input("Ingrese la columna del lote: "))

        if fila < 0 or fila >= num_filas or columna < 0 or columna >= num_columnas:
            print("Coordenadas inválidas. Intente nuevamente.")
            continue

        if lotes_disponibles[fila][columna] == ' ':
            break
        else:
            print("El lote seleccionado no está disponible. Por favor, elija otro.")

    # Capturar datos del cliente
    rut = input("Ingrese el RUT del cliente: ")
    nombre = input("Ingrese el nombre completo del cliente: ")
    telefono = input("Ingrese el número de teléfono del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")

    # Agregar el lote seleccionado a la lista de lotes seleccionados
    lotes_seleccionados.append((fila, columna))

    # Marcar el lote como vendido en la matriz de lotes disponibles
    lotes_disponibles[fila][columna] = 'X'

    # Agregar el cliente a la lista de clientes
    clientes.append((rut, nombre, telefono, email))

    print("Lote seleccionado con éxito.")

# Función para mostrar los detalles de un lote seleccionado
def mostrar_detalles_lote_seleccionado():
    if len(lotes_seleccionados) == 0:
        print("No se han seleccionado lotes.")
        return

    for i, lote in enumerate(lotes_seleccionados, start=1):
        fila, columna = lote
        numero_lote = i
        tamaño_terreno = 1
        precio = tamaño_terreno * precio_por_hectarea

        print(f"Detalles del Lote {numero_lote}:")
        print(f"Número de lote: {numero_lote}")
        print(f"Tamaño del terreno: {tamaño_terreno} hectárea")
        print(f"Precio: ${precio}")

# Función para mostrar la lista de clientes
def mostrar_clientes():
    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    print("Lista de Clientes:")
    for cliente in clientes:
        rut, nombre, telefono, email = cliente
        print(f"RUT: {rut}")
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {telefono}")
        print(f"Email: {email}")
        print()

# Función principal del programa
def main():
    while True:
        print("----- Menú -----")
        print("1. Ver disponibilidad de lotes")
        print("2. Seleccionar un lote")
        print("3. Ver detalles del lote seleccionado")
        print("4. Ver Clientes")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción inválida. Intente nuevamente.")
            continue

        if opcion == 1:
            mostrar_disponibilidad_lotes()
        elif opcion == 2:
            seleccionar_lote()
        elif opcion == 3:
            mostrar_detalles_lote_seleccionado()
        elif opcion == 4:
            mostrar_clientes()
        elif opcion == 5:
            print("¡Gracias por usar el sistema de Loteos! ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa principal
main()
