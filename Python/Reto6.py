#Problema: Crea un programa que pueda calcular el área y volumen de una esfera unicamente con su radio
print("¿Sabes sacar el volumen y área de una esfera? \n Yo puedo darte esa información si me das el radio de la esfera")
#VARIABLES
r=float(input("Dame el radio: "))
#OPERACIONES
r2=float(r*r)
r3=float(r*r*r)
pi=float(3.1416)
a=float(4*(pi*r2))
v= float(4*(pi*r3))
#SALIDAS
print("El área de la esfera es: ",a)
print("El volumen de la esfera es: ",v)
