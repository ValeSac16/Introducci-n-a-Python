from eii_utils import limpiar_consola, leer_booleano_opcional, leer_entero_opcional

edad: int = 0
i: int = 0
total: int = 0
promedio: float = 0
continuar: bool = True

limpiar_consola()

while continuar:
    edad = leer_entero_opcional("Digite la edad", 19)
    i = i + 1
    total += edad
    continuar = leer_booleano_opcional("Desea continuar", True)

promedio = total / i
print(promedio)