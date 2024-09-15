lista1 = list(range (1 ,11))
lista2 = list(range(5, 15))
lista3 = list(range(10 , 20))

conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

conjunto_comun = conjunto1 & conjunto2 & conjunto3

conjunto_union = conjunto1 | conjunto2 | conjunto3

conjunto_diferencia = conjunto1 - conjunto3

tupla_comun = tuple(conjunto_comun)
tupla_union = tuple(conjunto_union)
tupla_diferencia = tuple(conjunto_diferencia)

tupla_comun = sorted(tupla_comun)
tupla_union = sorted(tupla_union)
tupla_diferencia = sorted(tupla_diferencia)

suma_comun = tupla_comun[0] + tupla_comun[-1] if tupla_comun else None
suma_union = tupla_union[0] + tupla_union[-1] if tupla_union else None
suma_diferencia = tupla_diferencia[0] + tupla_diferencia[-1] if tupla_diferencia else None

print("Conjunto común:", conjunto_comun)
print("Conjunto unión:", conjunto_union)
print("Conjunto diferencia:", conjunto_diferencia)

print("Suma del primer y último elemento de la tupla común:", suma_comun)
print("Suma del primer y último elemento de la tupla unión:", suma_union)
print("Suma del primer y último elemento de la tupla diferencia:", suma_diferencia)
