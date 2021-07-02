def showMatrix(m):
    for row in m:
        for cell in row:
            print(cell, end=" ")
        print()

def showKs(Ks):
        for K in Ks:
            print("K del elemento")
            showMatrix(K)
            print("*********************")

def showVector(v):
    print("[")
    for item in v:
        print(item)
    print("]")

def showBs(Bs):
    for B in Bs:
        print("B del elemento")
        showVector(B)
        print("*********************")