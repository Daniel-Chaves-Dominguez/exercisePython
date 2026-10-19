# # # COLECCIONES
# ## Ejercicio 1:
# numeros = [7, 10, 26]
# print(numeros[0])
# print(numeros[1])
# print(numeros[2])


# ## Ejercicio 2:
# textos = ["uno", "dos", "tres", "cuatro"]
# print(textos)
# textos[1] = "nuevo"
# print(textos)


# ## Ejercicio 3:
# numeros = [2, 4, 6]
# print(sum(numeros))


# ## Ejercicio 4:
# numeros = [2, 4, 6, 8, 10]
# print(sum(numeros) / len(numeros))


# ## Ejercicio 5:
# palabras = ["Sol", "Luna", "Estrella"]
# print(max(palabras, key=len))


# ## Ejercicio 6:
# palabras = ["Casa", "Perro", "Gato", "Mesa", "Silla"]
# palabra = input("Escribe una palabra: ")
# esta = palabra in palabras
# print(f"La palabra {palabra} está en la lista: {esta}")


# ## Ejercicio 7:
# matriz = [[1, 2], [3, 4]]
# print(matriz[0][0])
# print(matriz[0][1])
# print(matriz[1][0])
# print(matriz[1][1])


# ## Ejercicio 8:
# matriz = [[1, 2, 3], [4,5,6]]
# media = sum(matriz[0] + matriz[1]) / (len(matriz[0]) + len(matriz[1]))
# print(media)


# ## Ejercicio 9:
# nombres = []
# nombres.append("Ana")
# nombres.append("Luis")
# nombres.append("Marta")
# nombres.append("Pedro")
# nombres.append("Lucía")
# print(nombres[0])
# print(nombres[-1])
# print(len(nombres))


# ## Ejercicio 10:
# notas = [6.5, 4.0, 7.25, 5.5, 3.75]
# media = sum(notas) / len(notas)
# if media >= 5:
#     print("Aprobado")
# else:
#     print("Suspenso")


# ## Ejercicio 11:
# colores = ["rojo", "azul", "verde", "negro", "blanco"]
# color = input("Escribe un color: ")
# if color in colores:
#     print("El color está en la lista")
# else:
#     print("El color no está en la lista")


# ## Ejercicio 12:
# dnis = {"12345678A", "12345678B", "12345678C", "12345678D", "12345678D"}
# print(len(dnis))

# print("12345678E" in dnis)


# ## Ejercicio 13:
# nombres = {"Ana", "Luís", "Marta", "Pedro", "Lucía"}
# nombre = input("Escribe un nombre: ")
# if nombre in nombres:
#     print("Ya existe")
# else:
#     nombres.add(nombre)
# print(nombres)


# ## Ejercicio 14:
# a = {1,2,3,4}
# b = {5,6}
# if len(a) > len(b):
#     print("El primero es más largo")
# elif len(a) < len(b):
#     print("El segundo es más largo")
# else:
#     print("Tienen el mismo tamaño")


# ## Ejercicio 15:
# diccionario = {"Ana": 20, "Luís":17, "Marta":35, "Pedro":12, "Lucía":18}
# nombre = input("Escribe el nombre: ")
# if nombre in diccionario:
#     edad = diccionario[nombre]
#     print(f"{nombre} tiene {edad} años")
#     print(f"Es mayor de edad: {edad >= 18}")


# ## Ejercicio 16:
# diccionario = {"Ana": 7.5, "Luís":3.5, "Marta":4.5, "Pedro":8.75, "Lucía":6.75}
# nombre = input("Escribe el nombre: ")
# if nombre in diccionario:
#     nota = diccionario[nombre]
#     print(f"{nombre} tiene {nota} de nota media")
#     print(f"El alumno ha aprobado: {nota >= 5}")



# ## Ejercicio 17:
# diccionario = {"Ana": "1234", "Luís":"decg45", "Marta":"koloko", "Pedro":"salchicha", "Lucía":"bocadillo12"}
# nombre = input("Escribe el nombre: ")
# contraseña = input("Escribe la contraseña: ")
# if nombre in diccionario and diccionario[nombre] == contraseña:
#     print("Login correcto")
# else:
#     print("Usuario y/o contraseña incorrectos")



