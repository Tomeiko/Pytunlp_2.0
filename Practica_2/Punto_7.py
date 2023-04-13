texto = """
 El salario promedio de un hombre en Argentina es de $60.000, mientras que 
el de una mujer es de $45.000. Además, las mujeres tienen menos 
posibilidades de acceder a puestos de liderazgo en las empresas. 
 """
lista = texto.split()
aux = 0
mayu = 0
min = 0
carac = 0
for elem in lista:
    aux += len(elem)
    for letra in elem:
        if letra.isupper():
            mayu += 1
        elif letra.islower():
            min += 1
        else:
            carac += 1
print ("total:", aux,  "mayusculas:", mayu, "minusculas:",min,"caracteres:", carac)
print(len(lista))