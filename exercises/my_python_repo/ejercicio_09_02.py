def planea_fiesta(bocadillos, personas):
    sobrantes = None
    por_persona = None

    # agregar el código para manejar las excepciones


    return(por_persona, sobrantes)

# no modificar este bloque de código
seguir_fiesta = 's'
while seguir_fiesta == 's':

    bocadillos = int(input("¿Cuántos bocadillos está preparando? "))
    personas = int(input("¿Cuántas personas van a asistir? "))

    por_persona, sobrantes = planea_fiesta(bocadillos, personas)

    if por_persona:  # si por_persona no es None
        mensaje = "\n¡Hagamos fiesta! Tendremos {} invitados, cada uno tendrá {} bocadillos y sobrarán {}."
        print(mensaje.format(personas, por_persona, sobrantes))

    seguir_fiesta = input("\n¿Desea continuar la fiesta? (s o n) ")
