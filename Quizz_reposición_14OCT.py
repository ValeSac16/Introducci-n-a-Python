#Valeria Sofía Sacahuí Calderón  C6M606

from eii_utils import leer_entero, leer_booleano, limpiar_consola

limpiar_consola()

precio_compra_bolsas = 600
precio_una_bolsa = 1100
precio_dos_bolsas = 1700
precio_tres_bolsas = 2400
bolsas_gratis: int = 0
inventario: int = 0

ingresos_totales = 0
bolsas_vendidas = 0
descubierta = False
piso: int = 0
aula: int = 0

bolsas_compradas = input("¿Cuántas bolsas desea comprar María? ")
bolsas_compradas = int(bolsas_compradas)
bolsas_gratis = (bolsas_compradas // 12) * 3

inventario = bolsas_compradas + bolsas_gratis
costo_total = bolsas_compradas * precio_compra_bolsas
utilidad_final: int = 0

piso = 1
while piso <= 2 and inventario > 0 and not descubierta:

    aula = 1

    while aula <= 10 and inventario > 0 and not descubierta:

        print("\nPiso:", piso, "Aula:", aula)

        # Verificar si hay personal de seguridad
        seguridad = input("¿Hay personal de seguridad cerca? (s/n): ").strip().lower()

        if seguridad == "s":
            descubierta = True
            print("María fue descubierta. La jornada termina.")

        else:
            respuesta_cliente = input("¿Hay clientes interesados en comprar? (s/n): ").strip().lower()

            while respuesta_cliente == "s" and inventario > 0:

                print("Inventario disponible:", inventario)
                cantidad = input("¿Cuántas bolsas desea comprar el cliente? ")

                # Validar la cantidad solicitada
                while (
                    not cantidad.isdigit()
                    or int(cantidad) < 1
                    or int(cantidad) > 3
                    or int(cantidad) > inventario
                ):
                    cantidad = input("Inventario insuficiente")

                cantidad = int(cantidad)

                if cantidad == 1:
                    precio_venta = precio_una_bolsa
                elif cantidad == 2:
                    precio_venta = precio_dos_bolsas
                else:
                    precio_venta = precio_tres_bolsas

                ingresos_totales = ingresos_totales + precio_venta
                bolsas_vendidas = bolsas_vendidas + cantidad
                inventario = inventario - cantidad

                print("Venta realizada, ingreso de esta venta:", precio_venta)
                print("Bolsas restantes:", inventario)

                if inventario >= cantidad:
                    respuesta_cliente = input("¿Hay otro cliente interesado? (s/n): ").strip().lower()   

        aula = aula + 1

    piso = piso + 1

utilidad_final = ingresos_totales - costo_total


print("Resumen de jornada: ")
print("Ingresos totales:", ingresos_totales, "colones")
print("Bolsas vendidas:", bolsas_vendidas)
print("Bolsas restantes:", inventario)
print("Utilidad final:", utilidad_final, "colones")

if descubierta:
    print("Motivo de finalización: María fue descubierta.")
elif inventario == 0:
    print("Motivo de finalización: se agotó el inventario.")
else:
    print("Motivo de finalización: terminó el recorrido.")