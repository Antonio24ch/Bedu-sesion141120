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
    'edad': '26'
}

Dilan = {
    'nombre': 'Dilan',
    'a_materno': 'Ortiz',
    'a_paterno': 'Granados',

}

print(Dilan.get('edad')) #para valores que no existen el el objeto
# print(Dilan.get('edad', '100')) # si no encuentra el valor de edad, me da 100