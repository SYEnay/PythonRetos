#Entradas
edad=int(input("Ingrese su edad: "))
#Operaciones
if edad >=0  and edad <= 12:
    print("Eres un niño")
elif edad > 12 and edad <= 18:
    print("Eres un adolescente")
    print("Aún no puedes votar")
elif edad  > 18 and edad < 60:
     print("Eres un adulto")
     print("Puedes votar")
elif edad >= 60 and edad <= 100:
     print("Eres un adulto mayor")
     print("Puedes votar")
else:
    print("No te creo")   
