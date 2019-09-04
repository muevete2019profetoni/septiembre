'''
    Teléfono FORMAT
'''
print('Teléfono FORMAT')

# *Introducir un número télefono
telefono = input('Introduce tu número a formatear: ')
pais = input('''
                [esp]España
                [fr]Francia
                [pt]Portugal
                [nl]Holanda ''')

# *prefijos de paises
prefijo = {
    'esp' : 34,
    'fr'  : 33,
    'pt'  : 351,
    'nl'  : 31
}


# *Convertir el texto a cadena
numero = [i for i in telefono]
''' numero = []
for i in telefono:
    numero.append(i)
'''

# *insertar carácteres para cambiar el formato número
numero.insert(0, f'(+{prefijo[pais]})') # *localización
numero.insert(4,'-') # *guión
numero.insert(8,'-') # *guión

# *Cambiar a formato cadena
numero_cadena = ''.join(numero)

# *Cambiar el caracter- por espacios
numero_blanco = numero_cadena.replace('-',' ')

# *Mostrar los dos formatos de teléfono
print(numero_cadena)
print(numero_blanco)

