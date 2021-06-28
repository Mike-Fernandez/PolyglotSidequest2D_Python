from enum import Enum
import classes

def INT_FLOAT(file, item_list, i):
    e0 = 0
    r0 = 0.0
    array  = [float(x) for x in file.readline().split()]
    e0 = int(array[0])
    r0 = array[1]
    item_list[i].setValues(classes.indicators.NOTHING, classes.indicators.NOTHING, classes.indicators.NOTHING, classes.indicators.NOTHING, e0, classes.indicators.NOTHING, classes.indicators.NOTHING, classes.indicators.NOTHING, r0)

def INT_FLOAT_FLOAT_FLOAT(file, item_list, i):
    e = 0
    r, rr, rrr = 0.0
    array = [float(x) for x in file.readline().split()]
    e = int(array[0])
    r = array[1]
    rr = array[2]
    rrr = array[3]
    item_list[i].setValues(e, r, rr, rrr, classes.indicators.NOTHING, classes.indicators.NOTHING, classes.indicators.NOTHING, classes.indicators.NOTHING, classes.indicators.NOTHING)

def INT_INT_INT_INT_INT(file, item_list, i):
    e1, e2, e3, e4, e5 = 0
    array = [int(x) for x in file.readline().split()]
    e1 = array[0]
    e2 = array[1]
    e3 = array[2]
    e4 = array[3]
    e5 = array[4]
    item_list[i].setValues(e1, classes.indicators.NOTHING, classes.indicators.NOTHING, classes.indicators.NOTHING, e2, e3, e4, e5, classes.indicators.NOTHING)

switch = {
    classes.modes.INT_FLOAT: INT_FLOAT,
    classes.modes.INT_FLOAT_FLOAT_FLOAT: INT_FLOAT_FLOAT_FLOAT,
    classes.modes.INT_INT_INT_INT_INT: INT_INT_INT_INT_INT
}


def obtenerDatos(file, nlines, n, mode, item_list):
    line = ""
#    file = open("3dtest.dat", "r")
#    line = file.readline()
    if(nlines == classes.lines.DOUBLELINE):
        line = file.readline()
    for i in range(n):
        switch[mode](file, item_list, i)

def correctConditions(n, list, indices):
    for i in range(n):
        indices[i] = list[i].getNode1()
    
    for i in range(n-1):
        pivot = list[i].getNode1()
        for j in range(i, n):
            if(list[j].getNode1() > pivot):
                list[j].setNode1(list[j].getNode1()-1)

def addExtension(newFileName, filename, extension):
    tupla = (filename, extension)
    newFileName = "".join(tupla)

def leerMallayCondiciones(m, filename):
    inputFileName = []
    k, Q = 0.0
    nNodes, nEltos, nDirich, nNeu = 0
    addExtension(inputFileName, filename, ".dat")
    file = open(inputFileName, "r")
    line  = [float(x) for x in file.readline().split()]
    k = line[0]
    Q = line[1]
    line = [int(x) for x in file.readline().split()]
    nNodes = line[0]
    nEltos = line[1]
    nDirich = line[2]
    nNeu = line[3]

    m.setParameters(k,Q)
    m.setSizes(nNodes, nEltos, nDirich, nNeu)
    m.createData()

    obtenerDatos(file, classes.lines.SINGLELINE, nNodes, classes.modes.INT_FLOAT_FLOAT_FLOAT, m.getNodes())
    obtenerDatos(file, classes.lines.DOUBLELINE, nEltos, classes.modes.INT_INT_INT_INT_INT, m.getElements())
    obtenerDatos(file, classes.lines.DOUBLELINE, nDirich, classes.modes.INT_FLOAT, m.getDirichlet())
    obtenerDatos(file, classes.lines.DOUBLELINE, nNeu, classes.modes.INT_FLOAT, m.getNeumann())

    file.close()
    correctConditions(nDirich, m.getDirichlet(), m.getDirichletIndices())

def findIndex(v, s, arr):
    for i in range(s):
        if(arr[i] == v):
            return True
    return False

def writeResults(m, T, filename):
    outputFilename = ""
    dirichIndices = m.getDirichletIndices()
    dirich = m.getDirichlet()

    addExtension(outputFilename, filename, ".post.res")
    file = open(outputFilename, "w")

    file.write("GiD Post Results File 1.0\n")
    file.write("Result \"Temperature\" \"Load Case 1\" 1 Scalar OnNodes\nComponentNames \"T\"\nValues\n")

    Tpos, Dpos = 0
    n = m.getSize(classes.sizes.NODES)
    nd = m.getSize(classes.sizes.DIRICHLET)
    for i in range(n):
        if(findIndex(i+1, nd, dirichIndices)):
            string = str(i+1) + " " + dirich[Dpos].getValue() + "\n"
            file.write(string)
            Dpos+= 1
        else:
            string2 = str(i+1) + " " + T[Tpos] + "\n"
            file.write(string2)
            Tpos+= 1
    
    file.write("End values\n")
    file.close()



#obtenerDatos("3dtest.dat", 0, 0, 0, 0)