notas = {}
while True:
    o = input(
        "Elije una opción:\n"
        "1. Añadir un alumno con su nota\n"
        "2. Buscar la nota de un alumno\n"
        "3. Calcular la nota media de todos los alumnos\n"
        "4. Mostrar quien tiene la nota más alta\n"
        "5. Salir\n"
    )
    if o == "1":
        a = input("Dame el nombre del alumno: ")
        n = float(input("Dame la nota del alumno: "))
        notas[a] = n
    elif o == "2":
        a = input("Dame el nombre del alumno: ")
        if a in notas:
            print(f"La nota de {a} es {notas[a]}")
        else:
            print(f"{a} no se encuentra en la lista")
    elif o == "3":
        if notas:
            print(f"La nota media de todos los alumnos es {sum(notas.values()) / len(notas.values())}")
        else:
            print("No hay alumnos en la lista")
    elif o == "4":
        if notas:
            print(f"La nota más alta es {max(notas.values())} y pertenece a {max(notas, key=lambda alumno: notas[alumno])}")
        else:
            print("No hay alumnos en la lista")
    elif o == "5":
        exit()
    else:
        print("Opción no válida")