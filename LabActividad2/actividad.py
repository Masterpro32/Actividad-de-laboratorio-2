def menu():
    print("1. Saludar")
    print("2. Sumar")
    print("3. Es par")
    print("4. Es mayor")

    opcion = input("Elige: ")

    if opcion == "1":
        def saludar(nombre):
            print("Hola,", nombre)
        nombre = input("Escribe tu nombre: ")
        saludar(nombre)

    elif opcion == "2":
        sumar()

    elif opcion == "3":
#par(Neda Victoria Merino)
def esPar(num):
    if num % 2 == 0:
        return "Verdadero(Es par)"
    else:
        return "Falso(Es impar)"

numero = int(input("Introduce un número: "))
print(esPar(numero))

    elif opcion == "4":
        esMayor()

    else:
        print("Opción inválida")
      
menu()




