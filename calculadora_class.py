class Calculadora:
    def __init__(self) -> None:
        pass
    def sumar(self,a, b):
        
        return a + b
      
    def restar(self,a, b):
        return a - b

    def multiplicar(self,a, b):
        return a * b

    def dividir(self,a, b):
        if b != 0:
            return a / b
        else:
            return "Error. División por 0."
        
mi_calculadora = Calculadora()
print(f"el resultado de la suma es  => {mi_calculadora.sumar(23,86)}")
print(f"el resultado de la resta es  => {mi_calculadora.restar(43,8)}")
print(f"el resultado de la multiplicacion es  => {mi_calculadora.multiplicar(53,8)}")
print(f"el resultado de la division es  => {mi_calculadora.dividir(12,8)}")