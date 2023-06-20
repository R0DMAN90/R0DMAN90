# Ingreso de datos por teclado

# Los datos ingresados deben asignarse a una variable, donde "nombre" sera nuestra variable:

print("Ingrese su nombre")
nombre = input()

# La funcion input() tambien puede mostrar un mensaje de manera opcional:

apellido = input("Ingrese su apellido")

print(nombre,apellido, sep="-")

# La funcion input() siempre que lee algun dato, lo retorna como un "string", incluso aunque sea un numero valido.
# Hay que convertir a numero (float,int) segun corresponda. float = real / int = entero

numero1 = input("Ingrese un numero")
numero2 = input("Ingrese otro numero")

print(numero1 + numero2) # Si hacemos la suma de esta manera, estara concatenando los valores ya que estos son detectados como dato string y no numerico. Hay que convertirlos a numero previa operacion.

numero1 = int(numero1)
numero2 = float(numero2)

print("la suma es: ", numero1 + numero2)