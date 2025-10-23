print("Ejercicio propuesto 4")
print("LA LANGOSTA AHUMADA - PRESUPUESTO DE BANQUETES")

# Entrada del número de personas
personas = int(input("Ingrese el número de personas para el evento: "))

# Determinar el costo por platillo según el rango
if personas > 300:           # Mayor a 300
    costo_platillo = 75.00
    presupuesto_total = personas * costo_platillo
elif personas > 200 and personas <= 300:  # Mayor a 200 Y menor o igual a 300
    costo_platillo = 85.00
    presupuesto_total = personas * costo_platillo
else:  # 200 personas o menos
    costo_platillo = 95.00
    presupuesto_total = personas * costo_platillo

# Mostrar resultados
print("\nPRESUPUESTO DEL EVENTO:")
print(f"Número de personas: {personas}")
print(f"Costo por platillo: ${costo_platillo:.2f}")
print(f"PRESUPUESTO TOTAL: ${presupuesto_total:.2f}")

