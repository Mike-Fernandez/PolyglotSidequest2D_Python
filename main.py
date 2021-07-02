#This is the main file for the program
import classes
import math_tools
import sel
#Arguments are sent in through sys, and can be called upon with sys.argv
import sys


filename = []
filename.append(sys.argv[2])

#Todas se inician como arrays, pero mas adelante se definiran por las funciones como matrices o vectores
localKs = []
localBs = []
K = []
b = []
T= []

m = classes.mesh()