def suma(n1,n2):
    print("suma")

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def imprimir_informacion(self):
        print(f"Nombre: {self.nombre} | Nota: {self.nota}")
    
    def verificar_aprobacion(self):
        if self.nota < 5:
            print(f"{self.nombre} ha desaprobado.")
        else:
            print(f"{self.nombre} ha aprobado.")

# Instanciar dos alumnos
alumno1 = Alumno("Juan", 7)
alumno2 = Alumno("María", 4)

# Imprimir información y verificar aprobación
alumno1.imprimir_informacion()
alumno1.verificar_aprobacion()

alumno2.imprimir_informacion()
alumno2.verificar_aprobacion()
