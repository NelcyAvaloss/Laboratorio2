
# En una tienda de ropa se necesita gestionar su inventario de manera eficiente. La tienda vende 
# tres tipos de productos: camisetas, pantalones y chaquetas. Cada producto 
# tiene diferentes tallas y colores, y es necesario registrar la información del inventario.
# Además, la tienda quiere saber el valor total de su inventario, calculado 
# a partir de los precios de compra y de venta de cada producto.


# En este ejercicio hay que crear un programa que permita a la tienda gestionar su inventario 
# de ropa. Los productos tienen características como tipo, talla, color, precio de compra y precio 
# de venta. Se implementará la funcionalidad para registrar nuevos productos, visualizar los detalles 
# de los productos existentes, y calcular el valor total del inventario.


class ProductoRopa:
    def _init_(self, tipo, talla, color, precio_compra):
        self.tipo = tipo         # Camiseta, Pantalón, Chaqueta.
        self.talla = talla       # S, M, L, XL.
        self.color = color       # Rojo, Azul, Negro, etc.
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.5

    def mostrar_informacion(self):
        detalles = [
            f"Tipo: {self.tipo}",
            f"Talla: {self.talla}",
            f"Color: {self.color}",
            f"Precio de compra: ${self.precio_compra:.2f}",
            f"Precio de venta: ${self.precio_venta:.2f}"
        ]
        return detalles


class Inventario:
    def _init_(self):
        self.productos = []  # Lista para almacenar los productos de ropa.

    def registrar_producto(self):
        tipo = input("Ingrese el tipo de producto (Camiseta/Pantalón/Chaqueta): ")
        talla = input("Ingrese la talla del producto (S/M/L/XL): ")
        color = input("Ingrese el color del producto: ")
        precio_compra = float(input("Ingrese el precio de compra del producto: "))

        producto = ProductoRopa(tipo, talla, color, precio_compra)
        self.productos.append(producto)
        print(f"\nEl producto {tipo} de talla {talla} ha sido registrado con éxito.\n")

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.\n")
        else:
            print("Productos registrados:\n")
            for producto in self.productos:
                for detalle in producto.mostrar_informacion():
                    print(detalle)
                print("")  # Espacio entre productos.

    def calcular_valor_inventario(self):
        valor_total = sum(producto.precio_venta for producto in self.productos)
        print(f"Valor total del inventario: ${valor_total:.2f}\n")


# Ejemplo de uso.
inventario = Inventario()

while True:
    print("1. Registrar un producto")
    print("2. Mostrar todos los productos")
    print("3. Calcular valor total del inventario")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        inventario.registrar_producto()
    elif opcion == "2":
        inventario.mostrar_productos()
    elif opcion == "3":
        inventario.calcular_valor_inventario()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.\n")


# Este programa permite a la tienda de ropa gestionar su inventario registrando nuevos 
# productos, visualizando los productos existentes, y calculando el valor total del inventario.
# Logramos resolver la necesidad de mantener un registro ordenado de los productos de ropa,
# así como conocer el valor total del inventario, lo que facilita la toma de decisiones comerciales.