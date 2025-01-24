#conjuntos tutor

#filter
edades= [5, 12, 17, 18, 24, 32]

def MiFuncion(x):
    if x<18:
        return False
    else:
        return True

adultos = filter(MiFuncion, edades)

for x in adultos:
    print(x)    