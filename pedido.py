def calcular_total(subtotal):
    descuento = subtotal * 0.10
    total = subtotal - descuento
    return total


subtotal = 100.00
print(f"Total a pagar: S/ {calcular_total(subtotal):.2f}")
