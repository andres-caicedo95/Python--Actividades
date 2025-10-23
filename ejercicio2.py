print("Ejercicio propuesto 2")

cantidad_litros = float(input("Ingresar litros de leche: "))
cantidad_galones = cantidad_litros / 3.785
precio = int(input("Ingresar el precio de galon de leche: "))
total_pago = cantidad_galones * precio
print(f"TOTAL GALONES: {cantidad_galones}")
print(f"TOTAL A PAGAR: {total_pago}")