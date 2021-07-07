from enum import Enum
from math_tools import vectorZeroes, zeroes
import classes

#Caso para leer una condicion
def INT_FLOAT(file, item_list, i):
    e0 = 0
    r0 = 0.0
    array  = [float(x) for x in file.readline().split()]
    e0 = int(array[0])
    r0 = array[1]
    item_list[i].setValues(classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], 
        classes.indicators["NOTHING"], e0, classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], 
        classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], 
        classes.indicators["NOTHING"], classes.indicators["NOTHING"], r0)

#Caso para leer un nodo
def INT_FLOAT_FLOAT_FLOAT(file, item_list: classes.item, i):
    e = 0
    r = 0.0 
    rr = 0.0 
    rrr = 0.0
    array = [float(x) for x in file.readline().split()]
    e = int(array[0])
    r = array[1]
    rr = array[2]
    rrr = array[3]
    item_list[i].setValues(e, r, rr, rrr, 
        classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], 
        classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], 
        classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"])

#Caso para leer un elemento
def INT10(file, item_list, i):
    e1 = 0
    e2 = 0
    e3 = 0
    e4 = 0
    e5 = 0
    e6 = 0
    e7 = 0
    e8 = 0
    e9 = 0
    e10 = 0
    e11 = 0
    array = [int(x) for x in file.readline().split()]
    e1 = array[0]
    e2 = array[1]
    e3 = array[2]
    e4 = array[3]
    e5 = array[4]
    e6 = array[5]
    e7 = array[6]
    e8 = array[7]
    e9 = array[8]
    e10 = array[9]
    e11 = array[10]
    item_list[i].setValues(e1, classes.indicators["NOTHING"], classes.indicators["NOTHING"], classes.indicators["NOTHING"], 
        e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, classes.indicators["NOTHING"])

#La sentencia de switch no existe en python, pero se puede hacer algo similar con el uso de diccionarios
switch = {
    classes.modes["INT_FLOAT"]: INT_FLOAT,
    classes.modes["INT_FLOAT_FLOAT_FLOAT"]: INT_FLOAT_FLOAT_FLOAT,
    classes.modes["INT10"]: INT10
}

#Esta funcion hace uso del switch para leer datos de la malla
def obtenerDatos(file, nlines, n, mode, item_list):
    line = ""
    line = file.readline()
    if(nlines == classes.lines["DOUBLELINE"]):
        line = file.readline()
    for i in range(n):
        switch[mode](file, item_list, i)

def correctConditions(n, list, indices, nNodes, nDirichx, nDirichy, nDirichz):
    #Python deja las variables delclaradas dentro de un grupo de instrucciones accesibles desde fuera, lo que causa problemas si se quiere
    #reusar el mismo nombre de variable

    #Aqui se copian los id de cada dirichlet para guardarlos y darselos al gid
    #Para nuestra logica vamos a ocupar las posiciones procesadas de cada dirichlet
    for r in range(n):
        indices[r] = list[r].getNode1()
    
    #Estos for corrigen la numeracion de los dirichlet de y 'y' de 'z' ya que los imprimimos 
    for m in range(nDirichy):
        list[nDirichx + m].setNode1(list[m].getNode1() + nNodes)
    
    for t in range(nDirichz):
        list[nDirichx + nDirichy + t].setNode1(list[t].getNode1() + 2*nNodes)

    #Este for corrige los indices de forma en la lista de dirichlet
    for i in range(n-1):
        pivot = list[i].getNode1()
        for j in range(i, n):
            pos = list[j].getNode1()
            if(pos > pivot):
                list[j].setNode1(pos-1)

#Esta funcion le agrega una extension al file para su uso en el codigo
def addExtension(filename, extension):
    tupla = (filename, extension)
    newFileName = "".join(tupla)
    return newFileName

#Funcion super importante que llena la malla de los datos en el file .dat
def leerMallayCondiciones(m, filename):
    inputFileName = ""
    nNodes = 0  
    nEltos=0 
    nDirich=0 
    nNeu = 0
    #Lectura de todos los valores preexistentes como mi Ei, y mi vector f
    inputFileName = addExtension(filename, ".dat")
    file = open(inputFileName, "r")
    line  = [float(x) for x in file.readline().split()]
    Ei = line[0]
    f_x = line[1]
    f_y = line[2]
    f_z = line[3]
    line = [int(x) for x in file.readline().split()]
    nNodes = line[0]
    nEltos = line[1]
    nDirichx = line[2]
    nDirichy = line[3]
    nDirichz = line[4]
    nDirich = nDirichx + nDirichy + nDirichz
    nNeu = line[5]

    file.readline()

    #Se setean los valores leidos en el objeto mesh
    m.setParameters(Ei, f_x, f_y, f_z)
    m.setSizes(nNodes, nEltos, nDirich, nNeu)
    m.createData()

    #Se leen primero los nodos de la mesh y se guardan ya que la malla se pasa por referencia
    obtenerDatos(file, classes.lines["SINGLELINE"], nNodes, classes.modes["INT_FLOAT_FLOAT_FLOAT"], m.getNodes())
    file.readline()
    #Se leen los elementos de la mesh y se guardan en ella ya que se pasan por referencia
    obtenerDatos(file, classes.lines["DOUBLELINE"], nEltos, classes.modes["INT10"], m.getElements())
    file.readline()
    #Se leen los dirichlet de la malla y se guardan estos en el objeto malla
    obtenerDatos(file, classes.lines["DOUBLELINE"], nDirichx+nDirichy+nDirichz, classes.modes["INT_FLOAT"], m.getDirichlet())
    #Se leen los neumann de la malla
    obtenerDatos(file, classes.lines["DOUBLELINE"], nNeu, classes.modes["INT_FLOAT"], m.getNeumann())

    file.close()
    #Se llama a la funcion para corregir los id de los dirichlet y guardar otros datos que necesitaremos despues
    correctConditions(nDirich, m.getDirichlet(), m.getDirichletIndices(), m.getSize(classes.sizes["NODES"]), nDirichx,nDirichy, nDirichz)

#Encontrar un valor en un vector
def findIndex(v, s, arr):
    for i in range(s):
        if(arr[i] == v):
            return True
    return False

#Funcion para escribir en el file .post.res los resultados calculados por el programa
def writeResults(m, T, filename):
    outputFilename = ""
    dirichIndices = m.getDirichletIndices()
    dirich = m.getDirichlet()

    outputFilename = addExtension( filename, ".post.res")
    print(outputFilename)
    file = open(outputFilename, "w")

    file.write("GiD Post Results File 1.0\n")
    file.write("Result \"Fuerza\" \"Load Case 1\" 1 Scalar OnNodes\nComponentNames \"w\"\nValues\n")

    Tpos = 0
    Dpos = 0
    n = m.getSize(classes.sizes["NODES"])
    nd = m.getSize(classes.sizes["DIRICHLET"])
    for i in range(n):
        if(findIndex(i+1, nd, dirichIndices)):
            string = str(i+1) + " " + str(dirich[Dpos].getValue()) + "\n"
            file.write(string)
            Dpos+= 1
        else:
            string2 = str(i+1) + " " + str(T[Tpos]) + "\n"
            file.write(string2)
            Tpos+= 1
    
    file.write("End values\n")
    file.close()
