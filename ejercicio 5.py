nom = input("¿Cual es tu nombre? ")
sexo = input("¿Cuál es tu sexo (Mujer o Hombre)? ")
if sexo == "M":
    if nom.lower() < "m":
        grupo = "a"
    else:
        grupo = "b"
else:
    if nom.lower() > "n":
        group = "a"
    else:
        grupo = "b"
print("Tu grupo es " + grupo)