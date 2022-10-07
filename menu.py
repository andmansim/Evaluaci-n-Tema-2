import ejercicios as e
import ejercicio3 as e3
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
           
            for key, value in p:
                
                producto = e3.Producto(value[0], key, value[1], value[2])
            
        if opcion == '4':
            print("Añadiendo un cliente...\n")
                
        if opcion == '5':
           print("Añadiendo un cliente...\n")
       