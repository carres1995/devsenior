#listas
"""
frutas = ["uva", "manzana", "banano", "fresa", 5, True]
#print(frutas[0])
#ordenadas, mutabkes, permiten duplicados
print(len(frutas)) #abreviatura de lenght- longitud
print(type(frutas)) #tipo de elemento
"""

"""
marcas = list(("mazda", "renault", "fiat"))

print(marcas[0:2])
"""
"""
marcas = list(("mazda", "renault", "fiat"))
marcas.append("bmw")
#marcas.clear()
print(marcas)
marcas2 = marcas.copy()
marcas1= ["chevrolet", "renault"]
#count conteo de un mismo elemento
marcas.extend(marcas1)
print(marcas)

print(marcas.index("renault"))
marcas.insert(1, "mercedes")
print(marcas)
"""
"""
marcas =['mazda', 'renault', 'fiat', 'bmw', 'chevrolet', 'renault']
marcas[1]= "volvo"
print(marcas)
"""

"""
marcas =['mazda', 'renault', 'fiat', 'bmw', 'chevrolet', 'renault']
marcas.pop()
print(marcas)
"""
"""
marcas =['mazda', 'renault', 'fiat', 'bmw', 'chevrolet', 'renault']
marcas.remove("mazda")
print(marcas)
marcas.reverse()
print(marcas)
marcas.sort()
print(marcas)
"""

