class computador:
    def _int_(self,marca,madelo):
        self.marca = ''
        self.modelo = ''
    def ligar(self):
        print(f"ligando o {self.marca} modelo {self.modelo}")

computador_1 = computador('Dell', 'xps')
computador_1.ligar()