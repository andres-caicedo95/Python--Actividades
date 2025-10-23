import math
print("Ejercicio propuesto 1")
print("CÁLCULO DEL ÁREA DE LA FIGURA")

# Entrada de datos
hipotenusa = float(input("Ingrese el valor de la hipotenusa: "))
radio = float(input("Ingrese el valor del radio: "))

# Validaciones
if hipotenusa <= 0 or radio <= 0:
    print("Error: Los valores deben ser positivos")
elif hipotenusa <= radio:
    print("Error: La hipotenusa debe ser mayor que el radio")
else:
    # Cálculos 
    altura_triangulo = math.sqrt(hipotenusa**2 - radio**2)        # altura = cateto faltante
    area_triangulo = (radio * altura_triangulo) / 2               # área = (base × altura)/2
    area_total_triangulos = 2 * area_triangulo                    # area total triangulos (triangulo *2)
    area_semicirculo = (math.pi * radio**2) / 2                   # area semicirculo (pi * radio**2) / 2   
    area_total = area_total_triangulos + area_semicirculo         # area_total = area total triangulos + area semicirculo   
    
    # Resultados
    print("\nRESULTADOS:")
    
    print(f"Hipotenusa: {hipotenusa:.2f}")
    print(f"Radio (base del triángulo): {radio:.2f}")
    print(f"Altura del triángulo: {altura_triangulo:.2f}")
    print(f"Área de un triángulo: {area_triangulo:.2f}")
    print(f"Área total triángulos: {area_total_triangulos:.2f}")
    print(f"Área semicírculo: {area_semicirculo:.2f}")
    print(f"ÁREA TOTAL: {area_total:.2f}")