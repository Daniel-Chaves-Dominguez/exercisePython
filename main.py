import math

# # VARIABLES Y OPERADORES
# # Ejercicio 1:
# a = float(input("Introduce el primer número: "))
# b = float(input("Introduce el segundo número: "))

# print(f"El resultado de la suma es {a + b}")
# print(f"El resultado de la resta es {a - b}")
# print(f"El resultado de la multiplicación es {a * b}")

# print(f"El resultado de la división es {a / b}")


# # Ejercicio 2:
# celsius = float(input("Grados Celsius: "))
# fahrenheit = celsius * 1.8 + 32
# print(f"{celsius} ºC es equivalente a {fahrenheit} ºF")


# km = float(input("Kilómetros: "))
# millas = km * 0.621371
# pies = km * 3280.84
# print(f"{km} km es equivalente a {millas} millas")
# print(f"{km} km es equivalente a {pies} pies")


# euros = float(input("Euros: "))
# libras = euros * 0.85
# dolares = euros * 1.1
# print(f"{euros} Euros es equivalente, a {libras} libras")
# print(f"{euros} Euros es equivalente, a {dolares} dólares")


# # Ejercicio 3: 
# nota1 = 7
# nota2 = 8
# nota3 = 6
# nota4 = 2

# media = (nota1 + nota2 + nota3 + nota4) / 4
# aprobado = media > 5

# print(f"La nota media es: {media}, el alumno ha aprobado {aprobado}") 


# # Ejercicio 4: 
# c = int(input("Introduce un número: "))
# par = c % 2 == 0
# print(f"El número {c} es par: {par}")


# # Ejercicio 5: 
# x = int(input("Número: ")) 
# lower_bound = 0
# upper_bound = 10
# in_range = x > lower_bound and x < upper_bound
# print(f"El número {x} está entre {lower_bound} y {upper_bound}: {in_range}")


# # Ejercicio 6:
# d = int(input("Número: "))
# print(f"El número {d} es múltiplo de 3: {d % 3 == 0}")
# print(f"El número {d} es múltiplo de 5: {d % 5 == 0}")
# print(f"El número {d} es múltiplo de 7: {d % 7 == 0}")


# # Ejercicio 7:
# lado = float(input("Lado del cuadrado: "))
# perimetro_cuadrado = 4 * lado
# area_cuadrado = lado ** 2
# print(f"Cuadrado de lado {lado}: perímetro {perimetro_cuadrado}, área {area_cuadrado}")

# base = float(input("Base del triángulo: "))
# altura = float(input("Altura del triángulo: "))
# area_triangulo = base * altura / 2
# print(f"Triángulo de base {base} y altura {altura}: área {area_triangulo}")

# radio = float(input("Radio del círculo: "))
# perimetro_circulo = 2 * math.pi * radio
# area_circulo = math.pi * radio ** 2
# print(f"Círculo de radio {radio}: perímetro {perimetro_circulo}, área {area_circulo}")

# cateto1 = float(input("Primer cateto: "))
# cateto2 = float(input("Segundo cateto: "))
# hipotenusa = math.sqrt(cateto1 ** 2 + cateto2 ** 2)
# print(f"Triángulo rectángulo de catetos {cateto1} y {cateto2}: hipotenusa {hipotenusa}")


# # Ejercicio 8:
# nombre = input("Nombre del producto: ")
# precio = float(input("Precio unitario: "))
# unidades = int(input("Unidades: "))
# impuesto = float(input("Impuesto (%): "))

# subtotal = precio * unidades
# total = subtotal + subtotal * impuesto / 100

# print(f"Producto: {nombre}")
# print(f"Precio unitario: {precio} euros")
# print(f"Unidades: {unidades} uds.")
# print(f"Subtotal: {subtotal} euros")
# print(f"Impuestos: {impuesto}%")
# print(f"Precio total: {total} euros")


# # Ejercicio 9:
# segundos_totales = int(input("Segundos: "))
# horas = segundos_totales // 3600
# resto = segundos_totales % 3600
# minutos = resto // 60
# segundos = resto % 60
# print(f"{horas} horas, {minutos} minutos y {segundos} segundos")


