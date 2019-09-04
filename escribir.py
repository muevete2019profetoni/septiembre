'''
    ESCRIBIR en Disco en Python
'''

nombre = input('Nombre: ')


# Escritura
with open('file.txt', 'a') as f:
    for i in range(5):
        f.write(f'{nombre}\n')
    f.close()

# f = open ('file.txt','w')
# f.write(nombre)
# f.close()



# Lectura
with open('file.txt','r') as f:
    for line in f:
        print(line)
