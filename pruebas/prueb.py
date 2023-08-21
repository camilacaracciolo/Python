#def factorial(numero):
#    print ("Valor inicial" , numero) 
#    if numero > 1:
#            numero = numero * factorial(numero-1)  
#    print ("valor final" , numero)
#    return numero
#
#print (factorial(5))
#
#
#def area_rectangulo(base, altura):
#    return base * altura
#
#base = 15
#altura = 10
#area = area_rectangulo(base, altura)
#
#print(f"El área del rectángulo con base {base} y altura {altura} es: {area}")
#import math
#
#def area_circulo(radio):
#    return math.pi * radio ** 2
#
#radio = 5
#area = area_circulo(radio)
#
#print(f"El área del círculo con radio {radio} es: {area}")
#def relacion(num1, num2):
#    if num1 > num2:
#        return 1
#    elif num1 < num2:
#        return -1
#    else:
#        return 0
#
#relacion_1 = relacion(5, 10)
#relacion_2 = relacion(10, 5)
#relacion_3 = relacion(5, 5)
#
#print(f"Relación entre 5 y 10: {relacion_1}")
#print(f"Relación entre 10 y 5: {relacion_2}")
#print(f"Relación entre 5 y 5: {relacion_3}")
#
#numero1 = int(input("Dime un numero: "))
#numero2 = int(input("Dime un numero: "))
#def intermedio(num1, num2):
#    medio = (num1 + num2) / 2
#    return medio
#punto_medio = intermedio(numero1, numero2)
#
#print(f"El punto intermedio entre {numero1} y {numero2} es: {punto_medio}")
#def recortar(numero, limite_inferior, limite_superior):
#    if numero < limite_inferior:
#        return limite_inferior
#    elif numero > limite_superior:
#        return limite_superior
#    else:
#        return numero
#
#numero = 15
#limite_inferior = 0
#limite_superior = 10
#resultado = recortar(numero, limite_inferior, limite_superior)
#
#print(f"El resultado de recortar {numero} entre los límites {limite_inferior} y {limite_superior} es: {resultado}")
#
#def separar(lista):
#    pares = []
#    impares = []
#    
#    for numero in lista:
#        if numero % 2 == 0:
#            pares.append(numero)
#        else:
#            impares.append(numero)
#    
#    pares.sort()
#    impares.sort()
#    
#    return pares, impares
#
## Ejemplo de lista de números enteros
#numeros = [5, 10, 3, 8, 7, 4, 1, 6]
#pares_resultado, impares_resultado = separar(numeros)
#
#print("Lista original:", numeros)
#print("Números pares ordenados:", pares_resultado)
#print("Números impares ordenados:", impares_resultado)

#def numerospares (numero):
#
#        if numero % 2 != 0:
#            print("Es impar")
#        elif numero == 0:
#            print("Fin")
#        else: 
#             print("es par" , numero)
#             numerospares (numero - 2)
#
#numerospares(200)2


#suma = 0
#while suma < 500:
#    num = int(input("Ingrese un numero "))
#    suma = suma + num
#    if suma >= 500:
#        print ("Limite", suma)

#class Alumno:
#
#    def __init__(self,nombre, nota):
#        self.nombre = nombre
#        self.nota = nota
#
#    def evaluacion(self):
#        print("No se")
#
#    def edad(self):
#        return 31
#    
#persona1 = Persona("Nicolas" , "Lopez")
#
#print(f"Resultado: {persona1.tipo}\n")
##print(f"Resultado: {persona1.__sueldo}\n")
#print(f"Resultado: {persona1.nombre}\n")
##print(f"Resultado: {persona1.__apellido}\n")
##print(f"Resultado: {persona1.__soy_feliz()}\n")
#print(f"Resultado: {persona1.edad()}\n")
#
#class Alumno:
#    def __init__(self, nombre, nota):
#        self.nombre = nombre
#        self.nota = nota
#    
#    def imprimir_informacion(self):
#        print(f"Nombre: {self.nombre} | Nota: {self.nota}")
#    
#    def verificar_aprobacion(self):
#        if self.nota < 5:
#            print(f"{self.nombre} ha desaprobado.")
#        else:
#            print(f"{self.nombre} ha aprobado.")
#
## Instanciar dos alumnos
#alumno1 = Alumno("Juan", 7)
#alumno2 = Alumno("María", 4)
#
## Imprimir información y verificar aprobación
#alumno1.imprimir_informacion()
#alumno1.verificar_aprobacion()
#
#alumno2.imprimir_informacion()
#alumno2.verificar_aprobacion()
#