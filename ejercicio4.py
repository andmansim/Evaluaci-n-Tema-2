
class Errores:
    def errores(a, b):
        try:
            a
        except b:
            print('Error controlado')
        if b == TypeError:
            print('No se puede operar elementos de distintos tipos')
        elif b == KeyError:
            print('Ese key no está en el diccionario')
        elif b == IndexError:
            print('No se encuentra ese índice')
        elif b == ZeroDivisionError:
            print('No se puede dividir entre cero')





