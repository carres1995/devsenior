def añadir_Estudiante_List(nombre_estudiante, correo, cedula):
        
    estudianteList = []
    estudianteList.append(nombre_estudiante)
    estudianteList.append(correo)
    estudianteList.append(cedula)
    return estudianteList

def editar_Nombre_Estudiante_List(listaEstudiante: list, indice, nombre_estudiante):
    
    if indice < len(listaEstudiante):
        listaEstudiante[indice] = nombre_estudiante
    else:
        print("Indice esta fuera de rango")
        
    return listaEstudiante
def eliminar_Por_Indice_Estudiante(listaEstudiante: list, indice):
    
    if indice < len(listaEstudiante):
        listaEstudiante = listaEstudiante.pop(indice)
    else:
        print("Indice esta fuera de rango")
        
    return listaEstudiante

#Diccionario------------------------
def añadir_Estudiante_Dict(nombre_estudiante, correo, cedula):
    
    estudianteDict = {}
    
    estudianteDict.update({'Nombre' : nombre_estudiante, 'Correo': correo, 'Cedula' : cedula})
    
    return estudianteDict

#def editar_estudiante_dict(dictestudiante= dict):
#    if i 
    
    
# INPUTS ----------------------

nombre_Estudiante = input("Ingrese el nombre del estudiante: ")
correo = input("Ingrese el correo del estudiante: ")
cedula = int(input("Ingrese el cedula del estudiante: "))

listEstudiantes = añadir_Estudiante_List(nombre_Estudiante, correo, cedula)
#print(listEstudiantes)
#print(editar_Nombre_Estudiante_List(listEstudiantes, 0, "Mario"))
#print(eliminar_Por_Indice_Estudiante(listEstudiantes, 2))
#print(listEstudiantes)
dictEstudiantes = añadir_Estudiante_Dict(nombre_Estudiante, correo, cedula)
print(dictEstudiantes)