alumnos = {}
Osasuna = ""
while Osasuna != "3":
    if Osasuna == "1":
        Añadir_alumno = input("Dime tu nombre y apellido")
        Nota_alumno = input("Que nota has sacado?")
        persona = {"Nombre y apellido": Añadir_alumno, "Nota": Nota_alumno}
    if Osasuna == "2":
        print("Lista de alumnos aprobados")
        for a, b in alumnos.items():
            if a["Aprobado"] >= 5:
                print(a,b["Nombre y apellido"])
    if Osasuna == "3":
        print("lista de alumnos")
        for a,b in alumnos.items():
            print (a,b["Nombre y apellido"])

            

