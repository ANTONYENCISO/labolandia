cadena = input("Introduce los dos nombres de tu ex: ")

vocales = "aeiouAEIOU"

contador_vocales = 0

for letra in cadena:
    if letra in vocales:
        contador_vocales += 1
print(f"El numero de vocales en la cadena es: {contador_vocales}")