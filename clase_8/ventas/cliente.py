from datetime import datetime

class Cliente():
    
    compras = [] # esto es un atributo de clase
    
    def __init__(self,email):
        self.email = email # esto es un atributo de instancia 
        self.id = datetime.now().timestamp()
        
        
    def registrar_compra(self, producto, valor):
        self.compras.append(
            {
                "producto": producto,
                "valor": valor
            }
        )
        
    def imprimir_compras(self):
        for compra in self.compras:
            print(compra)