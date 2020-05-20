
# Este es el juego de adivinar un número

import random

intentos = 0

print("Hola! ¿Cómo te llamas?")

miNombre = input()

numero = random.randint(1, 20)

print("Bueno, " + miNombre + ", estoy pensando un número entre 1 y 20. Tienes 6 intentos para adivinar")

while intentos < 6:
    print('Intenta adivinar')
    estimacion = int(input('Dime tu número: '))
    intentos += 1

    if estimacion < numero:
        print("El número es mayor")
    elif estimacion > numero:
        print("El número es menor")
    else:
        break

if estimacion == numero:
    print('Buen trabajo, ' + miNombre + '! ¡Has adivinado mi numero en ' + str(intentos) + ' intentos')

elif estimacion != numero:
    print('Pues no. El número que estaba pensando era ' + str(numero))
    print('Suerte pa´la próxima')
