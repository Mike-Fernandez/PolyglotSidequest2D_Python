#This is the main file for the program

#Arguments are sent in through sys, and can be called upon with sys.argv
import sys
import array as arr
import numpy as np

filename = []

filename.append(sys.argv[2])

localKs = np.array(np.matrix({}))
localBs = np.array(np.array({}))

K = np.matrix({})
b = np.array({})
T = np.array({})





print(filename[0])