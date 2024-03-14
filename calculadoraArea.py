#importa math para usar pi
import math

#le doy a pi su valor
pi = math.pi

radio = float(input("Cual quieres que sea el radio del cuadrado"))
#el ^ no eleva para elevar se usa **
area = pi*(radio**2)

print("El area del circulo con el radio que me has dado es de:", area)
