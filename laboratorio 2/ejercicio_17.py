cadena = input("Introduce una cadena: ")

prefijo = input("Introduce el prefijo a verificar: ")
sufijo = input("Introduce el sufijo a verificar: ")

comienza_con_prefijo = cadena.startswith(prefijo)
termina_con_sufijo = cadena.endswith(sufijo)

if comienza_con_prefijo and termina_con_sufijo:
    print("La cadena comienza con el prefijo y termina con el sufijo.")
elif comienza_con_prefijo:
    print("La cadena comienza con el prefijo, pero no termina con el sufijo.")
elif termina_con_sufijo:
    print("La cadena termina con el sufijo, pero no comienza con el prefijo.")
else:
    print("La cadena no comienza con el prefijo ni termina con el sufijo.")
