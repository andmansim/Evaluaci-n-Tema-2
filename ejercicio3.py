
class Producto:
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
        print('El producto ' + str(self.nombre) + ' se ha creado con éxito')
    
    def __str__(self):
        return f"({self.codigo}) {self.nombre} {self.precio} {self.tipo}"
    
        
    
class Productos:
    lista = []
    
    
    def buscar(nombre):
        for producto in Productos.lista: #busca en la lista que hemos creado antes
            if producto.nombre == nombre:
                return producto
            
    
    def crear(codigo, nombre, precio, tipo):
        producto = Productos(codigo, nombre, precio, tipo) #llamamos a la clase Cliente
        Productos.lista.append(producto)
        Productos.guardar()
        return producto
    
    
    def modificar(codigo, nombre, precio, tipo):
        for indice, producto in enumerate(Productos.lista):
            if producto.nombre == nombre: #cliente nos recorre la lita, pero esta se compone de objetos de las clases, por eso podemos poner el .dni. Pq va asociado a la clase Clientes
                Productos.lista[indice].precio = precio
                Productos.guardar()
                return Productos.lista[indice]
        
        