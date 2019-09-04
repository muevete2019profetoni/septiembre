'''
    NOTAS PARA EL PROFE
    Curso Dual del SOIB
    -------------------
    30% de la nota final, de la suma de los controles
    70% de la nota final en el final
'''

class AlumnosNotas:

    def __init__ (self, nombre, contro01, control02, control03, final):
        alumnos = {
            self.nombre : [self.control01,self.control02,self.control03,self.final]
        }

    def calcular():
        notas = alumnos['alumno01']

        controles = 0
        for i in range(3):
            controles += notas[i]
        controles = (controles/3) * 0.3

        final = (notas[3] * 0.7) + controles
        print(final)





alumnos = {
    'alumno01' : [4,4,4,6]
}

notas = alumnos['alumno01']

controles = 0
for i in range(3):
    controles += notas[i]
controles = (controles/3) * 0.3

final = (notas[3] * 0.7) + controles

