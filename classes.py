indicators = {
    "NOTHING": 0
}
lines = {
    "NOLINE": 0,
    "SINGLELINE": 1,
    "DOUBLELINE": 2
}
modes = {
    "NOMODE": 0,
    "INT_FLOAT" : 1,
    "INT_FLOAT_FLOAT_FLOAT" : 2,
    "INT_INT_INT_INT_INT" : 3
}
parameters = {
    "THERMAL_CONDUCTIVITY": 0,
    "HEAT_SOURCE" : 1
}
sizes ={
    "NODES" : 0,
    "ELEMENTS" : 1,
    "DIRICHLET" : 2,
    "NEUMANN" : 3
}

class item:
    def __init__(self):

        self.id = None
        self.x = None
        self.y = None
        self.z = None
        self.node1 = None
        self.node2 = None
        self.node3 = None
        self.node4 = None
        self.value = None

    def setID(self, identifier):
        self.id = identifier

    def setX(self, x_coord):
        self.x = x_coord

    def setY(self, y_coord):
        self.y = y_coord
    
    def setZ(self, z_coord):
        self.z = z_coord

    def setNode1(self, node_1):
        self.node1 = node_1

    def setNode2(self, node_2):
        self.node2 = node_2

    def setNode3(self, node_3):
        self.node3 = node_3

    def setNode4(self, node_4):
        self.node4 = node_4

    def setValue(self, value_to_assign):
        self.value = value_to_assign

    def getID(self):
        return self.id

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getNode1(self):
        return self.node1

    def getNode2(self):
        return self.node_2

    def getNode3(self):
        return self.node_3

    def getNode4(self):
        return self.node_4

    def getValue(self):
        return self.value

    def setValues(a,b,c,d,e,f,g, h, i):
        None

class node(item):
    def setValues(self,a, b, c, d, e, f, g, h, i):
        self.id = a
        self.x = b
        self.y = c
        self.z = d

class element(item):
    def setValues(self,a, b, c, d, e, f, g, h, i):
        self.id = a
        self.node1 = e
        self.node2 = f
        self.node3 = g
        self.node4 = h

class condition(item):
    def setValues(self,a, b, c, d, e, f, g, h, i):
        self.node1 = e
        self.value = i


class mesh:
    def __init__(self):
        self.parameters = [None for n in range(2)]
        self.sizes = [None for n in range(4)]
        self.node_list = []
        self.element_list = []
        self.indices_dirich = []
        self.dirichlet_list = []
        self.neumann_list = []

    def setParameters(self,k,Q):
        self.parameters[parameters["THERMAL_CONDUCTIVITY"]] = k
        self.parameters[parameters["HEAT_SOURCE"]] = Q

    def setSizes(self,nnodes,neltos,ndirich,nneu):
        self.sizes[sizes["NODES"]] = nnodes
        self.sizes[sizes["ELEMENTS"]] = neltos
        self.sizes[sizes["DIRICHLET"]] = ndirich        
        self.sizes[sizes["NEUMANN"]] = nneu

    def getSize(self,s):
        return self.sizes[s]

    def getParameter(self,p):
        return self.parameters[p]

    def createData(self):
        for n in range(self.sizes[sizes["NODES"]]):
            self.node_list.append(node)
#        self.node_list = [node for n in range(self.sizes[sizes["NODES"]])]
                    #d = [ [ None for y in range( 2 ) ] for x in range( 2 ) ]
        self.element_list = [element for n in range(self.sizes[sizes["ELEMENTS"]])]
        self.indices_dirich = [int for n in range(self.sizes[sizes["DIRICHLET"]])]
        self.dirichlet_list = [condition for n in range(self.sizes[sizes["DIRICHLET"]])]
        self.neumann_list = [condition for n in range(self.sizes[sizes["NEUMANN"]])] 

    def getNodes(self):
        return self.node_list

    def getElements(self):
        return self.element_list

    def getDirichletIndices(self):
        return self.indices_dirich

    def getDirichlet(self):
        return self.dirichlet_list

    def getNeumann(self):
        return self.neumann_list

    def getNode(self,i):
        return self.node_list[i]

    def getElement(self,i):
        return self.element_list[i]

    def getCondition(self,i,type):
        if(type == sizes["DIRICHLET"]):
            return self.direchlet_list[i]
        else:
            return self.neumann_list[i]
