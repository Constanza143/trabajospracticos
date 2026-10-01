def mostrar_menu(lista):
    print("Bienvenido estas son las opciones que puede elegir:")
    print(lista)
    opcion=(int(input("Ingrese un numero del 0 al 4 para el valor que desee ver:")))
    print(lista[opcion])
    return opcion