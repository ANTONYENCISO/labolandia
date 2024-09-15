
edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

edades_ordenadas = sorted(edades)

edad_minima = edades_ordenadas[0]
edad_maxima = edades_ordenadas[-1]

print("edad_minima", edad_minima)
print("edad_maxima", edad_maxima)

edades.extend([edad_minima , edad_maxima])

print("Lista_actualizada: ", edades)

n = len(edades_ordenadas)
if n % 2 == 0:
    mediana = (edades_ordenadas[n // 2 - 1] + edades_ordenadas[n // 2]) / 2
else:
    mediana = edades_ordenadas[n // 2]

print("Edad mediana:", mediana)

suma_edades= sum(edades)

numero_elementos = len(edades)

promedio = suma_edades / numero_elementos

print("Edad promedio" , promedio)

edad_minima = min(edades)
edad_maxima = max(edades)

rango = edad_maxima - edad_minima

print("Rango de edades:" , rango)

promedio = sum(edades) / len(edades)

valor_minimo_promedio = abs(edad_minima - promedio)
valor_maximo_promedio = abs(edad_maxima - promedio)

print("Valor absoluto de (mínimo - promedio):", valor_minimo_promedio)
print("Valor absoluto de (maximo - promedio):", valor_maximo_promedio)

