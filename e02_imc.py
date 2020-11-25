nombre = input('cual es tu nombre?\n')

peso = input(f'{nombre}, cual es tu peso?')
peso = float(peso)

altura = input(f'{nombre}, cual es tu altura?')
altura = float(altura)

imc = peso / (altura*altura)


if imc >= 40:
    grado_obesidad = 'obesidad muy severa.'
elif imc >= 35:
    grado_obesidad = 'obesidad severa.'
elif imc >= 30:
    grado_obesidad ='obesidad moderada.'
elif imc >= 25:
    grado_obesidad = 'sobrepeso.'
elif imc >= 10.5:
    grado_obesidad = 'peso saludable.'
elif imc >= 16:
    grado_obesidad = 'delgadez.'
elif imc >= 15:
    grado_obesidad = 'delgadez severa.'
else: 
    grado_obesidad = 'delgadez muy severa.'

resultado = f'{nombre} tu IMC es {imc:.2f}, quiere decir que tu tienes {grado_obesidad}'

print(resultado)