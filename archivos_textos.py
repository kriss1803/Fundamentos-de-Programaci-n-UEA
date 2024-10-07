#Tarea: Trabajo con Archivos de Texto en Python

#Crea un nuevo archivo llamado my_notes.txt.
archivo = open('my_notes.txt', 'w') #Se crea en modo escritura

#Escritura de al menos tres líneas de  notas personales en  el archivo.
archivo.write("Estudiar programación para el examen.\n")
archivo.write("Dar el examen el lunes 7 de octubre.\n")
archivo.write("Revisar las notas al finalizar la semana.\n")

#Abrir el archivo my_notes.txt. en modo lectura
archivo = open('my_notes.txt', 'r')

#Lee el contenido del archivo línea por línea utilizando el readline
archivo.seek(0)
linea1=archivo.readline()
linea2=archivo.readline()
linea3=archivo.readline()

#Imprimir en pantalla el contenido de cada línea
print("Mis Notas Personales:\n")
print(linea1.strip())
print(linea2.strip())
print(linea3.strip())

#Muestra en la consola cada línea leída.
archivo.close()


