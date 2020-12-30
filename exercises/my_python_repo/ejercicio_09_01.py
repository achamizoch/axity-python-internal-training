nombres = input('Capture los nombres separados por comas:').split(',')
tareas = input("Capture el número de tareas faltantes separados por comas:").split(',')
calificaciones = input("Capture las calificaciones separadas por comas:").split(',')
# cadena de mensaje a ser usada para cada estudiante
# NOTA: use .format() con esta cadena en el bucle for
mensaje = "Hola {},\n\nEste es un recordatorio de que tiene {} tareas por entregar, \
antes de que pueda graduarse. Su calificación actual es {} y puede incrementarse \
a {} si entrega todas sus tareas antes de la fecha límite.\n\n"

# escriba su código usando un bucle for que itere sobre las listas de nombres, tareas y calificaciones
for nombre, tarea, calificacion in zip(nombres, tareas, calificaciones):
    print(message.format(nombre, tarea, calificacion, int(calificacion) + int(tarea)*2))
    
    
mensajes=[]
nombres=[]
tareas=[]
calificaciones=[]

numero_estudiantes=int(input("Numero de estudiantes: \n"))

for i in range(numero_estudiantes):

    nombre_estudiante=input("Nombre del estudiante: ")

    nombres.append(nombre_estudiante)

    tareas_faltantes=int(input("Tareas faltantes: "))

    tareas.append(tareas_faltantes)

    calificacion=float(input("Calificacion: \n"))

    calificaciones.append(calificacion)

info=list(zip(tareas,calificaciones))

dict_alumnos=dict(list(zip(nombres,info))) print("\n") for alumno in dict_alumnos.keys():

    mensaje="Hola {​​​​}​​​​, \n\nEste es un recordatorio de que tiene {​​​​}​​​​ tareas por entregar, antes de que pueda graduarse. Su calificación actual es {​​​​}​​​​ y puede incrementarse a {​​​​}​​​​ si entrega todas sus tareas antes de la fecha límite.".format(alumno,dict_alumnos[alumno][0],dict_alumnos[alumno][1],dict_alumnos[alumno][1]+dict_alumnos[alumno][0]*2)

    mensajes.append(mensaje)

    print(mensaje,"\n\n")

[15:54] Leonardo Levi Galicia Amaro
list_nombres = input("Capture los nombres separados por comas: ")list_tareas = input("Capture el número de tareas faltantes separados por comas: ")list_calificaciones = input("Capture las calificaciones separadas por comas: ") nombres = [nombre for nombre in list_nombres.split(", ")]tareas = [tarea for tarea in list_tareas.split(", ")]calificaciones = [calificacion for calificacion in list_calificaciones.split(", ")]mensaje = "Hola {​​​​​}​​​​​,\n\nEste es un recordatorio de que tiene {​​​​​}​​​​​ tareas por entregar, \antes de que pueda graduarse. Su calificación actual es {​​​​​}​​​​​ y puede incrementarse \a {​​​​​}​​​​​ si entrega todas sus tareas antes de la fecha límite.\n\n" for i in range(len(nombres)):    print(mensaje.format(nombres[i], tareas[i], calificaciones[i], int(calificaciones[i]) * 2))

