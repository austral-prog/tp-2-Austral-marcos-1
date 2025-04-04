def change():
  expense =23.75
  money=100
  vuelto = money - expense
  pesos = int(vuelto)
  centavos = int((vuelto - pesos)*100)
  print(f"Ingresar gasto:\n{expense}")
  print(f"Dinero recibido\n{money}\n")
  print(f"Vuelto\n")
  print(f"Pesos:\n{pesos}")
  print(f"Centavos:\n{centavos}")
change()
