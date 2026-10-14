# # COLECCIONES
## Ejercicio 1:
numeros = [7, 10, 26]
print(numeros[0])
print(numeros[1])
print(numeros[2])


## Ejercicio 2:
textos = ["uno", "dos", "tres", "cuatro"]
print(textos)
textos[1] = "nuevo"
print(textos)


## Ejercicio 3:
numeros = [2, 4, 6]
print(sum(numeros))


## Ejercicio 4:
numeros = [2, 4, 6, 8, 10]
print(sum(numeros) / len(numeros))


## Ejercicio 5:
palabras = ["Sol", "Luna", "Estrella"]
print(max(palabras, key=len))


## Ejercicio 6:
palabras = ["Casa", "Perro", "Gato", "Mesa", "Silla"]
palabra = input("Escribe una palabra: ")
esta = palabra in palabras
print(f"La palabra {palabra} está en la lista: {esta}")


## Ejercicio 7:
matriz = [[1, 2], [3, 4]]
print(matriz[0][0])
print(matriz[0][1])
print(matriz[1][0])
print(matriz[1][1])


## Ejercicio 8:
matriz = [[1, 2, 3], [4,5,6]]
media = sum(matriz[0] + matriz[1]) / (len(matriz[0]) + len(matriz[1]))
print(media)


## Ejercicio 9:
nombres = []
nombres.append("Ana")
nombres.append("Luis")
nombres.append("Marta")
nombres.append("Pedro")
nombres.append("Lucía")
print(nombres[0])
print(nombres[-1])
print(len(nombres))


## Ejercicio 10:
notas = [6.5, 4.0, 7.25, 5.5, 3.75]
media = sum(notas) / len(notas)
if media >= 5:
    print("Aprobado")
else:
    print("Suspenso")


## Ejercicio 11:
colores = ["rojo", "azul", "verde", "negro", "blanco"]
color = input("Escribe un color: ")
if color in colores:
    print("El color está en la lista")
else:
    print("El color no está en la lista")
