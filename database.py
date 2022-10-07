
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        
        return 'El alumno ' + str(self.nombre) + ' se ha añadido correctamente'
    

    def clasificacion(self):
        if self.nota <= 5:
            print('El alumno ha aprobado')
        else:
            print('El alumno ha suspendido' )
            