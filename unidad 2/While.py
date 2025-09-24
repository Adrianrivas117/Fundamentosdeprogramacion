# sirve para mostrar el menu del programa
def mostrar_menu() -> None:
    print("\n===== MENÚ PRINCIPAL =====")
    print("1) Saludar")
    print("2) Calcular la suma de dos números")
    print("3) Mostrar la tabla de multiplicar del 5")
    print("0) Salir")
    
#esta funcion sirve para seleccionar la opcion saludar.
def opcion_saludar() -> None:
    nombre = input("¿Cómo te llamas? ").strip()
    print(f"¡Hola, {nombre}! Bienvenido/a.")

#sirve para seleccionar la opcion suma ejecuta la parte de la suma
def opcion_suma() -> None:
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        print(f"La suma es: {a + b}")
    except ValueError:
        print(" Debes introducir valores numéricos.")

# aqui solo ejecuta la opcion de la tabla
def opcion_tabla() -> None:
    numero = 5
    print(f"\nTabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} × {i} = {numero * i}")


# ---------- Bucle principal ----------
continuar = True   
# solo se ejecuta si l condicion es verdadera para crear un bucle            
while continuar:
    mostrar_menu()             
    eleccion = input("Elige una opción: ").strip()

    if eleccion == "1":
        opcion_saludar()
    elif eleccion == "2":
        opcion_suma()
    elif eleccion == "3":
        opcion_tabla()
    elif eleccion == "0":
        print("\n ¡Hasta luego!")
        continuar = False
    else:
        # es para imprimir en caso de selecciorar una accion no valida mandara error
        print(" Opción no válida, intenta de nuevo.")

print("Programa terminado.")