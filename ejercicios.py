#Ejercicio 1
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
        print(str(self.nombre) + ' se ha creado correctamente')

    def clasificacion(self):
        if self.nota <= 5:
            print('El alumno ha aprobado')
        else:
            print('El alumno ha suspendido' )

#Ejercicio 2

class Alumno1:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    def __str__(self):
        
        return 'El alumno ' + self.nombre + ' se ha añadido correctamente'

    def clasificacion(self):
        if self.nota <= 5:
            print('El alumno ha aprobado')
        else:
            print('El alumno ha suspendido' )
    
    
            