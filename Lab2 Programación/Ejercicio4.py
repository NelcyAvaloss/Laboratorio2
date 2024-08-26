class Perro:
    def _init_(self, nombre, raza, edad, peso, color, sexo, dueño, contacto):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.sexo = sexo
        self.dueño = dueño
        self.contacto = contacto
        self.estado = "NO ATENDIDO"  # Estado inicial.
        self.tamaño = self.determinar_tamaño()  # Determinar tamaño según el peso.

    def determinar_tamaño(self):
        return "Grande" if self.peso >= 10 else "Pequeño"

    def atender(self):
        self.estado = "ATENDIDO"  # Cambiar el estado a "ATENDIDO".

    def mostrar_info(self):
        return [
            f"Nombre: {self.nombre}",
            f"Raza: {self.raza}",
            f"Edad: {self.edad} años",
            f"Peso: {self.peso} kg",
            f"Color: {self.color}",
            f"Sexo: {self.sexo}",
            f"Dueño: {self.dueño}",
            f"Contacto: {self.contacto}",
            f"Estado: {self.estado}",
            f"Tamaño: {self.tamaño}"
        ]


class Veterinaria:
    def _init_(self):
        self.pacientes = []  # Lista para almacenar los perros.

    def registrar_perro(self):
        nombre = input("Ingrese el nombre del perro: ")
        raza = input("Ingrese la raza del perro: ")
        edad = int(input("Ingrese la edad del perro (en años): "))
        peso = float(input("Ingrese el peso del perro (en kg): "))
        color = input("Ingrese el color del perro: ")
        sexo = input("Ingrese el sexo del perro (Macho/Hembra): ")
        dueño = input("Ingrese el nombre del dueño: ")
        contacto = input("Ingrese el número de contacto del dueño: ")

        perro = Perro(nombre, raza, edad, peso, color, sexo, dueño, contacto)
        perro.atender()
        self.pacientes.append(perro)  # Agregar el perro a la lista de pacientes.
        print(f"\nEl perro {nombre} ha sido registrado con éxito.\n")

    def buscar_perro(self, nombre):
        for perro in self.pacientes:
            if perro.nombre.lower() == nombre.lower():
                return perro.mostrar_info()
        return None


# Ejemplo de uso.
veterinaria = Veterinaria()

while True:
    print("1. Registrar un perro")
    print("2. Mostrar información de un perro por nombre")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        veterinaria.registrar_perro()
    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre del perro a buscar: ")
        info = veterinaria.buscar_perro(nombre_buscar)
        if info:
            print("\nInformación del perro:\n")
            for linea in info:
                print(linea)
            print("")
        else:
            print(f"No se encontró ningún perro con el nombre {nombre_buscar}.\n")
    elif opcion == "3":
        break
    else:
        print("Opción no válida. Por favor, seleccione nuevamente.\n")