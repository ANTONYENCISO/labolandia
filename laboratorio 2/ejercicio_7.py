años_vividos = int(input("Introduce el número de años que has vivido: ")) #supongamos que a vivido 100

segundos_por_año = 365 * 24 * 60 * 60        # dias que tiene un año, horas del día, minutos cada hora, segundos de un minuto
segundos_vividos = años_vividos * segundos_por_año

print(f"Has vivido durante {segundos_vividos} segundos.")

#si en caso fuera un año bisiesto

años_vividos = int(input("Introduce el número de años que has vivido: ")) #supongamos que a vivido 100

segundos_por_año = 366 * 24 * 60 * 60       
segundos_vividos = años_vividos * segundos_por_año

print(f"Has vivido durante {segundos_vividos} segundos.")