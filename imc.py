'''
    IMC
'''
print('CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)')
print('')
peso = float(input('¿Cuánto pesa? '))
altura = float(input('¿Cuánto mide en metros? '))


# *** distintas maneras de calcular imc
imc = peso / altura**2

# imc = peso / pow(altura, 2)

# imc = peso / (altura*altura)

print(f'\nSu imc es {round(imc, 1)}')

print('''\nUn imc muy alto indica obesidad. Los valores \'normales\' de imc están \n
entre 20 y 25, pero esos límites dependen de la edad, del sexo, de la constitución física, etc.''')