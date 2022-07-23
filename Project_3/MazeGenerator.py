""" A class represnting disjoint set
    A node is represented by (i,j) where i,j are the indecies of row,column (respectively)
    of the node in the nested list"""
class Disjoint(object):
    
    """Constructor,

    @type m, n : int
    @param m, n: Dimentions of the set
    Time/Space complexity of O(m*n)
    """
    def __init__(self, m = 10, n = 10):
        self.parent = [[(i,j) for j in range(max(2,n))] for i in range(max(2,m))]
        self.rank = [[0 for j in range(max(2,n))] for i in range(max(2,m))]


    
    """returns a disjoint set, 

    @type m, n : int
    @param m, n: Dimentions of the set
    @rtype: Disjoint
    @returns: returns a disjoint set, m = n = 10 are the default dimensions
    Time/Space complexity of O(m*n)
    """
    def make_set(m=10,n=10):
        return Disjoint(m,n)



    """unions two Sub-sets

    @type a, b : tuple
    @param a, b: roots of different sub-sets
    Time complexity of O(α(m*n)), where α is Inverse-Ackermann function
    """
    def union(self,a,b):
        root1 = Disjoint.find(self,a)
        root2 = Disjoint.find(self,b)
        if root1 != root2:
            if Disjoint.getRank(self,root1) > Disjoint.getRank(self,root2):
                Disjoint.setParent(self,root2,root1)
            else:
                Disjoint.setParent(self,root1,root2)
                if Disjoint.getRank(self,root1) == Disjoint.getRank(self,root2):
                    Disjoint.setRank(self,root2,self.getRank(root2)+1)


    
    """finds the root of a Sub-sets

    @type a : tuple
    @param a : root of a sub-sets
    Time complexity of O(α(m*n)), where α is Inverse-Ackermann function
    """
    def find(self,e):
        if self:
            if e != Disjoint.getParent(self,e):
                Disjoint.setParent(self,e,Disjoint.find(self,Disjoint.getParent(self,e)))
            return Disjoint.getParent(self,e)


    
    """return the whole set

    @rtype: list
    @returns: nested list of all nodes, None if self is None
    Time/Space complexity of O(1)
    """
    def getSet(self):
        return None if not self else self.parent



    """returns the Parent of a given Node
    @rtype: tuple
    @returns: the Parent of a given Node , None if e is None
    Time/Space complexity of O(1)
    """
    def getParent(self,e):
        return None if not self else self.parent[e[0]][e[1]]



    """sets Parent of a node
    @type e, parent: tuple
    @param e,parent : nodes
    Time/Space complexity of O(1)
    """
    def setParent(self,e,parent):
        if self:
            self.parent[e[0]][e[1]] = parent



    """returns the rank of a given Node
    @rtype: int
    @returns: the rank of a given Node , -1 if root is None
    Time/Space complexity of O(1)
    """
    def getRank(self,root):
        return -1 if not self else self.rank[root[0]][root[1]]



    """sets Rank of a node
    @type root, val: tuple, int
    @param root,val : node, int
    Time/Space complexity of O(1)
    """
    def setRank(self,root,val):
        if self:
            self.rank[root[0]][root[1]] = val



    # 'Junction' functions :

    """unions two Sub-sets
    @type i, j, x, y : int
    @param (i,j), (x,y): roots of different sub-sets
    Time complexity of O(α(m*n)), where α is Inverse-Ackermann function
    """
    def Union(self,i,j,x,y):
        a = (i,j)
        b = (x,y)
        Disjoint.union(self,a,b)


    """finds the root of a Sub-sets
    @type i, j : int
    @param (i,j) : root of a sub-sets
    Time complexity of O(α(m*n)), where α is Inverse-Ackermann function
    """
    def Find(self,i,j):
        e = (i,j)
        return Disjoint.find(self,e)






""" A class represnting a Maze with disjoint sets
    A square is represented by (i,j) where i,j are the indecies of row,column (respectively)
    of the square in the nested list"""
import random
class Maze(object):

    """Constructor,

    @type m, n : int
    @param m, n: Dimentions of the maze
    Time/Space complexity of O(m*n)
    """
    def __init__(self,m=10,n=10):
        self.maze = Disjoint.make_set(m,n)
        self.m = m
        self.n = n




    """generating a maze by randomly connecting two neighboring nodes

    Expected Time complexity of O((m*n)*α(m*n)), where α is Inverse-Ackermann function
    note that the time complexity might not be bounded, but Expected it'll be ok
    """
    def generateMaze(self):
        if self :
            Maze.setNewMaze(self,self.m,self.n)
            maze = Maze.getMaze(self)
            disjoint = Disjoint.getSet(maze)
            numRows = len(disjoint)
            numCols = len(disjoint[0])
            numCells = numRows*numCols

            start = (0,0)
            goal = (numRows-1,numCols-1)
            edge = (0,0)
            while (maze.getParent(start) != maze.getParent(goal)):
                #i,j = random.randint(0,numRows-1),random.randint(0,numCols-1)
                a,b = Maze.randEdge(edge[0],edge[1],numRows,numCols)
                
                if Disjoint.find(maze,edge) != Disjoint.Find(maze,a,b):
                    maze.Union(edge[0],edge[1],a,b)
                edge = (a,b)




    """returns the maze
    @rtype: Disjoint
    @returns: the disjoint set representing the maze, None if e is None
    Time/Space complexity of O(1)
    """
    def getMaze(self):
        return None if not self else self.maze




    """resets the maze
    @type m, n : int
    @param m, n: Dimentions of the maze
    Time/Space complexity of O(m*n)
    """
    def setNewMaze(self,m=10,n=10):
        if self:
            self.maze = Disjoint.make_set(m,n)




    """choosing random neighbor of square (i,j)
    @type i, j, r, c : int
    @param (i, j) , r, c: a square and the Dimentions of the maze
    Time/Space complexity of O(1)
    """ 
    def randEdge(i,j,r,c):
        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        legal = []
        for (x,y) in directions:
            if 0 <= i+x < r and 0 <= j+y < c :
                legal.append((x,y))
        a,b = random.choice(legal)
        return (i+a,j+b)




    



