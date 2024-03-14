num1 = int(input("Cual quieres que sea el primer numero"))
num2 = int(input("Cual quieres que sea el segundo numero"))

operacion = input("Que operacion matematica quieres hacer (multiplicacion, division, suma, resta)")

if operacion == "multiplicacion":
    print("El resutado de la multiplicacion es: ", num1*num2)
elif operacion == "division":
    print("El resutado de la division es: ", num1/num2)
elif operacion == "suma":
    print("El resutado de la suma es: ", num1+num2)
elif operacion == "resta":
    print("El resutado de la resta es: ", num1-num2)
