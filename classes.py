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
    INT_FLOAT_FLOAT = auto()
    INT_INT_INT_INT = auto()
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

    def setValues(a,b,c,d,e,f,g):
        None

class node(item):
    def setValues(self,a, b, c, d, e, f, g):
        self.id = a
        self.x = b
        self.y = c

class element(item):
    def setValues(self,a, b, c, d, e, f, g):
        self.id = a
        self.node1 = d
        self.node2 = e
        self.node3 = f

class condition(item):
    def setValues(self,a, b, c, d, e, f, g):
        self.node1 = d
        self.value = g


class mesh:
    def __init__(self):
        self.parameters = [2]
        self.sizes = [4]
        self.node_list = []
        self.element_list = []
        self.indices_dirich = []
        self.direchlet_list = []
        self.neumann_list = []

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
        self.direchlet_list = [self.sizes[sizes.DIRICHLET]]
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
