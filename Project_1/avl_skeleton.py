#username - complete info
#id1      - complete info 
#name1    - complete info 
#id2      - complete info
#name2    - complete info  



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
    """Constructor, you are allowed to add more fields. 

    @type value: str
    @param value: data of your node
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1  # remember please!!!!!
        self.size = 0   # remember please!!!!!
        

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """
    
    def getLeft(self):
        if not self:
                return None
        return self.left


    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """
    def getRight(self):
        if not self:
                return None
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """
    def getParent(self):
        if not self:
                return None
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """
    def getValue(self):
        if not self:
                return None
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """
    def getHeight(self):#the case when asking an empty tree for height , we will send the root as an argument , but the tree is empty iff self.root == None
        if not self:
                return -1
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """
    def setLeft(self, node):#always check if you can insert before insertion. and check the virtual Node
        if self:
                self.left = node
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """
    def setRight(self, node):
        if self:
                self.right = node
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """
    def setParent(self, node):
        if self:
                self.parent = node
        return None

    """sets value

    @type value: str
    @param value: data
    """
    def setValue(self, value):
        if self:
                self.value = value
        return None

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """
    def setHeight(self, h):
        if self:
                self.height = h
        return None

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """
    def isRealNode(self):
        return AVLNode.getHeight(self) != -1

    # help methods :

    def getSize(self):
        if not self:
            return 0
        return self.size
    
    def setSize(self,s):
        if self:
            self.size = s

    def BF(self):
        if not self:
            return 0 #"check yourself-balance"
        return AVLNode.getHeight(AVLNode.getLeft(self)) - AVLNode.getHeight(AVLNode.getRight(self))


"""
A class implementing the ADT list, using an AVL tree.
"""

class AVLTreeList(object):

    """
    Constructor, you are allowed to add more fields.  

    """
    def __init__(self):
        self.root = None
        self._min = None
        self._max = None


    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """
    def empty(self):
        return AVLNode.getHeight(self.root) == -1  #check one more time the definition of an empty tree
        #I think the definition is implementor's decision

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """
    def retrieve(self, i):
        return AVLNode.getValue(self.select(self.root,i+1))

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def insert(self, i, val):

        # set up the insertion node
        to_insert = AVLNode(val)
        to_insert.setHeight(0)
        to_insert.setSize(1)
        to_insert.setLeft(AVLNode(None))
        to_insert.setRight(AVLNode(None))
        to_insert.getLeft().setParent(to_insert)
        to_insert.getRight().setParent(to_insert)

        #Edge case
        if AVLTreeList.empty(self) :
            self.root = to_insert
            self._min = to_insert
            self._max = to_insert
            return 1

        if (i==0):
            succ=self._min 
            succ.setLeft(to_insert)
            to_insert.setParent(succ)
            self._min = to_insert
        elif i == self.length():
            pred = self._max
            pred.setRight(to_insert)
            to_insert.setParent(pred)
            self._max = to_insert

        #insertion
        else:
            pred = AVLTreeList.select(self,self.root,i)
            if not AVLNode.isRealNode(pred.getRight()):
                pred.setRight(to_insert)
                to_insert.setParent(pred)
            else:
                succ = AVLTreeList.successor(self,pred)
                succ.setLeft(to_insert)
                to_insert.setParent(succ)
        #rotations and updates    
        tmpParent = to_insert.getParent()
        count = 0
        yet = True
        while(tmpParent):
            tmpParent.setSize(AVLNode.getSize(tmpParent.getLeft()) + AVLNode.getSize(tmpParent.getRight())+1) 
            if yet:
                prev_height = tmpParent.getHeight()
                tmpParent.setHeight(max(AVLNode.getHeight(tmpParent.getLeft()),AVLNode.getHeight(tmpParent.getRight()))+1)
                changed = not (prev_height == tmpParent.getHeight())
                if changed:
                    count += 1
            
                bf = abs(tmpParent.BF()) 

                if bf < 2 and not changed:
                    yet = False
                if bf == 2:
                    count += self.rotation(tmpParent)
                    yet = False
            tmpParent = tmpParent.getParent()
                    
        return count


    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """
    def delete(self, i):
        return -1


    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """
    def first(self):
        if not self:
            return self
        return None if empty(self) else AVLNode.getValue(self._min)

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """
    def last(self):
        if not self:
            return self
        return None if empty(self) else AVLNode.getValue(self._max)

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """
    def listToArray(self):
        res = []
        node = self._min
        while (node != None):
            res.append(node.getValue())
            node = AVLTreeList.successor(self,node)
        return res
        
        

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """
    def length(self):
        if not self:
            return 0
        return 0 if self.empty() else self.root.getSize()

    """splits the list at the i'th index

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list according to whom we split
    @rtype: list
    @returns: a list [left, val, right], where left is an AVLTreeList representing the list until index i-1,
    right is an AVLTreeList representing the list from index i+1, and val is the value at the i'th index.
    """
    def split(self, i):
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    def concat(self, lst):
        return None

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """
    def search(self, val):
        curr = self._min
        i = 0
        while(curr and curr.getValue() != val):
            curr = self.successor(curr)
            i += 1
        if curr == None:
            return -1
        else:
            return i



    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """
    def getRoot(self):
        if not self:
            return self
        return self.root

