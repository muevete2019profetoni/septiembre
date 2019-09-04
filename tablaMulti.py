'''
    TABLA DE MÚLTIPLICAR
'''
# *Pedir dato entero
print('TABLA DE MÚLTIPLICAR \n')
tabla = int(input('Tabla de multiplicar ')) 

# *la variable del for tomará el valor de cada elemento
for i in [1,2,3,4,5,6,7,8,9,10]:
    # *Realizar y mostrar resultado 
    print(f'{tabla} * {i} = {i * tabla}')
