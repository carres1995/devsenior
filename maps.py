#map
def MiFuncion(x):
    return len (x)


x =map(MiFuncion, ("MANZANA", "BANANO", "CEREZA"))
for i in x:
    print(i)
