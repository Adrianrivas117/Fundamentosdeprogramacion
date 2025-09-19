#van a crear una lista vacia con su nombre y van agregar 5 elementos con input: 
#(nombre, preparatoria, lugar de residencia, edad, carrera)

lista_nombres = []
print(" Lista de nombres ")
producto1 = input(" Agrega el primer producto: ")
lista_nombres.append(producto1)
producto2 = input("Agrega el segundo producto: ")
lista_nombres.append(producto2)
producto3 = input("Agrega el tercer producto: ")
lista_nombres.append(producto3)
producto4 = input("Agrega el cuarto producto: ")
lista_nombres.append(producto4)
print("\n Tu lista de nombres es:")
for producto in lista_nombres:
    print(f"- {producto}")
print("\n✅ ¡Lista creada con éxito!")
#https://www.webfx.com/tools/emoji-cheat-sheet/