# # CONDICIONALES
## Ejercicio 1:
# nota = float(input("Introduce una nota del 0 al 10: "))
# if nota >= 9:
#     print("Sobresaliente")
# elif nota  >= 7:
#     print("Notable")
# elif nota > 5:
#     print("Bien")
# elif nota == 5:
#     print("Suficiente")
# else:
#     print("Insuficiente")


# ## Ejercicio 2:
# a = float(input("Introduce un número: "))
# b = float(input("Introduce otro número: "))
# simbolo = input("Operación(+, -, *, /): ")
# if simbolo == "+":
#     print(a + b)
# elif simbolo == "-":
#     print(a - b)
# elif simbolo == "*":
#     print( a * b)
# elif simbolo == "/":
#     print( a / b)
# else:
#     print("Símbolo no válido")


# ## Ejercicio 3:
# a = float(input("Introduce un número: "))
# b = float(input("Introduce otro número: "))
# c = float(input("Introduce el último número: "))
# if a >= b and a >= c:
#     print(f"El mayor es {a}")
# elif b >= a and b >= c:
#     print(f"El mayor es {b}")
# elif a == b and a == c:
#     print("Son iguales")
# else:
#     print(f"El mayor es {c}")


# ## Ejercicio 4:
# a = float(input("Escribe un lado del triángulo: "))
# b = float(input("Escribe otro del triángulo: "))
# c = float(input("Escribe el último lado del triángulo: "))
# if a == b == c:
#     print("Equilátero")
# elif a == b or a == c or b == c:
#     print("Isósceles")
# else:
#     print("Escaleno")


# ## Ejercicio 5:
# a = float(input("Introduce un número si quieres saber si está entre 100 y 200: "))
# if a >= 100 and a <= 200:
#     print("Está dentro del rango")
# else:
#     print("No está dentro del rango")


# ## Ejercicio 6:
# metros = float(input("Metros: "))
# unidad = input("Unidad (km,cm,mm): ")
# if unidad == "km":
#     print(f"{metros} m son {metros / 1000} km")
# elif unidad == "cm":
#     print(f"{metros} m son {metros * 100} cm")
# elif unidad == "mm":
#     print(f"{metros} m son {metros * 1000} mm")
# else:
#     print("Unidad no válida")


# ## Ejercicio 7:
# edad = int(input("Edad: "))
# fin_semana = input("¿Es fin de semana? (s/n): ") == "s"
# if edad < 12:
#     precio = 5
# elif edad <=17:
#     precio = 7
# else:
#     precio = 10

# if fin_semana:
#     precio = precio + 2
# print(f"La entrada cuesta {precio} €")


# ## Ejercicio 8:
# meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
# mes = int(input("Introduce un número de mes (1-12): "))
# print(meses[mes - 1])


# ## Ejercicio 9:
# n = int(input("Introduce un número: "))
# if n % 3 == 0:
#     print(f"El número {n} es múltiplo de 3")
# elif n % 5 == 0:
#     print(f"El número {n} es múltiplo de 5")
# elif n % 7 == 0:
#     print(f"El número {n} es múltiplo de 7")
# else:
#     print(f"El número {n} no es múltiplo de 3, 5 ni 7")


# ## Ejercicio 10:
# t = float(input("Temperatura: "))
# if t < 10:
#     print("Hace frío")
# elif t >= 10 and t < 30:
#     print("Es templada")
# else:
#     print("Hace calor")


# # BUCLES
## Ejercicio 1:
i = 1
while i <= 10:
    print(i)
    i += 1


## Ejercicio 2:
i = 10
while i >= 1:
    print(i)
    i -= 1


## Ejercicio 3:
i = 1
suma = 0
while i <= 10:
    suma += i
    i += 1
print(f"La suma de los números del 1 al 10 es: {suma}")


## Ejercicio 4:
factorial = 1
i = 8 
while i >= 1:
    factorial = factorial * i
    i -= 1
print(f"El factorial de 8 es: {factorial}")