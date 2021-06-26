import classes

def INT_FLOAT(file):
    e0 = 0
    r0 = 0.0
    e0 = file.read()

def obtenerDatos(file, nlines, n, mode, item_list):
    line = ""
    file = open("3dtest.dat", "r")
#    line = file.readline()
    if(nlines == classes.lines.DOUBLELINE):
        line = file.readline()
#    for i in range(n):
    e0 = 0
    r0 = 0.0
    array  = [float(x) for x in file.readline().split()]
    e0 = array[0]
    r0 = array[1]
    print("e0"+ str(e0))
    print("r0"+ str(r0))

obtenerDatos("3dtest.dat", 0, 0, 0, 0)