
class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print('El producto ' + str(self.nombre) + ' se ha creado con éxito')
    
    def __str__(self):
        return f"({self.codigo}) {self.nombre} {self.precio} {self.tipo}"
    
        
    

    lista = []
    
    
    def buscar(nombre):
        for producto in Producto.lista: #busca en la lista que hemos creado antes
            if producto.nombre == nombre:
                return producto
            
    
    def crear(codigo, nombre, precio, tipo):
        producto = Producto(codigo, nombre, precio, tipo) #llamamos a la clase Cliente
        Producto.lista.append(producto)
        return producto
    
    
    def modificar(codigo, nombre, precio, tipo):
        for indice, producto in enumerate(Producto.lista):
            if producto.nombre == nombre: #cliente nos recorre la lita, pero esta se compone de objetos de las clases, por eso podemos poner el .dni. Pq va asociado a la clase Clientes
                Producto.lista[indice].precio = precio

                return Producto.lista[indice]
        
        