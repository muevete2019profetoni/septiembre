def run():

    contactos = []

    class Ficha:

        def __init__(self, nombre, telefono, email):
            self.nombre = nombre
            self.telefono = telefono
            self.email = email

            

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
        '''))

        if command == 'a':
            nombre = str(input('Nombre: '))
            telefono = str(input('Teléfono: '))
            email = str(input('Email: '))

            contactos.append(Ficha)

            print('*************')
            print('Contacto añadido correctamente')
            print('*************')
            print(contactos)

        elif command == 'ac':
            print('actualizar contacto')

        elif command == 'b':
            print('buscar contacto')

        elif command == 'e':
            print('eliminar contacto')

        elif command == 'l':
            print('listar contactos')

        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    run()
