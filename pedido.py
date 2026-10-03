def calcular_total(subtotal, cliente_frecuente=False):
    descuento = subtotal * 0.10 if cliente_frecuente else 0
    tarifa_servicio = subtotal * 0.08
    total = subtotal - descuento + tarifa_servicio
    return total


if __name__ == "__main__":
    subtotal = 100.00

    total_frecuente = calcular_total(subtotal, True)
    total_normal = calcular_total(subtotal, False)
    total_cero = calcular_total(0, True)

    print(f"Subtotal: S/ {subtotal:.2f}")
    print(f"Cliente frecuente (-10% +8%): S/ {total_frecuente:.2f}")
    print(f"Cliente no frecuente (+8%): S/ {total_normal:.2f}")

    assert abs(total_frecuente - 98.00) < 0.001, "Falla: cliente frecuente"
    assert abs(total_normal - 108.00) < 0.001, "Falla: cliente no frecuente"
    assert abs(total_cero - 0.00) < 0.001, "Falla: subtotal cero"
    print("Validación: 3 casos de prueba OK")