#################################################################################

    #helper functions 

    def select(self,node,i):#  returns a node , we send a sub-tree and an index as an input
        rank = node.getLeft().getSize() + 1
        while rank != i:
            if rank > i:
                node = node.getLeft()
                rank = node.getLeft().getSize() + 1
            elif rank < i:
                i = i - rank
                node = node.getRight()
                rank = node.getLeft().getSize() + 1
        return node

    

    def Min(self,node):
        if not node:
            return "check yourself-Min"
        left = AVLNode.getLeft(node)
        while left.getHeight() != -1:
            node = left
            left = node.getLeft()
        return node

    def successor(self,node):
        right = AVLNode.getRight(node)
        if AVLNode.getHeight(right) != -1:
            return AVLTreeList.Min(self,right)
        y = node.getParent()
        while y and node == AVLNode.getRight(y):
            node = y
            y = node.getParent()
        return y

    def rotate(self,criminal,is_right):
        f_root = criminal == self.root
        father = criminal.getParent()
        f_left = AVLNode.getLeft(father) == criminal
        if is_right:
            son = criminal.getLeft()
            criminal.setLeft(son.getRight())
            criminal.getLeft().setParent(criminal)
            son.setRight(criminal)
        else:
            son = criminal.getRight()
            criminal.setRight(son.getLeft())
            criminal.getRight().setParent(criminal)
            son.setLeft(criminal)
        criminal.setHeight(max(AVLNode.getHeight(AVLNode.getLeft(criminal)),AVLNode.getHeight(AVLNode.getRight(criminal)))+1)
        son.setHeight(max(AVLNode.getHeight(AVLNode.getLeft(son)),AVLNode.getHeight(AVLNode.getRight(son)))+1)
        AVLNode.setParent(son,father)
        criminal.setParent(son)
        if f_left:
            AVLNode.setLeft(father,son)
        else:
            AVLNode.setRight(father,son)
        AVLNode.setHeight(father,max(AVLNode.getHeight(AVLNode.getLeft(father)),AVLNode.getHeight(AVLNode.getRight(father)))+1)
        son.setSize(criminal.getSize())
        criminal.setSize(AVLNode.getSize(AVLNode.getLeft(criminal))+AVLNode.getSize(AVLNode.getRight(criminal))+1)
        if f_root:
            self.root = son


    def rotation(self,criminal):
        bf = criminal.BF()
        if bf == 2:
            son_bf = criminal.getLeft().BF()
            if son_bf == 1:
                AVLTreeList.rotate(self,criminal,True)
                return 1
            if son_bf == -1:
                AVLTreeList.rotate(self,criminal.getLeft(),False)
                AVLTreeList.rotate(self,criminal,True)
                return 2
                
        elif bf == -2:
            son_bf = criminal.getRight().BF()
            if son_bf == -1:
                AVLTreeList.rotate(self,criminal,False)
                return 1
            if son_bf == 1:
                AVLTreeList.rotate(self,criminal.getRight(),True)
                AVLTreeList.rotate(self,criminal,False)
                return 2
            
        
       
        
