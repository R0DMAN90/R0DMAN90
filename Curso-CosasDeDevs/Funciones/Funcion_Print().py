# Comentar linea
"""Comentario por bloque de codigo"""

# Mostrar por pantalla con la funcion print()

print("Este es un mensaje aleatorio en python")
print("Este es un mensaje")
print("Aleatorio en python")

# La funcion Print puede recibir diferentes parametros, "end" por ejemplo
# El parametro "end" hace que las diferentes lineas de print queden en el mismo renglon separadas, por defecto por un espacio.

print("Este es un mensaje aleatorio en python", end=" ")
print("Este es un mensaje", end=" - ")
print("Aleatorio en python", end=" * ")

# Existe otro parametro llamado "sep".
# Este permite indicar como queremos separar los diferentes valores que le pasamos a print(), por defecto es un espacio en blanco.
# Utilizando el ejemplo anterior:

print("Este es un mensaje aleatorio en python", "prueba1", end="    ")#Al final del texto agrega una separacion segun se configure el "end", 2 espacios y 1 tabulación en este caso y concatena la funcion print actual y la siguiente en el mismo renglon. 
print("Este es un mensaje aleatorio en python", "prueba2", sep=" / ")#Esto separa los diferentes parametros por "comas"
print("Este es un mensaje aleatorio en python", "prueba3", sep="/", end="  ")#----  PRUEBA 3 Y 4 SON IGUALES.
print("Este es un mensaje aleatorio en python", "prueba4",end="  ", sep="/" )#----  PRUEBA 3 Y 4 SON IGUALES. El orden de los parametros no afecta el resultado. (Si junta el renglon del print siguiente al anterior)
print(" ")
print("Este es un mensaje aleatorio en python", "prueba5", sep="$")

# La funcion print() tambien admite operaciones basicas, por ejemplo una suma:

print("El resultado de la suma es: ", 10 + 10)
