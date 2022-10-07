
class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print('El producto ' + str(self.nombre) + ' se ha creado con éxito')
    
    def __str__(self):
        return f"({self.codigo}) {self.nombre} {self.precio} {self.tipo}"
    

    def modificar(self, a):
        self.precio = a
        return 'Producto cambiado' + f"({self.codigo}) {self.nombre} {self.precio} {self.tipo}"
        
        