print("Ejercicio propuesto 3")
print("ALMACENES 'EL HARAPIENTO DISTINGUIDO'")

# Entrada del precio del traje
precio = float(input("Ingrese el precio del traje: $"))

# Calcular descuento según el precio
if precio > 2500:
    descuento_porcentaje = 15
    descuento = precio * (descuento_porcentaje / 100)
    precio_final = precio - descuento
else:
    descuento_porcentaje = 8
    descuento = precio * (descuento_porcentaje / 100)
    precio_final = precio - descuento

# Mostrar resultados
print("\nRESULTADO DE LA COMPRA:")
print(f"Precio original: ${precio:.2f}")
print(f"Descuento aplicado: {descuento_porcentaje}%")
print(f"Valor del descuento: ${descuento:.2f}")
print(f"Precio final a pagar: ${precio_final:.2f}")