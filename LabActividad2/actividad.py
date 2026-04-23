def sumar(a, b):
    return a + b

def menu():
    #Menú por Diego
    print("1. Saludar")
    print("2. Sumar")
    print("3. Es par")
    print("4. Es mayor")

    opcion = input("Elige: ")

    if opcion == "1":
        #Saludar por Jeanpier
        def saludar(nombre):
            print("Hola,", nombre)
        nombre = input("Escribe tu nombre: ")
        saludar(nombre)

    elif opcion == "2":
        #Suma por Haziel
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))

        resultado = sumar(num1, num2)
        print("La suma es:", resultado)

    elif opcion == "3":
        #Par por Neda Victoria
        def esPar(num):
            if num % 2 == 0:
                return "Verdadero(Es par)"
            else:
                return "Falso(Es impar)"

        numero = int(input("Introduce un número: "))
        print(esPar(numero))

    elif opcion == "4":
        #Mayor por Harol
        def esMayor(edad):
            if edad >= 18:
                return "Verdadero(Es mayor de edad)"
            else:
                return "Falso(Es menor de edad)"

        edad = int(input("Introduce tu edad: "))
        print(esMayor(edad))

    else:
        print("Opción inválida")
      
menu()


