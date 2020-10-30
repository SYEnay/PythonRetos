acceso="no"
while acceso=="no":
    contraseña=input("Escribe la contraseña: ")
    if contraseña == "1234":
        print("Bienvenido")
        acceso="si"
    else:
        print("La contraseña es incorrecta")
        acceso=input("¿Quiers Salir?")

if acceso=="si":
    print("Adios")
else:
    acceso=input("¿Quiers Salir? si o no")