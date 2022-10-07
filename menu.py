import ejercicios as e
import ejercicio3 as e3
import ejercicio4 as e4
import ejercicio5 as e4

def iniciar():
    while True:
        
        print("========================")
        print(" BIENVENIDO ")
        print("========================")
        print("[1] Ejercicio 1 ")
        print("[2] Ejercicio 2 ")
        print("[3] Ejercicio 3 ")
        print("[4] Ejercicio 4 ")
        print("[5] Ejercicio 5")
        print("========================")
        opcion = input("> ")

        if opcion == '1':
            print("Alumnos\n")
            a = {'Diego': 3, 'Carlota': 8, 'Pepe': 6}
            for key, value in a.items():
                alumno = e.Alumno(key, value)
                print(alumno)
                ap = alumno.clasificacion()

            
                
        if opcion == '2':
            print("Clase alumno modificada\n")
            print("Alumnos\n")
            a = {'Diego': 3, 'Carlota': 8, 'Pepe': 6}
            for key, value in a.items():
                alumno = e.Alumno(key, value)
                print(alumno)
                ap = alumno.clasificacion()
            
        
        if opcion == '3':
            print("Productos de la tienda\n")
            p = {'leche': ['08685', 4, 'comida'], 'zapatos':['46328',  10, 'ropa'], 'móvil': ['08685', 300, 'tecnología'] }
           
            for key, value in p.items():
                
                producto = e3.Producto(value[0], key, value[1], value[2])
                b = producto.buscar(key)
                c = producto.crear(value[0], key, value[1], value[2])
                m = producto.modificar(value[0], key, value[1], value[2])
                print(m)
            
        if opcion == '4':
            print("Controlando errores\n")
            lista = [4, 7, 30, 23, 5]
            paises = { "españa":"español", "eeuu":"inglés", "italia":"italiano" } 
            error = e4.Errores()
            error.errores(7/2, ZeroDivisionError)
            error.errores(7/2, ZeroDivisionError)
            error.errores(lista[10],IndexError)
            error.errores(paises["alemania"], KeyError)
            error.errores("2" + 10, TypeError)
                
        if opcion == '5':
           print("Herencia\n")
           print('No está disponible')
       