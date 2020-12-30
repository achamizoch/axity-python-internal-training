nombres = input('Capture los nombres separados por comas:').split(',')
tareas = input("Capture el número de tareas faltantes separados por comas:").split(',')
calificaciones = input("Capture las calificaciones separadas por comas:").split(',')
# cadena de mensaje a ser usada para cada estudiante
# NOTA: use .format() con esta cadena en el bucle for
mensaje = "Hola {​​​​​}​​​​​,\n\nEste es un recordatorio de que tiene {​​​​​}​​​​​ tareas por entregar, \
antes de que pueda graduarse. Su calificación actual es {​​​​​}​​​​​ y puede incrementarse \
a {​​​​​}​​​​​ si entrega todas sus tareas antes de la fecha límite.\n\n"
# escriba su código usando un bucle for que itere sobre las listas de nombres, tareas y calificaciones
for i in range(len(nombres)):
    cali_max = int(tareas[i])*2 + int(calificaciones[i])
    print(mensaje.format(nombres[i], tareas[i], calificaciones[i], cali_max))