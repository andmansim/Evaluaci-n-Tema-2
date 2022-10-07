
class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print('El producto ' + str(self.nombre) + ' se ha creado con éxito')
    
    def __str__(self):
        return 'El producto ' + self.nombre + ' se ha creado con éxito'
    
    
    @staticmethod
    def modificar(codigo, nombre, precio, tipo):
        for indice, cliente in enumerate(Clientes.lista):
            if cliente.dni == dni: #cliente nos recorre la lita, pero esta se compone de objetos de las clases, por eso podemos poner el .dni. Pq va asociado a la clase Clientes
                Clientes.lista[indice].nombre = nombre
                Clientes.lista[indice].apellido =apellido
                Clientes.guardar()
                return Clientes.lista[indice]