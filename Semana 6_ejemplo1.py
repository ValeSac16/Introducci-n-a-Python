nombre: str = "Valeria"
apellido: str = "Zamora"
cumple: str = "16 de febrero"

#"Hola, soy xxx xxx y cumplo el dìa xxx"

print(f"Hola, soy {nombre} {apellido} y cumplo el dìa {cumple}")

costo: float = 123,344
utilidad: float = costo * o.5
impuesto: float = (costo + utilidad)*0.13
total: float = costo + utilidad + impuesto

print(f"costo {costo}")
print(f"utilidad {utilidad}")
print(f"impuesto {impuesto}")
print(f"total {total}")
print(`_`*10)
print("{:12} {:8.2f}".format("costo", costo))
print("{:12} {:8.2f}".format("utilidad", utilidad))
print("{:12} {:8.2f}".format("impuesto", impuesto))
print("{:12} {:8.2f}".format("total", total))