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
number_range = 17
lower_bound = 0
upper_bound = 10
in_range = number_range > lower_bound and number_range < upper_bound
print(f"El número {number_range} está entre {lower_bound} y {upper_bound}: {in_range}")