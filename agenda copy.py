'''
    AGENDA 2019/2020
    ----------------
    nombre / teléfono / email
'''

# ****************** CLASES
# *************************
class Ficha:
    
    def __init__ (self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email


class Agenda:
    
# ********** Contructor
    def __init__ (self):
        self._contactos = []

# ********** Métodos
    # Añadir contacto
    def nuevo(self, name, phone, email):
        contacto = Ficha(name, phone, email)
        self._contactos.append(contacto)

        print('''
        >>>
        \tContacto Añadido Correctamente
        ''')
    # Mostrar todos los contactos
    def mostrar_todo(self):
        for contacto in self._contactos:
            self._mostrar(contacto)

        print('''
        >>>
        \tMostrados todos los Contactos
        ''')  

    # Formato de contacto para el método mostrar
    def _mostrar(self, contacto):
        print('---*---*---*---*---*---*---*---*---*---')
        print('Nombre: {}'.format(contacto.name))
        print('Teléfono: {}'.format(contacto.phone))
        print('Email: {}'.format(contacto.email))
        print('---*---*---*---*---*---*---*---*---*---')

    # Borrar contacto
    def borrar(self, name):
        for index, contacto in enumerate(self._contactos):
            if contacto.name.lower() == name.lower():
                del self._contactos[index]
                break

        print('''
        >>>
        \tContacto Borrado
        ''')   

    # Buscar contacto
    def buscar(self, name):
        for contacto in self._contactos:
            if contacto.name.lower() == name.lower():
                self._mostrar(contacto)
                break
        else:
            self._no_encontrado()

        print('''
        >>>
        \tBusqueda Finalizada con Éxito
        ''')   

    # Actualizar contacto
    def actualizar(self, name, phone, email):
        for contacto in self._contactos:
            if contacto.name.lower() == name.lower():
                contacto.phone = phone
                contacto.email = email
                break
        else:
            self._no_encontrado()

        print('''
        >>>
        \tContacto Actualizado con Éxito
        ''') 
        
    # Formato para cuando no se encuentra un contacto
    def _no_encontrado(self):
        print('***********')
        print('¡No encontrado!')
        print('***********')




# ****************** FUNCIONES
# *************************

def run():

    # * Creamos un objeto llamado agenda_de_Toni
    agenda_de_Toni = Agenda()

    # *Menu de la Agenda
    while True:
        menu = input('''
        ¿Qué deseas hacer?

        [a]ñadir contacto
        [ac]ualizar contacto
        [b]uscar contacto
        [e]liminar contacto
        [l]istar contactos
        [s]alir
        ''')

        if menu == 'a':
            # Se le piden los datos de contacto
            name = input('Escribe el nombre del contacto')
            phone = input('Escribe el telefono del contacto')
            email = input('Escribe el email del contacto')
            # Se llama al método de añadir contacto
            agenda_de_Toni.nuevo(name, phone, email)
            
        elif menu == 'ac':
            pass
        elif menu == 'b':
            pass
        elif menu == 'e':
            pass
        elif menu == 'l':
            pass
        elif menu == 's':
            break
        else:
            print('Prueba otra vez!')

# *Inicio
if __name__ == "__main__":
    run()
        