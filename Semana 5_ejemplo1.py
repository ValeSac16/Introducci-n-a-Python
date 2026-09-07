from eii_utils import leer_entero, leer_texto, limpiar_consola

#declaración
paciente: str = ""
edad: int = 0
encargado: str = ""

#entradas
limpiar_consola()
paciente = leer_texto("Digite el nombre del paciente ")
edad = int(input("Digite la edad "))

if edad < 18:
    encargado = leer_texto("Dgite el nombre de la persona encargada ")

    print(f"La persona paciente se llama {paciente} y tiene {edad} años")
    print(f"La persona encargada es {encargado}")