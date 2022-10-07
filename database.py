
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print('El alumno se ha creado con éxito')
    
    @staticmethod
    def clasificaion(self):
        if self.nota <= 5:
            print('El alumno ha aprobado')
        else:
            print('El alumno ha suspendido' )
            