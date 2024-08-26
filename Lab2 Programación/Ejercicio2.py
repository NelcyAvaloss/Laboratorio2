class Vehiculo:
    def _init_(self, marca, modelo, tipo, color, motor, transmision, combustible, año, kilometraje, precio_compra):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.color = color
        self.motor = motor
        self.transmision = transmision
        self.combustible = combustible
        self.año = año
        self.kilometraje = kilometraje
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()

    def calcular_precio_venta(self):
        return self.precio_compra * 1.4

    def mostrar_informacion(self):
        detalles = [
            f"Marca: {self.marca}",
            f"Modelo: {self.modelo}",
            f"Tipo: {self.tipo}",
            f"Color: {self.color}",
            f"Motor: {self.motor}",
            f"Transmisión: {self.transmision}",
            f"Combustible: {self.combustible}",
            f"Año: {self.año}",
            f"Kilometraje: {self.kilometraje} km",
            f"Precio de compra: ${self.precio_compra:.2f}",
            f"Precio de venta: ${self.precio_venta:.2f}"
        ]
        return detalles


class Agencia:
    def _init_(self):
        self.vehiculos = []

    def registrar_vehiculo(self):
        marca = input("Ingrese la marca del vehículo: ")
        modelo = input("Ingrese el modelo del vehículo: ")
        tipo = input("Ingrese el tipo de vehículo (Nacional/Importado): ")
        color = input("Ingrese el color del vehículo: ")
        motor = input("Ingrese el tipo de motor: ")
        transmision = input("Ingrese el tipo de transmisión (Manual/Automática): ")
        combustible = input("Ingrese el tipo de combustible: ")
        año = input("Ingrese el año del vehículo: ")
        kilometraje = float(input("Ingrese el kilometraje del vehículo: "))
        precio_compra = float(input("Ingrese el precio de compra del vehículo: "))

        vehiculo = Vehiculo(marca, modelo, tipo, color, motor, transmision, combustible, año, kilometraje, precio_compra)
        self.vehiculos.append(vehiculo)
        print(f"\nEl vehículo {marca} {modelo} ha sido registrado con éxito.\n")

    def mostrar_vehiculos(self):
        if not self.vehiculos:
            print("No hay vehículos registrados.\n")
        else:
            print("Vehículos registrados:\n")
            for vehiculo in self.vehiculos:
                for detalle in vehiculo.mostrar_informacion():
                    print(detalle)
                print("")

    def buscar_vehiculo_por_modelo(self):
        modelo_buscar = input("Ingrese el modelo del vehículo a buscar: ")
        encontrados = [vehiculo for vehiculo in self.vehiculos if vehiculo.modelo.lower() == modelo_buscar.lower()]

        if not encontrados:
            print(f"No se encontraron vehículos del modelo '{modelo_buscar}'.\n")
        else:
            print(f"Vehículos encontrados del modelo '{modelo_buscar}':\n")
            for vehiculo in encontrados:
                for detalle in vehiculo.mostrar_informacion():
                    print(detalle)
                print("")


# Ejemplo de uso
agencia = Agencia()

while True:
    print("1. Registrar un vehículo")
    print("2. Mostrar todos los vehículos")
    print("3. Buscar vehículos por modelo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agencia.registrar_vehiculo()
    elif opcion == "2":
        agencia.mostrar_vehiculos()
    elif opcion == "3":
        agencia.buscar_vehiculo_por_modelo()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.\n")