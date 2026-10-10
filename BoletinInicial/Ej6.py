lista = []
while True:
    o = input(
        "Elije una opción:\n"
        "1. Añadir un producto a una lista\n"
        "2. Ver todos los productos\n"
        "3. Eliminar un producto\n"
        "4. Salir\n"
    )
    if o == "1":
        p = input("Dame el nombre del producto: ")
        lista.append(p)
    elif o == "2":
        print("Productos en la lista:")
        for p in lista:
            print(p)
    elif o == "3":
        p = input("Dame el nombre del producto a eliminar: ")
        if p in lista:
            lista.remove(p)
            print(f"{p} ha sido eliminado de la lista")
        else:
            print(f"{p} no se encuentra en la lista")
    elif o == "4":
        exit()
    else:
        print("Opción no válida")