
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return 
    
    @staticmethod
    def clasificaion(self):
        if self.nota <= 5:
            print('El alumno ha aprobado')
        else:
            print('El alumno ha suspendido' )
            