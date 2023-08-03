from ventas.cliente import Cliente

cliente_1 = Cliente("sofiaontivero@gmail.com")

cliente_1.imprimir_compras()

print("." * 90)

cliente_1.registrar_compra("Termo", 100)
cliente_1.registrar_compra("mate", 80)
cliente_1.registrar_compra("bombilla", 30)
cliente_1.registrar_compra("terba", 5)


cliente_1.imprimir_compras()