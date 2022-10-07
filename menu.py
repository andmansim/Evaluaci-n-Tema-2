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
            print("Listando los clientes...\n")
            alumno = db.Alumno('Diego', 3)
            alumno1 = db.Alumno('Carlota', 8)
            alumno3 = db.Alumno('Pepe', 6)
            
            
                
        if opcion == '2':
            print("Buscando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")
        
        if opcion == '3':
            print("Añadiendo un cliente...\n")
            # Comprobación de DNI válido
            dni = None
            while 1:
                dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")
        
        if opcion == '4':
            print("Modificando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 chars) [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 chars) [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")
                
        if opcion == '5':
            print("Borrando un cliente...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            print("Cliente borrado correctamente.") if db.Clientes.borrar(dni) else print("Cliente no encontrado.")
            
       
        input("\nPresiona ENTER para continuar...")