# #FUNCIONES
## Ejercicio 1:
def greet():
    print(f"Hello world")
greet()


## Ejercicio 2:
def greet_name(name):
    print(f"Hello {name}")
greet_name("Ana")
greet_name("Luis")
greet_name("Rafa")

## Ejercicio 3:
def pow(a,b):
    return a ** b
print(f"2 elevado a 3 es: {pow(2,3)}")

## Ejercicio 4:
def celsius_to_farenheit(temperature):
    return temperature * 1.8 + 32
print(f"24 grados Celsius son {celsius_to_farenheit(24)} grados farenheit")

## Ejercicio 5:
def area_circle(radius):
    return math.pi * radius ** 2
print(f"El area de un circulo cuyo radio es 4, es: {area_circle(4)}")

## Ejercicio 6:
def avg(a,b,c):
    return (a + b + c) / 3
print(f"La media de 2, 4, 6 es: {avg(2,4,6)}")

## Ejercicio 7:
def concat(a,b,c):
    return a + b + c
print(f"Concateno Ven a casa: {concat("Ven ", " a ", " casa")}")

## Ejercicio 8:
def full_name(name, surname1, surname2):
    return name + surname1 + surname2
print(f"Mi nombre completo es: {full_name("Daniel ", " Chaves "," Dominguez")}")

## Ejercicio 9:
def current_age(birth_year):
    return 2026 - birth_year
print(f"Tengo {current_age(1999)} anhos")

## Ejercicio 10:
def introduction(name, surname1, surname2, birth_year):
    nombre = full_name(name, surname1, surname2)
    edad = current_age(1999)
    print(f"Hola, soy {nombre} y tengo {edad} anhos")
introduction("Daniel ", " Chaves ", " Dominguez ", 1999)

## Ejercicio 11:
def welcome():
    return "Bienvenidos a la clase de Python"
print(welcome())

## Ejercicio 12:
def welcome_name(name):
    return f"Hola {name}, bienvenido a la clase de Pyhton"
print(welcome_name("Daniel"))

## Ejercicio 13:
def double(number):
    return number * number
print(f"El doble de 10 es: {double(10)}")

## Ejercicio 14:
def price_with_tax(price):
    return price * 1.21
print(f"El precio con impuestos de 100 es: {price_with_tax(100)}")

## Ejercicio 15
def price_with_tax2(price, tax):
    return price + price * tax / 100
print(f"Si a 100 le sumamos 10% de impuestos, sale a pagar: {price_with_tax2(100, 10)}")

## Ejercicio 16:
def volume_cube(side):
    return side ** 3
print(f"El volumen de un cubo 5cm de lado es: {volume_cube(5)}")

## Ejercicio 17:
def time_to_seconds(hours, minutes, seconds):
    return (hours * 3600) + (minutes * 60) + seconds
print(f"4 horas, 27 minutos con 11 segundos equivalen a: {time_to_seconds(4,27,11)} segundos")

## Ejercicio 18:
def pretty_text(text):
    return f"=== {text} ==="
print(pretty_text("Mi texto bonito"))

## Ejercicio 19:
def format_name(surnames, name):
    return f"{surnames}, {name}"
print(f"Se presenta el soldado {format_name("Chaves Dominguez", "Daniel")}")

## Ejercicio 20:
def passed(grade1, grade2, grade3):
    media = (grade1 + grade2 + grade3) / 3
    return media >= 5
print(f"He aprobado sacando un 4, 5 y 6 en los examenes?: {passed(4, 5, 6)}")

## Ejercicio 21:
def student_passed(name, surnames, grade1, grade2, grade3):
    nombre = format_name("Chaves Dominguez", "Daniel")
    aprobado = passed(3, 5, 4.5)
    print(f"{nombre} ha aprobado las asignaturas con un 3, 5 y 4.5?: {aprobado}")
student_passed("Daniel ", " Chaves Dominguez", 3, 4, 4.5)