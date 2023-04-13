import re
frase = input ("ingresa la frase: ")
palabra = input ("ingresa la palabra: ")
frase = re.sub(r'[^\w\s]', '', frase)
lista = frase.split()
aux = 0
for elem in lista:
    if elem.lower() == palabra.lower():
        aux += 1
print(aux)