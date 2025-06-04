class Empleado:
    def __init__(self,sueldo,nombre):
        self.sueldo = sueldo
        self.nombre =nombre
    def calcular_sueldo(self):
        sueldo = 12 * self.sueldo * (1 + 1/100)
        print (f"EL sueldo  de {self.nombre}-> es de {self.sueldo}")
class Diseñador(Empleado):
      def calcular_sueldo(self):
        sueldo = 12 * self.sueldo *(1 + 3/100)
        print (f"EL sueldo  de {self.nombre}-> es de {self.sueldo}")
class Programador(Empleado):
      def calcular_sueldo(self):
        sueldo = 12 * self.sueldo *(1 + 4/100)
        print (f"EL sueldo  de {self.nombre}-> es de {self.sueldo}")
        
        
        
empleados = [
  
  Empleado(10000,"jose"),
  Diseñador(20000,"jon"),
  Programador(345000,"alex")
]
def sueldo_empresa():
  for employe in empleados:
    employe.calcular_sueldo()
    
sueldo_empresa()
  
