'''
-------------------------------------------
id - nombre - a_paterno - a_materno - edad
--------------------------------------------
124 - Antonio - chavez - Campos - 26
-------------------------------------------
45 - Dalai - aguirre - jimenez - 26
------------------------------------------
465 - Dilan - Ortiz - Granados - 25
'''

Antonio = {
    'nombre': 'Antonio',
    'a_materno': 'Chavez',
    'a_paterno': 'Campos',
    'edad': '26'
}

Dalai = {
    'nombre': 'Dalai',
    'a_materno': 'Aguirre',
    'a_paterno': 'Jimenez',
    'edad': '30'
}

Dilan = {
    'nombre': 'Dilan',
    'a_materno': 'Ortiz',
    'a_paterno': 'Granados',
}

alumnos = []
alumnos.append(Antonio)
alumnos.append(Dalai)
alumnos.append(Antonio)

print(f'Total alumnos {len(alumnos)}')

alumnos_con_edad = []

for alumno in alumnos:
    edad_alumno = alumno.get('edad')
    if edad_alumno is not None:
        alumnos_con_edad.append(alumno)

for alumno in alumnos_con_edad:
    print(alumno['edad'])
