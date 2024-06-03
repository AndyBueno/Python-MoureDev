#Todo sobre variables

mensaje = 'Esta es una variable de tipo str'
print(mensaje)

#nomenclatura de variables
mi_variable = 'Convencion de variable snake_case'
miVariable = 'Convencion de variable lowerCamelCase'
MiVariable = 'Convencion de variable UpperCamelCase'
MI_VARIABLE = 'Convencion de variable SCREAMING_SNAKE_CASE'

print(mi_variable)
print(miVariable)
print(MiVariable)
print(MI_VARIABLE)

'''
    Para declarar una variable solo hace falta 
    escribir el nombre que tendra la variable, respentando las 
    diferentes convenciones, seguido de agregar el valor a la 
    variable, segun sea lo necesario para su funcionamiento.
'''

mensaje = 'Im Andy, Im '
numEjemplo = 28
mensaje2 = 'Years Old'
#La funcion Print() puede recibir varios argumentos
print(mensaje, numEjemplo, mensaje2)
#De esta manera se puede concatenar diferentes variables en una cadena


#Funciones del sistema
print('Este es el tamaño de la variable mensaje2: ', len(mensaje2))

#variables de una sola linea, ¡No abusar de esta sintaxis!
name, surname, alias, age = 'Andres', 'Bueno', 'Andy', 28 #se declaran las variables y se establece el valor de las mismas respetando el orden en el que fueron declaradas.
print('Mi nombre es', name, surname, 'Me dicen', alias, 'Y tengo', age, 'Años') #Concatenacion de variables en una cadena de texto


