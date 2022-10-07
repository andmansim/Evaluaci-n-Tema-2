
lista = [4, 7, 30, 23, 5]
paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 




'''resultado = "2" + 10'''

def errores(a, b):
    try:
        a
    except b:
        print('Error controlado')

errores(7/2, ZeroDivisionError)
errores(lista[10],IndexError)
errores(paises["alemania"], KeyError)



