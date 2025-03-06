usuario="David Aguilar"
pin=703007
saldo=300

def sesion():
    intentos=2
    ingresaUsuario=input("Ingresa tu usuario: ")
    ingresaPin=input("Ingresa tu pin: ")

    while((ingresaUsuario!=usuario or int(ingresaPin)!=pin) and intentos>0):
        intentos-=1
        print(f"\nError, usuario o pin incorrectos te quedan {intentos+1}\n")
        ingresaUsuario=input("Ingresa tu usuario: ")
        ingresaPin=input("Ingresa tu pin: ")

    if intentos==0:
        print("\nSe bloqueó el acceso, fin del programa")

    if ingresaUsuario==usuario and int(ingresaPin)==pin:

        opcion=input("Menú: \nIngresa 1 para consultar tu saldo.\n2 para hacer un retiro.\n3 para salir.\n")

        while opcion!="1" and opcion!="2" and opcion!="3":

            print("Error, solo puedes ingresar 1, 2 o 3")
            opcion=input("Menú: \nIngresa 1 para consultar tu saldo.\n2 para hacer un retiro.\n3 para salir.\n")
        
        if opcion=="1":
            print(saldo)

        if opcion=="2":
           retiro=input("Ingresa la cantidad a retirar: $")

           while not retiro.isdigit():
               
               print("\nError, debe ser un valor numerico")
               retiro=input("Ingresa la cantidad a retirar: $")

           while int(retiro)>saldo:
               
               print("\nError, la cantidad retiro es mayor a tu saldo\n")
               retiro=input("Ingresa la cantidad a retirar: $")

           print(f"\nRetiro hecho exitosamente, tu nuevo saldo es {saldo-int(retiro)}")
