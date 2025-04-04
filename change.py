def change():
    gasto_persona = 23.75
    pago = 100
    print("Ingresar gasto:")
    print(gasto_persona)
    print("Dinero recibido")
    print(pago)
    print("\n")
    z = pago - gasto_persona
    l = str(z).split('.')[1]
    print("Vuelto")
    print("\n")
    print("Pesos:")
    print(z)
    print("Centavos:")
    print(l)
change()
