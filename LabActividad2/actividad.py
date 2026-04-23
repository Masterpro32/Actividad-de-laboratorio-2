def menu():
    print("1. Saludar")
    print("2. Sumar")
    print("3. Es par")
    print("4. Es mayor")

    opcion = input("Elige: ")

    if opcion == "1":
        saludar()

    elif opcion == "2":
        sumar()

    elif opcion == "3":
        esPar()

    elif opcion == "4":
        esMayor()

    else:
        print("Opción inválida")
      
menu()
