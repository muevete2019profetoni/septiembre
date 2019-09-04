'''
    Guarda la información en disco en Python
    ----------------------------------------
    w (escribir)
    r (leer)
    a (escribir al final)
    r+ (lee y escribe)
'''

nombre = input('Nombre: ')

# Escritura
with open('file.txt', 'a') as f:
    for i in range(5):
        f.write(f'{nombre}\n')
    f.close()

# f = open ('file.txt', 'w')
# f.write(f'{nombre}\n')
# f.close()


# Lectura
# with open('file.txt', 'r') as f:
#     for linea in f:
#         print(linea)
