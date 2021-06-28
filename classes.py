from enum import Enum,auto
class indicators(Enum):
    NOTHING = auto()
class lines(Enum):
    NOLINE = auto()
    SINGLELINE = auto()
    DOUBLELINE = auto()
class modes(Enum):
    NOMODE = auto()
    INT_FLOAT = auto()
    INT_FLOAT_FLOAT_FLOAT = auto()
    INT_INT_INT_INT_INT = auto()
class parameters(Enum):
    THERMAL_CONDUCTIVITY = auto()
    HEAT_SOURCE = auto()
class sizes(Enum):
    NODES = auto()
    ELEMENTS = auto()
    DIRICHLET = auto()
    NEUMANN = auto()

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

    def setID(identifier):
        id = identifier

    def setX(x_coord):
        x = x_coord

    def setY(y_coord):
        y = y_coord
    
    def setZ(z_coord):
        z = z_coord

    def setNode1(node_1):
        node1 = node_1

    def setNode2(node_2):
        node2 = node_2

    def setNode3(node_3):
        node3 = node_3

    def setNode4(node_4):
        node4 = node_4

    def setValue(value_to_assign):
        value = value_to_assign

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
        node2 = self.node_2

    def getNode3(self):
        node3 = self.node_3

    def getNode4(self):
        node4 = self.node_4

    def getValue(self):
        value = self.value_to_assign

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
        self.parameters = [2]
        self.sizes = [4]
        self.node_list = [float]
        self.element_list = [float]
        self.indices_dirich = [float]
        self.dirichlet_list = [float]
        self.neumann_list = [float]

    def setParameters(self,k,Q):
        self.parameters[parameters.THERMAL_CONDUCTIVITY] = k
        self.parameters[parameters.HEAT_SOURCE] = Q

    def setSizes(self,nnodes,neltos,ndirich,nneu):
        self.sizes[sizes.NODES] = nnodes
        self.sizes[sizes.ELEMENTS] = neltos
        self.sizes[sizes.DIRICHLET] = ndirich        
        self.sizes[sizes.NEUMANN] = nneu

    def getSize(self,s):
        return self.sizes[s]

    def getParameter(self,p):
        return self.parameters[p]

    def createData(self):
        self.node_list = [self.sizes[sizes.NODES]]
        self.element_list = [self.sizes[sizes.ELEMENTS]]
        self.indices_dirich = [self.sizes[sizes.DIRICHLET]]
        self.dirichlet_list = [self.sizes[sizes.DIRICHLET]]
        self.neumann_list = [self.sizes[sizes.NEUMANN]]

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
        if(type == sizes.DIRICHLET):
            return self.direchlet_list[i]
        else:
            return self.neumann_list[i]
