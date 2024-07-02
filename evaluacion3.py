import os

menu = """
MENU  DE OPCIONES DEL  VETERINARIO
1. Registrar una Mascota
2. Listar a todas las mascotas
3. Imprimir Ficha de Registro
4. Salir del Programa
Dijite una opcion: """




ficha = [
    [], # Especie
    [], # Nombre
    [], # Peso
    [], # Costo de consulta inicial   
    []  # Costo Total 
]


especies = ["Perro", "Gato", "Ave"]


def registrarMascota():
    especie = input("Ingrese la especie [Perro, Gato, Ave]: ")
    if especie not in especie:
        print("La Especie ingresada no es válida. Por favor, seleccione uno de las siguientes especies: especies = Perro, Gato, Ave.")
        return
    nombre = input("Ingrese el nombre de la mascota: ")
    peso = input("Ingrese el peso de la mascota: ")
    costoConsulta = float(input("Ingrese el Costo de la Consulta: "))
    
    # Calcular el impuesto de Salud
    costodeSalud = costoConsulta * 0.05
    costoTotal = costoConsulta + costodeSalud


    # Agregar los datos a la planilla
    ficha[0].append(especie)
    ficha[1].append(nombre)
    ficha[2].append(peso)
    ficha[3].append(costoConsulta)
    ficha[4].append(round(costoTotal, 1))

    
    print("Mascota Registrada Con exito!.")







def listadeMascotas():
    if not ficha[0]:
        print("No se encuentra ninguna mascota registrada.")
    else:
        print("Lista de las Mascotas:")
        print("Especie          Nombre          Peso         Costo de Consulta Inicial         Costo Total a Pagar")
        for i in range(len(ficha[0])):
            print(f"{ficha[0][i]}      {ficha[1][i]}            {ficha[2][i]}kg             {ficha[3][i]}             {ficha[4][i]}")
            


def imprimirFicha():
    if not ficha[0]:
        print("No hay Mascotas registrados.")
        return
    
    print("Seleccione una opción para imprimir la Ficha:")
    print("1. Imprimir ficha de todas las mascotas")
    for i, especies in enumerate(especies, start=2):
        print(f"{i}. Imprimir ficha solo de {especies}s")
    
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        filename = "ficha_general.txt"
    else:
        cargo = especies[opcion - 2]
        filename = f"ficha_{especies.lower()}s.txt"
    
    with open(filename, "w", encoding="UTF-8") as file:
        file.write("Ficha de Mascotas\n")
        file.write("Especie           Nombre          Peso         Costo de Consulta Inical         Costo Total a Pagar\n")
        
        if opcion == 1:
            for i in range(len(ficha[0])):
                file.write(f"{ficha[0][i]}      {ficha[1][i]}            {ficha[2][i]}             {ficha[3][i]}             {ficha[4][i]}\n")
        else:
            for i in range(len(ficha[0])):
                if ficha[1][i] == especies:
                    file.write(f"{ficha[0][i]}      {ficha[1][i]}            {ficha[2][i]}             {ficha[3][i]}             {ficha[4][i]}\n")
    
    print(f"Ficha guardada Nombre del archivo: {filename}.")

while True:
    try:
        opc = int(input(menu))
        if opc == 4:
            break
        elif opc == 1: 
            registrarMascota() 
            input("\Precione enter para volver al menu principal")
        elif opc == 2:
            listadeMascotas() 
            input("\Precione enter para volver al menu principal")
        elif opc == 3: 
            imprimirFicha()
            input("\Precione enter para volver al menu principal")
    except:
        print("La opcion que selecciono no es valida, solo opciones del 1 al 4.")

print("¡Muchas gracias por venir, Hasta luego!")