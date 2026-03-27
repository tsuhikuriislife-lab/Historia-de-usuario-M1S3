import json

def agregarProducto(datos,nombre,precio,cantidad):
    datos[nombre] = {"cantidad":cantidad,"precio":precio}
def mostrarInventario(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        inventarioLeidos = json.load(f)
    return inventarioLeidos
def buscarProducto(inventario,nombre):
    if nombre in inventario:
        print(f"Nombre del producto: {nombre}\nCantidad: {inventario[nombre]["cantidad"]}\nPrecio: {inventario[nombre]["precio"]}")
def actualizarProducto(inventario,nombre,nuevo_precio=None,nueva_cantidad=None):
    inventario[nombre] = {"cantidad":nueva_cantidad,"precio":nuevo_precio}
    print("Producto actualizado con exito.")
def eliminarProducto(inventario,nombre):
    if nombre in inventario:
        inventario.pop(nombre)
    else:
        print("El producto no se encuentra en el inventario")
def calcularEstadisticas(inventario):
    totalCantidad = 0
    totalPrecio = 0
    for producto, valor in inventario.items():
        totalCantidad += valor["cantidad"]
    for producto, valor in inventario.items():
        totalPrecio += valor["cantidad"] * valor["precio"]
    print(f"Total cantidad de productos: {totalCantidad}\nTotal valor de productos: {totalPrecio}")
def escribirArchivo(inventario, nombre):
    if not nombre:
        nombre = input("Ingresa el nombre del archivo")
        with open(nombre, 'w', encoding='utf-8') as f:
            json.dump(inventario, f, indent=4)
    with open(nombre,'w',encoding='utf-8') as f:
        json.dump(inventario, f, indent=4)
    print("Archivo guardado correctamente")
def cargarArchivo(inventario):
    nombre = input("\nIngrese el nombre del archivo: ")
    if not nombre.endswith(".json"):
        print(f"'{nombre}' no es un archivo JSON valido")
        nombre = False
    else:
        try:
            with open(nombre, 'r',encoding='utf-8') as f:
                    inventario = json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error de formato JSON: {e}")
        except FileNotFoundError:
            print(f"Error: El archivo {nombre} no existe.\n")
            inventario = {}
            nombre = False
    return inventario, nombre

archivoNombre = False
inventario = {

}






menuOpcion = 0
while menuOpcion != "9":
    if not archivoNombre:
        print("No estas dentro de ningun archivo.")
    else:
        print(f"Dentro de archivo '{archivoNombre}'")
    menuOpcion = input(
        "\nSeleccione una opcion:"
        "\n1.Agregar producto"
        "\n2.Mostrar inventario"
        "\n3.Buscar producto"
        "\n4.Actualizar producto"
        "\n5.Eliminar producto"
        "\n6.Calcular estadisticas"
        "\n7.Guardar archivo"
        "\n8.Cargar archivo"
        "\n9.Salir del programa"
        "\n--- "
    )

    match menuOpcion:
        case "1":
            if not archivoNombre:
                print("No estas dentro de ningun archivo.")
            else:
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                inventario[nombre] = {"cantidad":cantidad,"precio":precio}
                agregarProducto(inventario, nombre, precio, cantidad)
        case "2":
            if not archivoNombre:
                print("No tienes ningun archivo cargado")
            else:
                inventarioLeidos = mostrarInventario(archivoNombre)
                print(f"inventario leidos:\n{inventarioLeidos}")
        case "3":
            if not archivoNombre:
                print("No tienes ningun archivo cargado")
            else:
                nombreProducto = input("Ingresa el nombre del producto que quieres buscar: ")
                if nombreProducto in inventario:
                    buscarProducto(inventario, nombreProducto)
                else:
                    print(f'"{nombreProducto}" no se encuentra dentro del inventario')
        case "4":
            if not archivoNombre:
                print("No tienes ningun archivo cargado")
            else:
                nombreProducto = input("Ingrese el nombre del producto a actualizar: ")
                if nombreProducto not in inventario:
                    print("El producto no esta dentro del inventario.")
                else:
                    nuevaCantidad = float(input("Ingrese la nueva cantidad: "))
                    nuevoPrecio = int(input("Ingrese el nuevo precio: "))
                    actualizarProducto(archivoNombre,inventario,nombreProducto,nuevoPrecio,nuevaCantidad)
        case "5":
            if not archivoNombre:
                print("No tienes ningun archivo cargado")
            else:
                nombreProducto = input("Ingresa el nombre del producto a eliminar: ")
                eliminarProducto(inventario, nombreProducto)
        case "6":
            if not archivoNombre:
                print("No tienes ningun archivo cargado")
            else:
                calcularEstadisticas(inventario)
        case "7":
            escribirArchivo(inventario,archivoNombre)
        case "8":
            inventario, archivoNombre = cargarArchivo(inventario)
