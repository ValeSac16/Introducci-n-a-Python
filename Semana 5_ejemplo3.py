from eii_utils import leer_entero, limpiar_consola, imprimir_mensaje, imprimir_error

estudiantes: int = 0
monto: int = 0

limpiar_consola()
estudiantes  = leer_entero("Cuantos estudiantes son ")
monto = leer_entero("Monto recolectado")

if monto >= (estudiantes * 500):
    imprimir_mensaje("Nos fuimos de fiesta")
else:
    imprimir_error("Se devuelve el dinero")