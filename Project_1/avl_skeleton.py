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
        return AVLNode.getHeight(AVLTreeList.getRoot(self)) == -1  #check one more time the definition of an empty tree
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
            return 0   ####

        if i == self.length():
            self._max.setRight(to_insert)
            to_insert.setParent(self._max)
            self._max = to_insert
        
        else:
            succ = AVLTreeList.select(self,self.root,i+1)
            if not AVLNode.isRealNode(succ.getLeft()):
                succ.setLeft(to_insert)
                to_insert.setParent(succ)
            else:
                pre = AVLTreeList.predecessor(self,succ)
                pre.setRight(to_insert)
                to_insert.setParent(pre)
        if i == 0:
            self._min = to_insert

        
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

                '''if bf < 2 and not changed:
                    yet = False'''
                if bf == 2:
                    count += self.rotation(tmpParent)
                    if changed:
                        count -= 1
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

        if i == 0 and i == self.length()-1:
            self.root = None
            self._min = None
            self._max = None
            return 0
        
        to_delete = self.select(self.root,i+1)
        father = to_delete.getParent()
        succ = self.successor(to_delete)
        is_root = to_delete == self.root
        if i == 0:
            self._min = succ
        if i == self.length() - 1:
            self._max = self.predecessor(to_delete)
        if_left = AVLNode.getLeft(father) == to_delete
        getter_father = (lambda x : AVLNode.getLeft(x)) if if_left else (lambda x : AVLNode.getRight(x))
        setter_father = (lambda x : AVLNode.setLeft(father,x)) if if_left else (lambda x : AVLNode.setRight(father,x))
        tmpParent = None
        if to_delete.getSize() == 1:
            setter_father(AVLNode(None))
            AVLNode.setParent(getter_father(father),father)
            tmpParent = father
        elif (to_delete.getLeft().isRealNode()) and to_delete.getRight().isRealNode():
            if to_delete.getRight() == succ:
                setter_father(succ)
                succ.setLeft(to_delete.getLeft())
                succ.getLeft().setParent(succ)
                AVLNode.setParent(succ,father)
                tmpParent = succ
            else:
                succ.getRight().setParent(succ.getParent())
                succ.getParent().setLeft(succ.getRight())
                tmpParent = succ.getParent()
                succ.setLeft(to_delete.getLeft())
                succ.setRight(to_delete.getRight())
                succ.setHeight(to_delete.getHeight())
                succ.setSize(to_delete.getSize())
                succ.setParent(to_delete.getParent())
            if is_root:
                self.root = succ
                
        else:
            node = to_delete.getLeft() if to_delete.getLeft().isRealNode() else to_delete.getRight()
            node.setParent(father)
            setter_father(node)
            tmpParent = father
            if is_root:
                self.root = node
            

        count = 0
        yet = True
        while tmpParent:
            tmpParent.setSize(AVLNode.getSize(tmpParent.getLeft()) + AVLNode.getSize(tmpParent.getRight())+1)
            if yet:
                prev_height = tmpParent.getHeight()
                tmpParent.setHeight(max(AVLNode.getHeight(tmpParent.getLeft()),AVLNode.getHeight(tmpParent.getRight()))+1)
                changed = not (prev_height == tmpParent.getHeight())
                if changed:
                    count += 1
            
                bf = abs(tmpParent.BF()) 

                '''if bf < 2 and not changed:
                    print ( "stoped her") 
                    yet = False'''
                if bf == 2:
                    count += self.rotation(tmpParent)
                    if changed:
                        count -= 1
            tmpParent = tmpParent.getParent()

        return count



    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """
    def first(self):
        if not self:
            return self
        return None if AVLTreeList.empty(self) else AVLNode.getValue(self._min)

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """
    def last(self):
        if not self:
            return self
        return None if AVLTreeList.empty(self) else AVLNode.getValue(self._max)

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
        to_split = self.select(self.root,i+1)
        
        return None

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    def concat(self, lst):

        self_height ,lst_height = AVLNode.getHeight(AVLTreeList.getRoot(self)) ,AVLNode.getHeight(AVLTreeList.getRoot(lst))
        if AVLTreeList.empty(lst):
            return abs(self_height - lst_height)
        if AVLTreeList.empty(self):
            self.root = lst.root 
            self._max = lst._max
            self._min = lst._min
            return abs(self_height - lst_height)
        x = self._max
        self.delete(self.length()-1)
        self._max = lst._max
        self.root = self.join(AVLTreeList.getRoot(self),x,AVLTreeList.getRoot(lst))
        return abs(self_height - lst_height)

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

    

    def MinMax(self,node,key):
        if not node:
            return "check yourself-Min"
        nxt = key(node)
        while AVLNode.getHeight(nxt) != -1:
            node = nxt
            nxt = key(node)
        return node


    def successor(self,node):
        right = AVLNode.getRight(node)
        if AVLNode.getHeight(right) != -1:
            return AVLTreeList.MinMax(self,right,lambda x : AVLNode.getLeft(x))
        y = node.getParent()
        while y and node == AVLNode.getRight(y):
            node = y
            y = node.getParent()
        return y

    def predecessor(self,node):
        left = AVLNode.getLeft(node)
        if AVLNode.getHeight(left) != -1:
            return AVLTreeList.MinMax(self,left,lambda x : AVLNode.getRight(x))
        y = node.getParent()
        while y and node == AVLNode.getLeft(y):
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
        bf = AVLNode.BF(criminal)
        if bf == 2:
            son_bf = AVLNode.BF(AVLNode.getLeft(criminal))
            if son_bf >= 0:
                AVLTreeList.rotate(self,criminal,True)
                return 1
            if son_bf == -1:
                AVLTreeList.rotate(self,criminal.getLeft(),False)
                AVLTreeList.rotate(self,criminal,True)
                return 2
                
        elif bf == -2:
            son_bf = AVLNode.BF(AVLNode.getRight(criminal))
            if son_bf <= 0:
                AVLTreeList.rotate(self,criminal,False)
                return 1
            if son_bf == 1:
                AVLTreeList.rotate(self,criminal.getRight(),True)
                AVLTreeList.rotate(self,criminal,False)
                return 2


    def join(self,node1,x,node2):
        if not node1:
            node1 = AVLNode(None)
        if not node2:
            node2 = AVLNode(None)
        if AVLNode.getHeight(node1) < AVLNode.getHeight(node2):
            tmp = node2
            while AVLNode.getHeight(tmp) > AVLNode.getHeight(node1):
                tmp = AVLNode.getLeft(tmp)
            x.setLeft(node1)
            x.setRight(tmp)
            x.setHeight(max(AVLNode.getHeight(tmp),AVLNode.getHeight(node1))+1)
            x.setSize(AVLNode.getSize(tmp) + AVLNode.getHeight(node1) + 1)
            x.setParent(AVLNode.getParent(tmp))
            AVLNode.setLeft(AVLNode.getParent(tmp),x)
            AVLNode.setParent(tmp,x)
            AVLNode.setParent(node1,x)
        else:
            tmp = node1
            while AVLNode.getHeight(tmp) > AVLNode.getHeight(node2):
                tmp = AVLNode.getRight(tmp)
            x.setLeft(tmp)
            x.setRight(node2)
            x.setHeight(max(AVLNode.getHeight(tmp),AVLNode.getHeight(node2))+1)
            x.setSize(AVLNode.getSize(tmp) + AVLNode.getHeight(node2) + 1)
            x.setParent(AVLNode.getParent(tmp))
            AVLNode.setRight(AVLNode.getParent(tmp),x)
            AVLNode.setParent(tmp,x)
            AVLNode.setParent(node2,x)
        tmpParent = x
        root = tmpParent
        while tmpParent:
            AVLNode.setSize(tmpParent,AVLNode.getSize(AVLNode.getLeft(tmpParent)) + AVLNode.getSize(AVLNode.getRight(tmpParent))+1)
            AVLNode.setHeight(tmpParent,max(AVLNode.getHeight(AVLNode.getLeft(tmpParent)),AVLNode.getHeight(AVLNode.getRight(tmpParent)))+1)
            bf = abs(AVLNode.BF(tmpParent)) 
            if bf == 2:
                self.rotation(tmpParent)
            root = tmpParent
            tmpParent = AVLNode.getParent(tmpParent)
            
        return root
        
            

            
        
       
        
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
    
    

    '''t = AVLTreeList()


    t.insert(0,"a")
    print("after inserting first \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    
    t.insert(1,"b")
    print("after inserting second \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    t.insert(2,"c")
    print("after inserting third \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    t.insert(3,"d")
    print("after inserting fourth \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    t.insert(4,"e")
    print("after inserting fifth \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    t.insert(5,"f")
    print("after inserting sixth \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")

    t.insert(2,'r')
    print("after inserting seventh \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    t.insert(5,'z')
    print("after inserting eighth \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    t.insert(2,'x')
    print("after inserting nineth \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    t.delete(3)
    print("after deleting index 3 \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")

    t.delete(3)
    print("after deleting index 3 \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")

    t.delete(3)
    print("after deleting index 3 \n")
    print("\n")
    print("\n")
    print("\n")
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")'''
    '''t = AVLTreeList()
    
    
    
    t.insert(0,15)
    t.insert(0,8)
    t.insert(2,22)
    t.insert(0,4)
    t.insert(3,20)
    t.insert(2,11)
    t.insert(6,24)
    t.insert(0,2)
    t.insert(5,18)
    t.insert(3,9)
    t.insert(5,12)
    t.insert(6,13)
    print2D(t.root)
    print("\n")
    print("\n")
    print("\n")
    print ("rrrrrrrrrrr"+ str(t.delete(11)))
    #t.delete(3)
    print2D(t.root)
    
    print("\n")
    print("\n")
    print("\n")

    #t.delete(3)

    print2D(t.root)
    
    print("\n")
    print("\n")
    print("\n")'''

    '''t.insert(0,'a')
    t.insert(1,'b')
    print(t.insert(2,'c'))
    print(t.delete(2))'''


    t1 = AVLTreeList()
    t2= AVLTreeList()
    '''t1.insert(0,"y")
    t1.insert(1,"x")
    t1.insert(2,"z")
    t1.insert(2,"w")
    t1.insert(4,'m')'''

    t2.insert(0,"b")
    t2.insert(1,"a")
    t2.insert(2,"g")
    t2.insert(2,"f")
    t2.insert(1,'e')
    t2.insert(0,"c")
    t2.insert(0,'d')
    print("t1 before concat")
    #print2D(t1.root)
    print("t2 before concat")
    print2D(t2.root)

    print(AVLTreeList.concat(t1,t2))
    print("t1 after concat")
    print(t2.root.value)
    print(t2._min.value)
    print(t2._max.value)
    print2D(t1.root)
    print("t2 after concat")
    print2D(t2.root)
    

    





    
    
    
COUNT = [10]    
def print2DUtil(root, space) :
 
    # Base case
    if (root == None) :
        return
 
    # Increase distance between levels
    space += COUNT[0]
 
    # Process right child first
    print2DUtil(root.right, space)
 
    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end = " ")
    print(root.value)
 
    # Process left child
    print2DUtil(root.left, space)
 
# Wrapper over print2DUtil()
def print2D(root) :
     
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)    




    
