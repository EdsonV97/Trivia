print ("Hola bienvenido a mi trivia")
print ("")
print ("")
nombre = input("Ingresa tu nombre: ")
print ("\nHola",nombre,"resuelve el siguiente problema escribiendo la primera letra de la opción que elegiste y presione Enter para enviar su respuesta.")

print ("")
print ("PROBLEMA 1: 99 - 92 - 86 - 81 - XXX")
print ("a) 95")
print ("b) 79")
print ("c) 77")

pista = input("Quieres una pista? escribe si o no  ")
if pista == "si":
  print("Es una secuencia de numeros decrecientes")
if pista =="no":
  print("")
while pista not in ("si", "no"):  
  pista= input("Solo debes escoger entre si o no")
rp1 = input("Tu respuesta: ")

while rp1 not in ("a","b","c"):  
  rp1 = input("Solo debes responder con a, b o c.")

if rp1 =="c":
  print("Repuesta Correcta")
else:
  print("Respuesta Incorrecta")
