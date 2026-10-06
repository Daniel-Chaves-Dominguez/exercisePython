import math

# Ejercicio 1:
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))

print(f"El resultado de la suma es {a + b}")
print(f"El resultado de la resta es {a - b}")
print(f"El resultado de la multiplicación es {a * b}")

print(f"El resultado de la división es {a / b}")


# Ejercicio 2:
celsius = float(input("Grados Celsius: "))
fahrenheit = celsius * 1.8 + 32
print(f"{celsius} ºC es equivalente a {fahrenheit} ºF")


km = float(input("Kilómetros: "))
millas = km * 0.621371
pies = km * 3280.84
print(f"{km} km es equivalente a {millas} millas")
print(f"{km} km es equivalente a {pies} pies")


euros = float(input("Euros: "))
libras = euros * 0.85
dolares = euros * 1.1
print(f"{euros} Euros es equivalente, a {libras} libras")
print(f"{euros} Euros es equivalente, a {dolares} dólares")


# Ejercicio 3: 
nota1 = 7
nota2 = 8
nota3 = 6
nota4 = 2

media = (nota1 + nota2 + nota3 + nota4) / 4
aprobado = media > 5

print(f"La nota media es: {media}, el alumno ha aprobado {aprobado}") 


# Ejercicio 4: 
c = int(input("Introduce un número: "))
par = c % 2 == 0
print(f"El número {c} es par: {par}")


# Ejercicio 5: 
x = int(input("Número: ")) 
lower_bound = 0
upper_bound = 10
in_range = x > lower_bound and x < upper_bound
print(f"El número {x} está entre {lower_bound} y {upper_bound}: {in_range}")


# Ejercicio 6:
d = int(input("Número: "))
print(f"El número {d} es múltiplo de 3: {d % 3 == 0}")
print(f"El número {d} es múltiplo de 5: {d % 5 == 0}")
print(f"El número {d} es múltiplo de 7: {d % 7 == 0}")


# Ejercicio 7:
lado = float(input("Lado del cuadrado: "))
perimetro_cuadrado = 4 * lado
area_cuadrado = lado ** 2
print(f"Cuadrado de lado {lado}: perímetro {perimetro_cuadrado}, área {area_cuadrado}")

base = float(input("Base del triángulo: "))
altura = float(input("Altura del triángulo: "))
area_triangulo = base * altura / 2
print(f"Triángulo de base {base} y altura {altura}: área {area_triangulo}")

radio = float(input("Radio del círculo: "))
perimetro_circulo = 2 * math.pi * radio
area_circulo = math.pi * radio ** 2
print(f"Círculo de radio {radio}: perímetro {perimetro_circulo}, área {area_circulo}")

cateto1 = float(input("Primer cateto: "))
cateto2 = float(input("Segundo cateto: "))
hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
print(f"Triángulo rectángulo de catetos {cateto1} y {cateto2}: hipotenusa {hipotenusa}")


# Ejercicio 8:
nombre = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
unidades = int(input("Unidades: "))
impuesto = float(input("Impuesto (%): "))

subtotal = precio * unidades
total = subtotal + subtotal * impuesto / 100

print(f"Producto: {nombre}")
print(f"Precio unitario: {precio} euros")
print(f"Unidades: {unidades} uds.")
print(f"Subtotal: {subtotal} euros")
print(f"Impuestos: {impuesto}%")
print(f"Precio total: {total} euros")


# Ejercicio 9:
segundos_totales = int(input("Segundos: "))
horas = segundos_totales // 3600
resto = segundos_totales % 3600
minutos = resto // 60
segundos = resto % 60
print(f"{horas} horas, {minutos} minutos y {segundos} segundos")
