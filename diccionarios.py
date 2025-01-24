"""carro ={
    "marca":"mazda",
    "modelo":"cx5", 
    "año":"2025", 
    "colores":["rojo", "azul", "negro"]
    }
#print(carro["modelo"])
#print(len(carro))
#print(carro ["colores"][1])
#print(type(carro))
#print(carro.keys())
#print(carro.values())

#carro["marca"] ="renault"
print(carro)
print(carro.items())
"""
#setdefault() and update()
carro ={
    "marca":"mazda",
    "modelo":"cx5", 
    "año":"2025", 
    "colores":["rojo", "azul", "negro"]
    }
#carro.setdefault( "cilindraje" , "2500")
#carro.setdefault( "modelo" , "cx30")
carro.update('modelo': 'cx30', "año": "2025")
print(carro)


