#herencia y multiple

class Persona:
  def __init__(self, name, email, address):
    self.name = name
    self.email = email
    self.address = address
  def saludar(self):
    print (f"{self.name}:buen dia")    

class Alumno(Persona):

  def __init__(self, name, email, address,legajo , materias = None):
    super().__init__(name, email, address )
    self.legajo = legajo
    if materias is None:
      self.materias = []
    else: 
      self.materias = materias

  def saludar(self):
      print (f"{self.name}:buen dia")

  def addmateria(self,materia):
      if materia not in self.materias:
          self.materias.append(materia)

  def getMaterias(self):
      print(f"{self.name}")
      print("Materias:")
      for materia in self.materias:
         print (f"Curso: {materia}")
  
  

persona1 = Persona("Camila" , "camilacaracciolo@hotmail.com", "Billinghurst436" )
persona1.saludar()
alumno1 = Alumno("Camila" , "camilacaracciolo@hotmail.com", "Billinghurst436", 123456 , ["Lengua" , "MAtematica" , "Quimica"] )
alumno1.saludar()
alumno1.addmateria("Quimica")
alumno1.getMaterias()

#duck typing
class Pato:
   def caminar(self):
      print("Camina")

class gato:
    def caminar(self):
        print("dospasos")

class maestro:
    def atrapar(self, Pato):
       Pato.caminar()
       print("Atrapado")

patito= Pato()
gatito = gato() 
ash = maestro()

ash.atrapar(patito) 
ash.atrapar(gatito)