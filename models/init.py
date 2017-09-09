from models.clientes import Cliente
cliente = Cliente('Omar','Hernandez','24')
cliente.edad = 27
print(cliente.edad)
print(cliente.nombres, len(cliente))