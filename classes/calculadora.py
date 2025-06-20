import tkinter as tk

class Calculadora:
  
    def sumar(self,a, b):        return a + b
    def restar(self,a, b):       return a - b
    def multiplicar(self,a, b):  return a * b
    def dividir(self,a, b):      return a / b if b != 0 else "Error. División por 0."


class MiCalculadora(tk.Frame):
  
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.calculadora = Calculadora()

       
        self.entry1 = tk.Entry(self, width=10)
        self.entry2 = tk.Entry(self, width=10)

        self.entry1.grid(row=0, column=0, padx=5, pady=5)
        self.entry2.grid(row=0, column=1, padx=5, pady=5)

       
        btn_sumar = tk.Button(self, text="+", command=self.sumar)
        btn_restar = tk.Button(self, text="-", command=self.restar)
        btn_multiplicar = tk.Button(self, text="*", command=self.multiplicar)
        btn_dividir = tk.Button(self, text="/", command=self.dividir)

        btn_sumar.grid(row=1, column=0, sticky="ew")
        btn_restar.grid(row=1, column=1, sticky="ew")
        btn_multiplicar.grid(row=2, column=0, sticky="ew")
        btn_dividir.grid(row=2, column=1, sticky="ew")

       
        self.result_label = tk.Label(self, text="Resultado:", font=("Arial", 12))
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

    def obtener_numeros(self):
      
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            self.result_label.config(text="Error: Entradas no válidas.")
            return None, None

    def mostrar_resultado(self, resultado):
      
        self.result_label.config(text=f"Resultado: {resultado}")

    def sumar(self): 
        a, b = self.obtener_numeros()
        if a is not None:
            self.mostrar_resultado(self.calculadora.sumar(a, b))

    def restar(self): 
        a, b = self.obtener_numeros()
        if a is not None:
            self.mostrar_resultado(self.calculadora.restar(a, b))

    def multiplicar(self): 
        a, b = self.obtener_numeros()
        if a is not None:
            self.mostrar_resultado(self.calculadora.multiplicar(a, b))

    def dividir(self): 
        a, b = self.obtener_numeros()
        if a is not None:
            self.mostrar_resultado(self.calculadora.dividir(a, b))

