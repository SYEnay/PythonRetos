#Ejercicio: Votaciones
#Entradas
edad=input("Ingrese su edad: ")
edad=int(edad)
#Operaciones
if edad >= 18 and edad <= 100:
    print("Pruedes votar")
elif edad >= 3 and edad < 17:
    print("Lo siento, aun no puedes votar")
else:
    print("No te creo")   
