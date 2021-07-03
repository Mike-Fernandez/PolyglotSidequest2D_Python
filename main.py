#This is the main file for the program
import classes
import math_tools
import sel
import tools
#Arguments are sent in through sys, and can be called upon with sys.argv
import sys


filename = []
filename.append(sys.argv[2])

#Todas se inician como arrays, pero mas adelante se definiran por las funciones como matrices o vectores
localKs = []
localBs = []
K = []
B = []
T= []

m = classes.mesh()

tools.leerMallayCondiciones(m,filename)

sel.crearSistemasLocales(m, localKs, localBs)

K = math_tools.zeroes(m.getSize(classes.sizes["NODES"]), m.getSize(classes.sizes["NODES"]))
math_tools.vectorZeroes(B, m.getSize(classes.sizes["NODES"]))

sel.assembly(m, localKs, localBs, K, B)

sel.applyNeumann(m, B)
sel.applyDirichlet(m, K, B)

math_tools.vectorZeroes(T, len(B))
sel.calculate(K,B,T)
tools.writeResults(m, T, filename)

