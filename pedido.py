def calcular_total(subtotal):
    tarifa_servicio = subtotal * 0.08
    total = subtotal + tarifa_servicio
    return total


subtotal = 100.00
print(f"Total a pagar: S/ {calcular_total(subtotal):.2f}")
