
base_de_datos = {}


def registrar_usuario():
    nombre = input("Ingresa tu nombre: ")
    email = input("Ingresa tu email: ")
    contraseña = input("Ingresa tu contraseña: ")

    
    if email in base_de_datos:
        print("Este email ya está registrado.")
        return

    
    base_de_datos[email] = {
        "nombre": nombre,
        "email": email,
        "contraseña": contraseña
    }
    print("Usuario registrado con éxito.")


def iniciar_sesion():
    email = input("Ingresa tu email: ")
    contraseña = input("Ingresa tu contraseña: ")

   
    if email in base_de_datos:
        
        if base_de_datos[email]["contraseña"] == contraseña:
            print(f"Bienvenido, {base_de_datos[email]['nombre']}!")
        else:
            print("Contraseña incorrecta.")
    else:
        print("El email no está registrado.")


def mostrar_usuarios():
    if not base_de_datos:
        print("No hay usuarios registrados.")
    else:
        for email, datos in base_de_datos.items():
            print(f"Nombre: {datos['nombre']}, Email: {email}")


def ejecutar_programa():
    while True:
        print("\n---- Menú ----")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Mostrar usuarios registrados")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            mostrar_usuarios()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


ejecutar_programa()
