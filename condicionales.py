"""edad = 16
#comparaciones

if edad >= 18: 
    print("La persona es mayor de edad y tiene " + edad)
else:
    print("La persona es menor de edad y tiene " + edad)    

    
sexo = "M"
if sexo == "M":
    print("masculino")
elif sexo == "F":
    print("femenino")
else:
    print("otro")  
"""
"""
primera infacia  sea de cero a 5 años
infancia entre 6 y 13 años
adolecencia entre 14 y 27 años
18+ adultos


edad = int(input("ingrese su edad: "))
if edad >= 0 and edad < 6:
    print("primera infacia")
    if edad >= 0 and edad < 2:
        print("es un bebe")
    else:
        print("es un niño")    
elif edad >= 6 and edad  < 14:
    print("infancia")
elif edad  >= 14 and edad < 18:
    print("adolecente")
elif edad >= 18 and edad < 100:
    print("adulto")
else:
    print("error")
"""
"""
""" """   
i = 0
while i <= 10:
    print(i)
    i += 2                
"""    
""" 

tabla = int(input("tabla multiplicar "))
i = 1
while i < 11:
    if i == 6:
        break
    print(tabla,"x", i , "=",i*tabla)
    i += 1
print("termina")  
""" 

tabla = int(input("tabla multiplicar "))
i = 1
while i <= 10:
    #if i == 6:
    #    continue
    print(tabla,"x", i , "=",i*tabla)
    i += 1
print("termina")  

"""
i = 0
while i < 11:
    i += 1   
    
    if i == 6:
        continue
    print(i , "X", tabla, "=", i*tabla)
print("Aquí ya salió del ciclo")

#ciclo for
cadena = "cosita"
#for elemento in cadena:
 #   print(elemento)
    
posicion= 0
longitud = len(cadena)
while posicion <= longitud:
    print(cadena[posicion])   
    posicion =+ 1
#repasar estructuras de control de flujo   
""" 