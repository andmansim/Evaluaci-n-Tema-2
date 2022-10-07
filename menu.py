import database as db
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
                alumno = db.Alumno(key, value)
                print(alumno)
                ap = alumno.clasificacion()

            
                
        if opcion == '2':
            print("Buscando un cliente...\n")
            
        
        if opcion == '3':
            print("Añadiendo un cliente...\n")
            
        if opcion == '4':
            print("Añadiendo un cliente...\n")
                
        if opcion == '5':
           print("Añadiendo un cliente...\n")
       