def test():
    '''t = AVLTreeList()
    t.root = AVLNode(5)
    
    b = t.root
    b.setHeight(2)
    b.setSize(3)
    a = AVLNode(4)
    a.setParent(b)
    b.setLeft(a)
    a.setHeight(1)
    a.setSize(2)
    c = AVLNode(3)
    c.setParent(a)
    a.setLeft(c)
    c.setSize(1)
    c.setHeight(0)
    c.setLeft(AVLNode(None))
    c.setRight(AVLNode(None))
    a.setRight(AVLNode(None))
    b.setRight(AVLNode(None))
    c.getLeft().setParent(c)
    c.getRight().setParent(c)
    a.getRight().setParent(a)
    b.getRight().setParent(b)
    d = AVLNode(6)
    d.setLeft(b)
    d.setSize(4)
    d.setHeight(3)
    b.setParent(d)
    print(str(d.getLeft() == b) + " b's parent is d")
    print(str(t.successor(c) == a) + "   successor")
    print(str(t.successor(a) == b) + "   successor")
    t.rotate(b,True)
    print(c.getParent() == b.getParent())
    print(str(b.getParent() == a) + " check b's parent")
    print(str(d.getLeft() == a) + " b's parent is now a's")'''
    
    '''t = AVLTreeList()
    t.root = AVLNode(5)
    
    b = t.root
    b.setHeight(2)
    b.setSize(3)
    a = AVLNode(4)
    a.setParent(b)
    b.setRight(a)
    a.setHeight(1)
    a.setSize(2)
    c = AVLNode(3)
    c.setParent(a)
    a.setRight(c)
    c.setSize(1)
    c.setHeight(0)
    c.setLeft(AVLNode(None))
    c.setRight(AVLNode(None))
    a.setLeft(AVLNode(None))
    b.setLeft(AVLNode(None))
    c.getLeft().setParent(c)
    c.getRight().setParent(c)
    a.getLeft().setParent(a)
    b.getLeft().setParent(b)
    d = AVLNode(6)
    d.setRight(b)
    d.setSize(4)
    d.setHeight(3)
    b.setParent(d)
    t._min = b
    t._max = c'''
    
    '''print(str(d.getRight() == b) + " b's parent is d")
    print(str(AVLNode.getHeight(t.successor(c)) == -1) + "   c's successor")
    print(str(t.successor(a) == c) + "   a's successor")
    t.rotate(b,False)
    print(t.retrieve(3))
    print(c.getParent() == b.getParent())
    print(str(b.getParent() == a) + " check b's parent")
    print(str(d.getRight() == a) + " b's parent is now a's")'''
    
    

    t = AVLTreeList()


    t.insert(0,"a")
    t.insert(1,"b")
    t.insert(2,"c")
    t.insert(3,"d")
    t.insert(4,"e")
    t.insert(5,"f")
    print("size of root=  "+str(t.root.getSize()))
    print("size of left=  "+str(t.root.getLeft().getSize()))
    print("size of right=  "+str(t.root.getRight().getSize()))
    print(t.root.getHeight())
    print(t.root.getLeft().getHeight())
    print(t.root.getRight().getHeight())

    print(t.listToArray())
    print(t.root.getValue())
    print(t.root.getRight().getValue())
    
    
            




    
