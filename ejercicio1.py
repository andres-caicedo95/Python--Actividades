import math

print("CÁLCULO DEL ÁREA DE LA FIGURA")
print("=" * 30)

# Solicitar datos de entrada
H = float(input("Ingrese el valor de la hipotenusa H: "))
R = float(input("Ingrese el valor del cateto R (radio): "))

# Validar que los datos sean positivos
if H <= 0 or R <= 0:
    print("Error: H y R deben ser valores positivos")
else:
    # Validar que H sea mayor que R (por teorema de Pitágoras)
    if H <= R:
        print("Error: La hipotenusa H debe ser mayor que el cateto R")
    else:
        # 1. Calcular el cateto faltante (altura del triángulo)
        altura_triangulo = math.sqrt(H**2 - R**2)
        
        # 2. Calcular el área de un triángulo
        area_triangulo = (R * altura_triangulo) / 2
        
        # 3. Calcular el área total de los dos triángulos
        area_total_triangulos = 2 * area_triangulo
        
        # 4. Calcular el área del semicírculo
        area_semicirculo = (math.pi * R**2) / 2
        
        # 5. Calcular el área total de la figura
        area_total = area_total_triangulos + area_semicirculo
        
        # Mostrar resultados
        print("\nRESULTADOS:")
        print("=" * 30)
        print(f"Altura del triángulo: {altura_triangulo:.2f}")
        print(f"Área de un triángulo: {area_triangulo:.2f}")
        print(f"Área total de los dos triángulos: {area_total_triangulos:.2f}")
        print(f"Área del semicírculo: {area_semicirculo:.2f}")
        print(f"Área total de la figura: {area_total:.2f}")