class Cuaderno:
   def __init__(self, hojas, costo_base):
       self.hojas = hojas
       self.marca = "HOJITAS"
       self.costo_base = costo_base
       self.precio_venta = self.calcular_precio_venta()
   def calcular_precio_venta(self):
       return self.costo_base * 1.3
   def mostrar_informacion(self):
       detalles = [
           f"Marca: {self.marca}",
           f"Hojas: {self.hojas}",
           f"Costo Base: ${self.costo_base:.2f}",
           f"Precio de Venta: ${self.precio_venta:.2f}"
       ]
       return detalles
 
class Lapiz:
   def __init__(self, tipo, costo_base):
       self.tipo = tipo
       self.marca = "RAYAS"
       self.costo_base = costo_base
       self.precio_venta = self.calcular_precio_venta()
   def calcular_precio_venta(self):
       return self.costo_base * 1.3
   def mostrar_informacion(self):
       detalles = [
           f"Marca: {self.marca}",
           f"Tipo: {self.tipo}",
           f"Costo Base: ${self.costo_base:.2f}",
           f"Precio de Venta: ${self.precio_venta:.2f}"
       ]
       return detalles
 
class Papeleria:
   def __init__(self):
       self.inventario = []
   def registrar_cuaderno(self):
       hojas = input("Ingrese la cantidad de hojas (50/100): ")
       costo_base = float(input("Ingrese el costo base del cuaderno: "))
       cuaderno = Cuaderno(hojas, costo_base)
       self.inventario.append(cuaderno)
       print("\nCuaderno registrado con éxito.\n")
   def registrar_lapiz(self):
       tipo = input("Ingrese el tipo de lápiz (grafito/colores): ").lower()
       costo_base = float(input("Ingrese el costo base del lápiz: "))
       lapiz = Lapiz(tipo, costo_base)
       self.inventario.append(lapiz)
       print("\nLápiz registrado con éxito.\n")
   def mostrar_inventario(self):
       if not self.inventario:
           print("No hay productos registrados.\n")
       else:
           print("Inventario de la papelería:\n")
           for producto in self.inventario:
               for detalle in producto.mostrar_informacion():
                   print(detalle)
               print("")
 
# Ejemplo de uso.
papeleria = Papeleria()
while True:
   print("1. Registrar cuaderno")
   print("2. Registrar lápiz")
   print("3. Mostrar inventario")
   print("4. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       papeleria.registrar_cuaderno()
   elif opcion == "2":
       papeleria.registrar_lapiz()
   elif opcion == "3":
       papeleria.mostrar_inventario()
   elif opcion == "4":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")
       