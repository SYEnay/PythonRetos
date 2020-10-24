#Este bot está diseñado para hacer mas concientes a las personas sobre el cuidado
#de los animales y las responsabilidades de los dueños de mascotas.
#Inicio
print("¡Hola! Soy Canbot y quiero aprender de ti.") 
nombre= input("¿Puedes decirme tu nombre? ")
ciclo=True
while ciclo==True:
    edad= int(input("¿Cúantos años tienes? "))    
    if (edad >= 18) and (edad <= 100):
        print("¡Genial! Debes saber mucho")
        #INTRODUCCIÓN
        print("Mira yo trato de aprender cada día más sobre tu mundo y por ahora investigo sobre la relación de los humanos y los animales.")
        print("Quiero saber mucho de los animales y saber ¿cuál es la manera adecuada de cuidarlos? Y sobre todo la responsabilidad de tener una mascota.")
        ciclo2=True
        while ciclo2==True:
            ayuda=input("¿Me ayudarías? Si / No \n")
            if ayuda=="si" or ayuda=="Sí" or ayuda=="Si" or ayuda=="Yes" or ayuda=="sip" or ayuda=="yep" or ayuda=="Sip":
                print ("!Empecemos entonces!")
        #Preguntas del Tema
        #Pregunta para saber el interes en el tema
                ciclo3=True
                while ciclo3==True:
                    gustar=input("Primero que nada, ¿a tí gustan los animales? Si / No \n")
                    if gustar=="si" or gustar=="Sí" or gustar=="Si" or gustar=="Yes" or gustar=="sip" or gustar=="yep" or gustar=="Sip":
                        print ("Debes saber mucho sobre el tema")
        #Preguntas de conocimiento del tema
        #Pregunta animal
                        print("Ahora dime por favor", nombre)
                        es_animal=input("¿Para ti que es un animal? ")
                        define_animal=str("es un ser vivo que respira y siente como los humanos, \n tal vez no hable pero tiene necesidades como comer, cubrirse del frío, ir al baño, dormir e incluso sentir cariño.")
                        print("Sabes: yo investigue un poco en línea y encontré que un animal ", define_animal)
                        ciclo4=True
                        while ciclo4==True:
                            es_cierto=input("¿Crees que esto es verdad? Si / No \n")
                            if es_cierto=="si" or es_cierto=="Sí" or es_cierto=="Si" or es_cierto=="Yes" or es_cierto=="sip" or es_cierto=="yep" or es_cierto=="Sip":
                                print ("Gracias ahora se que lo que tengo en mi base de datos no esta mal")
            #Pregunta mascota 
                                es_cierto=input("Oye y tu ¿Sabes que es una mascota? Me dijo un amigo que son animales domésticos que pueden convivir con los humanos. \n Y que ambos se acompañan y se quieren mucho. Por favor dime para ti que son. \n")
                                ciclo5=True
                                while ciclo5==True:
                                    define_mascota=input("¿Tienes mascotas o alguien que conozcas tiene una? Si / No \n")
                                    if define_mascota=="si" or define_mascota=="Sí" or define_mascota=="Si" or define_mascota=="Yes" or define_mascota=="sip" or define_mascota=="yep" or define_mascota=="Sip":
                                        print ("Gracias por contestar")
                                        print(nombre) 
                                        actividades=input("¿podrías decirme que haces o hacen los dueños de una mascota? ")
                                        print("Entonces los dueños de las mascotas deben tener muchas responsabilidades.")
                                        #Conclusiones
                                        print("Con tus respuestas puedo decir que:")
                                        print("1) Un animal ", define_animal," que esta información es ", es_cierto ," y además", es_animal)
                                        print("2) También que para ti una mascota es ", define_mascota)
                                        print("3) Que los dueños de los animales: ", actividades)
                                        print("Y entiendo que tener una mascota, es una decisión que implica ciertas obligaciones para cubrir sus necesidades básicas de comida y ")
                                        print("el cuidado de su salud, tanto físico y como emocional. ")
                                        #Despedida
                                        print("Muchas Gracias!")
                                        print("Con tu ayuda ahora se más sobre los animales y las mascotas.")
                                        print("Solo te encargo una misión más ",nombre,", por favor.")
                                        print("¡Cuida y respeta mucho a todos los animales que te rodean!")
                                        print("Si llegas a ver que los lastiman por favor avisa a tus padres o a un policía. Ellos sabrán que hacer")
                                        print("Adiós ",nombre," cuídate mucho.")
                                        ciclo5=False
                                        ciclo4=False
                                        ciclo3=False
                                        ciclo2=False
                                        ciclo=False
                                        
                                    elif define_mascota=="Nop" or define_mascota=="no" or define_mascota=="No" or define_mascota=="Not" or define_mascota=="nop" or define_mascota=="yep" or define_mascota=="nop":
                                        print ("¡ya veo! deberías tener una")
                                        print(nombre) 
                                        actividades=input("¿podrías decirme que haces o hacen los dueños de una mascota? ")
                                        print("Entonces los dueños de las mascotas deben tener muchas responsabilidades.")
                                        #Conclusiones
                                        print("Con tus respuestas puedo decir que:")
                                        print("1) Un animal ", define_animal," que esta información es ", es_cierto ," y además", es_animal)
                                        print("2) También que para ti una mascota es ", define_mascota)
                                        print("3) Que los dueños de los animales: ", actividades)
                                        print("Y entiendo que tener una mascota, es una decisión que implica ciertas obligaciones para cubrir sus necesidades básicas de comida y ")
                                        print("el cuidado de su salud, tanto físico y como emocional. ")
                                        #Despedida
                                        print("Muchas Gracias!")
                                        print("Con tu ayuda ahora se más sobre los animales y las mascotas.")
                                        print("Solo te encargo una misión más ",nombre,", por favor.")
                                        print("¡Cuida y respeta mucho a todos los animales que te rodean!")
                                        print("Si llegas a ver que los lastiman por favor avisa a tus padres o a un policía. Ellos sabrán que hacer")
                                        print("Adiós ",nombre," cuídate mucho.")
                                        ciclo5=False
                                        ciclo4=False
                                        ciclo3=False
                                        ciclo2=False
                                        ciclo=False
                                        
                                    else:
                                        print("Lo siento no te entiendo... ¿Si o No?")
                            elif es_cierto=="Nop" or es_cierto=="no" or es_cierto=="No" or es_cierto=="Not" or es_cierto=="nop" or es_cierto=="yep" or es_cierto=="nop":
                                print ("Gracias, seguire investigando más.")
                                ciclo4=False
                                ciclo3=False
                                ciclo2=False
                                ciclo=False
                            else:
                                print("Lo siento no te entiendo... ¿Si o No?")
                        else:   
                            ciclo4=False
                            ciclo3=False
                            ciclo2=False
                            ciclo=False
                    elif gustar=="Nop" or gustar=="no" or gustar=="No" or gustar=="Not" or gustar=="nop" or gustar=="yep" or gustar=="nop":
                        no_gustar=input("¿Por qué no te gustan? \n")
                        print ("Supongo que puede suceder, pero espero que los respetes, sé que tú los ayudaras aunque no te gusten, así como me ayudas a mí :).")
         #Preguntas de conocimiento del tema
         #Pregunta animal
                        print("Ahora dime por favor", nombre)
                        es_animal=input("¿Para ti que es un animal? ")
                        define_animal=str("es un ser vivo que respira y siente como los humanos, \n tal vez no hable pero tiene necesidades como comer, cubrirse del frío, ir al baño, dormir e incluso sentir cariño.")
                        print("Sabes: yo investigue un poco en línea y encontré que un animal ", define_animal)
                        ciclo4=True
                        while ciclo4==True:
                            es_cierto=input("¿Crees que esto es verdad? Si / No \n")
                            if es_cierto=="si" or es_cierto=="Sí" or es_cierto=="Si" or es_cierto=="Yes" or es_cierto=="sip" or es_cierto=="yep" or es_cierto=="Sip":
                                print ("Gracias ahora se que lo que tengo en mi base de datos no esta mal")
                #Pregunta mascota 
                                es_cierto=input("Oye y tu ¿Sabes que es una mascota? Me dijo un amigo que son animales domésticos que pueden convivir con los humanos. \n Y que ambos se acompañan y se quieren mucho. Por favor dime para ti que son. \n")
                                ciclo5=True
                                while ciclo5==True:
                                    define_mascota=input("¿Tienes mascotas o alguien que conozcas tiene una? Si / No \n")
                                    if define_mascota=="si" or define_mascota=="Sí" or define_mascota=="Si" or define_mascota=="Yes" or define_mascota=="sip" or define_mascota=="yep" or define_mascota=="Sip":
                                        print ("Gracias por contestar")
                                        ciclo5=False
                                    elif define_mascota=="Nop" or define_mascota=="no" or define_mascota=="No" or define_mascota=="Not" or define_mascota=="nop" or define_mascota=="yep" or define_mascota=="nop":
                                        print ("¡ya veo! deberías tener una")
                                        ciclo5=False
                                    else:
                                        print("Lo siento no te entiendo... ¿Si o No?")
                                print(nombre) 
                                actividades=input("¿podrías decirme que haces o hacen los dueños de una mascota? ")
                                print("Entonces los dueños de las mascotas deben tener muchas responsabilidades.")
                                #Conclusiones
                                subprocess.call (["cmd.exe","/C","cls"])
                                print("Con tus respuestas puedo decir que:")
                                print("1) Un animal ", define_animal," que esta información es ", es_cierto ," y además", es_animal)
                                print("2) También que para ti una mascota es ", define_mascota)
                                print("3) Que los dueños de los animales: ", actividades)
                                print("Y entiendo que tener una mascota, es una decisión que implica ciertas obligaciones para cubrir sus necesidades básicas de comida y ")
                                print("el cuidado de su salud, tanto físico y como emocional. ")
                                #Despedida
                                print("Muchas Gracias!")
                                print("Con tu ayuda ahora se más sobre los animales y las mascotas.")
                                print("Solo te encargo una misión más ",nombre,", por favor.")
                                print("¡Cuida y respeta mucho a todos los animales que te rodean!")
                                print("Si llegas a ver que los lastiman por favor avisa a tus padres o a un policía. Ellos sabrán que hacer")
                                print("Adiós ",nombre," cuídate mucho.")
                                #Aqui termino
                                ciclo4=False
                                ciclo3=False
                                ciclo2=False
                                ciclo=False
                            elif es_cierto=="Nop" or es_cierto=="no" or es_cierto=="No" or es_cierto=="Not" or es_cierto=="nop" or es_cierto=="yep" or es_cierto=="nop":
                                print ("Gracias, seguire investigando más.")
                                ciclo4=False
                                ciclo3=False
                                ciclo2=False
                                ciclo=False
                            else:
                                print("Lo siento no te entiendo... ¿Si o No?")
                        else:   
                            ciclo4=False
                            ciclo3=False
                            ciclo2=False
                            ciclo=False
                    else:
                        print("Lo siento no te entiendo... ¿Si o No? ")
                        ciclo2=False
            elif ayuda=="Nop" or ayuda=="no" or ayuda=="No" or ayuda=="Not" or ayuda=="nop" or ayuda=="yep" or ayuda=="nop":
                print ("Ok, muchas gracias, adiós")
                ciclo2=False
            else:
                print("Lo siento no te entiendo...")
        else: 
            ciclo=False
    elif  (edad >= 3) and (edad < 18):
        print("Aprenderemos juntos")
        #INTRODUCCIÓN
        print("Mira yo trato de aprender cada día más sobre tu mundo y por ahora investigo sobre la relación de los humanos y los animales.")
        print("Quiero saber mucho de los animales y saber ¿cuál es la manera adecuada de cuidarlos? Y sobre todo la responsabilidad de tener una mascota.")
        ciclo2=True
        while ciclo2==True:
            ayuda=input("¿Me ayudarías? Si / No \n")
            if ayuda=="si" or ayuda=="Sí" or ayuda=="Si" or ayuda=="Yes" or ayuda=="sip" or ayuda=="yep" or ayuda=="Sip":
                print ("!Empecemos entonces!")
            #Preguntas del Tema
            #Pregunta para saber el interes en el tema
                ciclo3=True
                while ciclo3==True:
                    gustar=input("Primero que nada, ¿a tí gustan los animales? Si / No \n")
                    if gustar=="si" or gustar=="Sí" or gustar=="Si" or gustar=="Yes" or gustar=="sip" or gustar=="yep" or gustar=="Sip":
                        print ("Debes saber mucho sobre el tema")
                #Preguntas de conocimiento del tema
                #Pregunta animal
                        print("Ahora dime por favor", nombre)
                        es_animal=input("¿Para ti que es un animal? ")
                        define_animal=str("es un ser vivo que respira y siente como los humanos, \n tal vez no hable pero tiene necesidades como comer, cubrirse del frío, ir al baño, dormir e incluso sentir cariño.")
                        print("Sabes: yo investigue un poco en línea y encontré que un animal ", define_animal)
                        ciclo4=True
                        while ciclo4==True:
                            es_cierto=input("¿Crees que esto es verdad? Si / No \n")
                            if es_cierto=="si" or es_cierto=="Sí" or es_cierto=="Si" or es_cierto=="Yes" or es_cierto=="sip" or es_cierto=="yep" or es_cierto=="Sip":
                                print ("Gracias ahora se que lo que tengo en mi base de datos no esta mal")
                        #Pregunta mascota 
                                es_cierto=input("Oye y tu ¿Sabes que es una mascota? Me dijo un amigo que son animales domésticos que pueden convivir con los humanos. \n Y que ambos se acompañan y se quieren mucho. Por favor dime para ti que son. \n")
                                ciclo5=True
                                while ciclo5==True:
                                    define_mascota=input("¿Tienes mascotas o alguien que conozcas tiene una? Si / No \n")
                                    if define_mascota=="si" or define_mascota=="Sí" or define_mascota=="Si" or define_mascota=="Yes" or define_mascota=="sip" or define_mascota=="yep" or define_mascota=="Sip":
                                        print ("Gracias por contestar")
                                        print(nombre) 
                                        actividades=input("¿podrías decirme que haces o hacen los dueños de una mascota? ")
                                        print("Entonces los dueños de las mascotas deben tener muchas responsabilidades.")
                                        #Conclusiones
                                        print("Con tus respuestas puedo decir que:")
                                        print("1) Un animal ", define_animal," que esta información es ", es_cierto ," y además", es_animal)
                                        print("2) También que para ti una mascota es ", define_mascota)
                                        print("3) Que los dueños de los animales: ", actividades)
                                        print("Y entiendo que tener una mascota, es una decisión que implica ciertas obligaciones para cubrir sus necesidades básicas de comida y ")
                                        print("el cuidado de su salud, tanto físico y como emocional. ")
                                        #Despedida
                                        print("Muchas Gracias!")
                                        print("Con tu ayuda ahora se más sobre los animales y las mascotas.")
                                        print("Solo te encargo una misión más ",nombre,", por favor.")
                                        print("¡Cuida y respeta mucho a todos los animales que te rodean!")
                                        print("Si llegas a ver que los lastiman por favor avisa a tus padres o a un policía. Ellos sabrán que hacer")
                                        print("Adiós ",nombre," cuídate mucho.")
                                        ciclo5=False
                                        ciclo4=False
                                        ciclo3=False
                                        ciclo2=False
                                        ciclo=False
                                        
                                    elif define_mascota=="Nop" or define_mascota=="no" or define_mascota=="No" or define_mascota=="Not" or define_mascota=="nop" or define_mascota=="yep" or define_mascota=="nop":
                                        print ("¡ya veo! deberías tener una")
                                        print(nombre) 
                                        actividades=input("¿podrías decirme que haces o hacen los dueños de una mascota? ")
                                        print("Entonces los dueños de las mascotas deben tener muchas responsabilidades.")
                                        #Conclusiones
                                        print("Con tus respuestas puedo decir que:")
                                        print("1) Un animal ", define_animal," que esta información es ", es_cierto ," y además", es_animal)
                                        print("2) También que para ti una mascota es ", define_mascota)
                                        print("3) Que los dueños de los animales: ", actividades)
                                        print("Y entiendo que tener una mascota, es una decisión que implica ciertas obligaciones para cubrir sus necesidades básicas de comida y ")
                                        print("el cuidado de su salud, tanto físico y como emocional. ")
                                        #Despedida
                                        print("Muchas Gracias!")
                                        print("Con tu ayuda ahora se más sobre los animales y las mascotas.")
                                        print("Solo te encargo una misión más ",nombre,", por favor.")
                                        print("¡Cuida y respeta mucho a todos los animales que te rodean!")
                                        print("Si llegas a ver que los lastiman por favor avisa a tus padres o a un policía. Ellos sabrán que hacer")
                                        print("Adiós ",nombre," cuídate mucho.")
                                        ciclo5=False
                                        ciclo4=False
                                        ciclo3=False
                                        ciclo2=False
                                        ciclo=False
                                        
                                    else:
                                        print("Lo siento no te entiendo... ¿Si o No?")
                            elif es_cierto=="Nop" or es_cierto=="no" or es_cierto=="No" or es_cierto=="Not" or es_cierto=="nop" or es_cierto=="yep" or es_cierto=="nop":
                                print ("Gracias, seguire investigando más.")
                                ciclo4=False
                                ciclo3=False
                                ciclo2=False
                                ciclo=False
                            else:
                                print("Lo siento no te entiendo... ¿Si o No?")
                        else:   
                            ciclo4=False
                            ciclo3=False
                            ciclo2=False
                            ciclo=False
                    elif gustar=="Nop" or gustar=="no" or gustar=="No" or gustar=="Not" or gustar=="nop" or gustar=="yep" or gustar=="nop":
                        no_gustar=input("¿Por qué no te gustan? \n")
                        print ("Supongo que puede suceder, pero espero que los respetes, sé que tú los ayudaras aunque no te gusten, así como me ayudas a mí :).")
                #Preguntas de conocimiento del tema
                #Pregunta animal
                        print("Ahora dime por favor", nombre)
                        es_animal=input("¿Para ti que es un animal? ")
                        define_animal=str("es un ser vivo que respira y siente como los humanos, \n tal vez no hable pero tiene necesidades como comer, cubrirse del frío, ir al baño, dormir e incluso sentir cariño.")
                        print("Sabes: yo investigue un poco en línea y encontré que un animal ", define_animal)
                        ciclo4=True
                        while ciclo4==True:
                            es_cierto=input("¿Crees que esto es verdad? Si / No \n")
                            if es_cierto=="si" or es_cierto=="Sí" or es_cierto=="Si" or es_cierto=="Yes" or es_cierto=="sip" or es_cierto=="yep" or es_cierto=="Sip":
                                print ("Gracias ahora se que lo que tengo en mi base de datos no esta mal")
                    #Pregunta mascota 
                                es_cierto=input("Oye y tu ¿Sabes que es una mascota? Me dijo un amigo que son animales domésticos que pueden convivir con los humanos. \n Y que ambos se acompañan y se quieren mucho. Por favor dime para ti que son. \n")
                                ciclo5=True
                                while ciclo5==True:
                                    define_mascota=input("¿Tienes mascotas o alguien que conozcas tiene una? Si / No \n")
                                    if define_mascota=="si" or define_mascota=="Sí" or define_mascota=="Si" or define_mascota=="Yes" or define_mascota=="sip" or define_mascota=="yep" or define_mascota=="Sip":
                                        print ("Gracias por contestar")
                                        ciclo5=False
                                    elif define_mascota=="Nop" or define_mascota=="no" or define_mascota=="No" or define_mascota=="Not" or define_mascota=="nop" or define_mascota=="yep" or define_mascota=="nop":
                                        print ("¡ya veo! deberías tener una")
                                        ciclo5=False
                                    else:
                                        print("Lo siento no te entiendo... ¿Si o No?")
                                print(nombre) 
                                actividades=input("¿podrías decirme que haces o hacen los dueños de una mascota? ")
                                print("Entonces los dueños de las mascotas deben tener muchas responsabilidades.")
                                #Conclusiones
                                subprocess.call (["cmd.exe","/C","cls"])
                                print("Con tus respuestas puedo decir que:")
                                print("1) Un animal ", define_animal," que esta información es ", es_cierto ," y además", es_animal)
                                print("2) También que para ti una mascota es ", define_mascota)
                                print("3) Que los dueños de los animales: ", actividades)
                                print("Y entiendo que tener una mascota, es una decisión que implica ciertas obligaciones para cubrir sus necesidades básicas de comida y ")
                                print("el cuidado de su salud, tanto físico y como emocional. ")
                                #Despedida
                                print("Muchas Gracias!")
                                print("Con tu ayuda ahora se más sobre los animales y las mascotas.")
                                print("Solo te encargo una misión más ",nombre,", por favor.")
                                print("¡Cuida y respeta mucho a todos los animales que te rodean!")
                                print("Si llegas a ver que los lastiman por favor avisa a tus padres o a un policía. Ellos sabrán que hacer")
                                print("Adiós ",nombre," cuídate mucho.")
                                #Aqui termino
                                ciclo4=False
                                ciclo3=False
                                ciclo2=False
                                ciclo=False
                            elif es_cierto=="Nop" or es_cierto=="no" or es_cierto=="No" or es_cierto=="Not" or es_cierto=="nop" or es_cierto=="yep" or es_cierto=="nop":
                                print ("Gracias, seguire investigando más.")
                                ciclo4=False
                                ciclo3=False
                                ciclo2=False
                                ciclo=False
                            else:
                                print("Lo siento no te entiendo... ¿Si o No?")
                        else:   
                            ciclo4=False
                            ciclo3=False
                            ciclo2=False
                            ciclo=False
                    else:
                        print("Lo siento no te entiendo... ¿Si o No? ")
                        ciclo2=False
            elif ayuda=="Nop" or ayuda=="no" or ayuda=="No" or ayuda=="Not" or ayuda=="nop" or ayuda=="yep" or ayuda=="nop":
                print ("Ok, muchas gracias, adiós")
                ciclo2=False
            else:
                print("Lo siento no te entiendo...")
        else: 
            ciclo=False
    else: 
        print("No te creo")
else:
    print("Vuelve pronto")

