from eii_utils import leer_entero, leer_flotante, limpiar_consola, imprimir_mensaje, imprimir_error

salario: float = 0
salario_minimo: float = 0
impuesto: float = 0

#entradas
limpiar_consola()
salario = leer_flotante("¿Cuanto es su salario?")
salario_minimo = leer_flotante("¿Cuanto es el salario mínimo actualmente?")

if salario > (5* salario_minimo):
    impuesto = (salario - 5*salario_minimo) * 0.25
    imprimir_mensaje ("Paga el impuesto")

else:
    impuesto = 0
    imprimir_error ("No paga impuesto")

print(f"El impuesto es {impuesto}")