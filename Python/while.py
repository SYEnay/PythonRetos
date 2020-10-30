#Ejercicio: Crear un programa que simule el cresimiento de una persona cuando llegue a 18 termina
crecer="si"
edad=int(input("¿Cúantos años tienes? "))
while crecer=="si":
    if (edad<18):
        crecer= input("¿Quieres crecer un año? ")
        edad=edad+1
        print("Ahora tienes: ",edad)
    else: 
        print("Ya eres muy grande :P")
        crecer="no"
else: 
    print("ya no puedes crecer más :P")

#Bucle
salir="no"
while salir=="no":
    print("Estás en un ciclo")
    salir=input("¿Quieres salir?")
else:
    print("Adios")