import random

class Producto:
    def __init__(self, nombre, precio, ubicacion, descripcion, casa, referencia, pais, unidades, garantia):
        self.id = random.randint(1, 100)  
        self.nombre = nombre
        self.precio = precio
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        self.casa = casa
        self.referencia = referencia
        self.pais = pais
        self.unidades = unidades
        self.garantia = garantia

class TiendaComics:
    def __init__(self):
        self.inventario = []

    def registrar_producto(self, producto):
        if len(self.inventario) >= 100:
            print("Error: El inventario está lleno.")
        else:
            self.inventario.append(producto)
            print("Producto registrado exitosamente.")

    def mostrar_productos_bodega(self):
        if not self.inventario:
            print("No hay productos registrados en la bodega.")
        else:
            print("Productos en bodega:")
            for producto in self.inventario:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Unidades: {producto.unidades}")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio}, Descripción: {producto.descripcion}")
                return
        print("Producto no encontrado.")

    def modificar_unidades_compradas(self, nombre, nuevas_unidades):
        for producto in self.inventario:
            if producto.nombre == nombre:
                if nuevas_unidades <= producto.unidades:
                    producto.unidades = nuevas_unidades
                    print("Unidades modificadas correctamente.")
                else:
                    print("Error: La cantidad ingresada es mayor a las unidades compradas inicialmente.")
                return
        print("Producto no encontrado.")

    def eliminar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                confirmacion = input(f"¿Seguro que deseas eliminar el producto '{nombre}'? (s/n): ")
                if confirmacion.lower() == 's':
                    self.inventario.remove(producto)
                    print("Producto eliminado.")
                return
        print("Producto no encontrado.")

def mostrar_menu():
    print("\nBienvenido a la Tienda de Cómics")
    print("1. Registrar un producto")
    print("2. Mostrar productos en bodega")
    print("3. Buscar un producto por nombre")
    print("4. Modificar unidades compradas de un producto")
    print("5. Eliminar un producto")
    print("6. Salir")

tienda = TiendaComics()

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        nombre = input("Nombre del producto: ")
        precio = float(input("Precio del producto: "))
        ubicacion = input("Ubicación del producto: ")
        descripcion = input("Descripción del producto: ")
        casa = input("Casa productora: ")
        referencia = input("Referencia del producto: ")
        pais = input("País de origen: ")
        unidades = int(input("Unidades disponibles: "))
        garantia = input("¿Tiene garantía? (True/False): ")
        producto = Producto(nombre, precio, ubicacion, descripcion, casa, referencia, pais, unidades, garantia)
        tienda.registrar_producto(producto)

    elif opcion == '2':
        tienda.mostrar_productos_bodega()

    elif opcion == '3':
        nombre = input("Ingrese el nombre del producto a buscar: ")
        tienda.buscar_producto_por_nombre(nombre)

    elif opcion == '4':
        nombre = input("Ingrese el nombre del producto a modificar: ")
        nuevas_unidades = int(input("Ingrese las nuevas unidades compradas: "))
        tienda.modificar_unidades_compradas(nombre, nuevas_unidades)

    elif opcion == '5':
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        tienda.eliminar_producto(nombre)

    elif opcion == '6':
        print("Gracias por usar la Tienda de Cómics. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")
