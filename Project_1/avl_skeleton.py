
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
        self.height = -1  
        self.size = 0   
        

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """
    
    def getLeft(self):#time complexity of O(1)
        if not self:
                return None
        return self.left


    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """
    def getRight(self):#time complexity of O(1)
        if not self:
                return None
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """
    def getParent(self):#time complexity of O(1)
        if not self:
                return None
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """
    def getValue(self):#time complexity of O(1)
        if not self:
                return None
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """
    def getHeight(self):#time complexity of O(1)
        if not self:
                return -1
        return self.height

    """sets left child

    @type node: AVLNode
    @param node: a node
    """
    def setLeft(self, node):#time complexity of O(1)
        if self:
                self.left = node
        return None

    """sets right child

    @type node: AVLNode
    @param node: a node
    """
    def setRight(self, node):#time complexity of O(1)
        if self:
                self.right = node
        return None

    """sets parent

    @type node: AVLNode
    @param node: a node
    """
    def setParent(self, node):#time complexity of O(1)
        if self:
                self.parent = node
        return None

    """sets value

    @type value: str
    @param value: data
    """
    def setValue(self, value):#time complexity of O(1)
        if self:
                self.value = value
        return None

    """sets the Height of the node

    @type h: int
    @param h: the height
    """
    def setHeight(self, h):#time complexity of O(1)
        if self:
                self.height = h
        return None

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """
    def isRealNode(self):#time complexity of O(1)
        return AVLNode.getHeight(self) != -1

    # help methods :

    """returns the size of subtree

    @rtype: int
    @returns: the size of the subtree where self is the root
    """
    def getSize(self):#time complexity of O(1)
        if not self:
            return 0
        return self.size
    
    """sets the Size of the node

    @type s: int
    @param s: the size of the subtree where self is the root
    """
    def setSize(self,s):#time complexity of O(1)
        if self:
            self.size = s


    """returns the balance factor

    @rtype: int
    @returns: the balance factor of the Node
    """
    def BF(self):#time complexity of O(1)
        if not self:
            return 0 
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
    def empty(self):#time complexity of O(1)
        return AVLNode.getHeight(AVLTreeList.getRoot(self)) == -1  

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """
    def retrieve(self, i):#Time complexity of O(logn)
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
    def insert(self, i, val):#Time complexity of O(logn)

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
            return 0   

        #insertion of the new Node
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
    def delete(self, i):#Time complexity of O(logn)

        #Edge case
        if i == 0 and i == self.length()-1:
            self.root = None
            self._min = None
            self._max = None
            return 0
        
        #finding the node to Delete
        to_delete = self.select(self.root,i+1)
        father = to_delete.getParent()
        succ = self.successor(to_delete)
        is_root = to_delete == self.root

        #Deletion of the Node
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
                tmpParent = succ.getParent()
                succ.getRight().setParent(tmpParent)
                tmpParent.setLeft(succ.getRight())
                
                succ.setLeft(to_delete.getLeft())
                succ.setRight(to_delete.getRight())
                AVLNode.setParent(succ.getRight(),succ)
                AVLNode.setParent(succ.getLeft(),succ)
                
                succ.setParent(father)
                setter_father(succ)
                
                succ.setHeight(to_delete.getHeight())
                succ.setSize(to_delete.getSize())
                
                
                
            if is_root:
                self.root = succ
                
        else:
            node = to_delete.getLeft() if to_delete.getLeft().isRealNode() else to_delete.getRight()
            node.setParent(father)
            setter_father(node)
            tmpParent = father
            if is_root:
                self.root = node
            
        #Updates and Rotations
        count = 0
        yet = True
        while tmpParent:
            tmpParent.setSize(AVLNode.getSize(tmpParent.getLeft()) + AVLNode.getSize(tmpParent.getRight())+1)
            prev_height = tmpParent.getHeight()
            tmpParent.setHeight(max(AVLNode.getHeight(tmpParent.getLeft()),AVLNode.getHeight(tmpParent.getRight()))+1)
            changed = not (prev_height == tmpParent.getHeight())
            if changed:
                count += 1
            
            bf = abs(tmpParent.BF()) 

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
    def first(self):#Time complexity of O(1)
        if not self:
            return self
        return None if AVLTreeList.empty(self) else AVLNode.getValue(self._min)

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """
    def last(self):#Time complexity of O(1)
        if not self:
            return self
        return None if AVLTreeList.empty(self) else AVLNode.getValue(self._max)

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """
    def listToArray(self):#Time complexity of O(n)
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
    def length(self):#Time complexity of O(1)
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
    def split(self, i):#Time complexity of O(logn)

        to_split = self.select(self.root,i+1)
        new_min = self.successor(to_split)
        new_max = self.predecessor(to_split)

        smaller = to_split.getLeft()
        larger = to_split.getRight()
        tmp = to_split
        tmpParent = to_split.getParent()
        while tmpParent:
            
            if tmpParent.getRight() == tmp:
                tmpParent.getLeft().setParent(None)
                smaller.setParent(None)
                nxtTmp = tmpParent.getParent()
                smaller = self.join(tmpParent.getLeft(),tmpParent,smaller)
                
            else:
                tmpParent.getRight().setParent(None)
                nxtTmp = tmpParent.getParent()
                larger.setParent(None)
                larger = self.join(larger,tmpParent,tmpParent.getRight())
            tmp = tmpParent
            tmpParent = nxtTmp

        t1 = AVLTreeList()
        t1.root = smaller if AVLNode.isRealNode(smaller) else None
        t1._min = self._min
        t1._max = new_max

        t2 = AVLTreeList()
        t2.root = larger if AVLNode.isRealNode(larger) else None
        t2._min = new_min
        t2._max = self._max
        
        return [t1,to_split.getValue(),t2]

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """
    def concat(self, lst):#Time complexity of O(logn)

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
    def search(self, val):#Time complexity of O(n)
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
    def getRoot(self):#Time complexity of O(1)
        if not self:
            return self
        return self.root

#################################################################################

    #helper functions
    

    """
    @type i: int
    @pre: 0 < i <= self.length()
    @param i:  The rank of the node we want.
    @type node: AVLNode 
    @param node: The sub-tree. 
    @rtype: node
    @returns: the node with rank=i in the sub tree.
    """

    def select(self,node,i): #Time Complexity of O(logn)
        
        rank = node.getLeft().getSize() + 1
        
        while rank != i:
            
            if rank > i:
                node = node.getLeft()
                
            elif rank < i:
                i = i - rank
                node = node.getRight()
            rank = node.getLeft().getSize() + 1
        
        return node

    """
    @type node: AVLNode 
    @param node: Sub-tree.
    @type key: lambda function 
    @param key: determine if return Min or Max. 
    @rtype: AVLNode  
    @returns: The node with the Minimal/ Maximal index in the sub_tree.
    """

    def MinMax(self,node,key): #Time Complexity of O(logn)
        if not node:
            return None 
        nxt = key(node)
        while AVLNode.isRealNode(nxt):
            node = nxt
            nxt = key(node)
        return node


    """
    @type node: AVLNode 
    @param node: Sub-tree. 
    @rtype: AVLNode  
    @returns: The successor of a given node.
    """


    def successor(self,node):   #Time Complexity of O(logn)
        right = AVLNode.getRight(node)
        if AVLNode.isRealNode(right):
            return AVLTreeList.MinMax(self,right,lambda x : AVLNode.getLeft(x))
        y = node.getParent()
        while y and node == AVLNode.getRight(y):
            node = y
            y = node.getParent()
        return y


    """
    @type node: AVLNode 
    @param node: Sub-tree. 
    @rtype: AVLNode  
    @returns: The perdecessor of a given node.
    """
    
    def predecessor(self,node): #Time Complexity of O(logn)
        left = AVLNode.getLeft(node)
        if AVLNode.isRealNode(left):
            return AVLTreeList.MinMax(self,left,lambda x : AVLNode.getRight(x))
        y = node.getParent()
        while y and node == AVLNode.getLeft(y):
            node = y
            y = node.getParent()
        return y


    """
    @type criminal: AVLNode 
    @param criminal: a node with BF=2.
    @type is_right: Boolean value
    @param is_right: determine if right\left rotation.
    """

    def rotate(self,criminal,is_right): #Time Complexity of O(1)
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
        AVLNode.setSize(father,AVLNode.getSize(AVLNode.getLeft(father))+AVLNode.getSize(AVLNode.getRight(father))+1)
        son.setSize(criminal.getSize())
        criminal.setSize(AVLNode.getSize(AVLNode.getLeft(criminal))+AVLNode.getSize(AVLNode.getRight(criminal))+1)
        if f_root:
            self.root = son

    """
    @type criminal: AVLNode. 
    @param criminal: a node with BF=2. 
    @rtype: int.  
    @returns: number of balance operations.
    """
    def rotation(self,criminal): #Time Complexity of O(1)
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


    """
    @type node1: AVLNode. 
    @param node1: the first sub-tree to join 
    @type node2:AVLNode. 
    @param node2: the second sub-tree to join.
    @type x: AVLNode. 
    @param x: joining node. 
    @rtype: AVLNode.  
    @returns: the root of the joined trees.
    """

    def join(self,node1,x,node2): #Time Complexity of O(|height(node1)-height(node2)+1|) 
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
    import random
    t = AVLTreeList()
    for i in range(200):
        #ind = random.randint(0,t.length())
        t.insert(t.length(),str(t.length()))
    print2D(t.getRoot())
    for i in range(200):
        #ind = random.randint(0,t.length())
        t.delete(t.length()-1)
    print2D(t.getRoot())
    print(t.search('199'))
    
    '''t=AVLTreeList()
    t.insert(0,'a')
    t.insert(1,'b')
    t2= AVLTreeList()
    t2.insert(0,'c')
    t3= AVLTreeList()
    max_= t._max
    t.delete(1)
    (x,y) = t.join(t.root,max_,t2.root)
    t3.root = x
    print(y)
    print2D(t3.root)'''
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


    '''t1 = AVLTreeList()
    t2= AVLTreeList()'''
    '''t1.insert(0,"y")
    t1.insert(1,"x")
    t1.insert(2,"z")
    t1.insert(2,"w")
    t1.insert(4,'m')'''

    '''t2.insert(0,"b")
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
    print2D(t2.root)'''

    
    '''t1.insert(0,'a')
    t1.insert(1,'b')
    t1.insert(0,'c')
    print2D(t1.root)
    lst = t1.split(2)
    print(lst)
    print2D(lst[0].root)
    print2D(lst[2].root)'''

'''
    t1 = AVLTreeList()
    t1.insert(0,'a')
    t1.insert(0,'b')
    t1.insert(2,'e')
    t1.insert(0,'c')
    t1.insert(3,'f')
    t1.insert(2,'d')
    t1.insert(6,'g')
    t1.insert(3,'k')
    t1.insert(6,'l')
    t1.insert(9,'h')
    t1.insert(2,'m')
    t1.insert(4,'p')
    #t1.delete(7)
    t1.insert(2,'s')
    #t1.delete(10)

    #print2D(t1.root)
    


    t2=AVLTreeList()
    t2.insert(0,'x')
    t2.insert(0,'y')
    t2.insert(2,'z')
    t2.insert(2,'w')
    t1.concat(t2)

    
    
    #left,val,right = t1.split(8)

    print2D(t1.root)
    print(t1.length())
    print("\n")
    print("\n")
    print("\n")
    print2D(t1.select(t1.root,5))
    succ=t1.select(t1.root,6)
    print("\n")
    print("\n")
    print("\n")
    t1.delete(4)
    print2D(t1.root)
    print("\n")
    print("\n")
    print("\n")
    print("hiiii im succ")
    print2D(succ)
    print(t1.length())
'''
    
'''
    print("\n")
    print("\n")
    print("\n")
    print(left.delete(4))
    print("after deleting the root 1")
    print("\n")
    print("\n")
    print("\n")
    print2D(left.getRoot())

    print("\n")
    print("\n")
    print("\n")
    print(t1.delete(4))
    print("after deleting the root 2")
    print("\n")
    print("\n")
    print("\n")
    print2D(t1.getRoot())


    print("\n")
    print("\n")
    print("\n")
    print(t1.delete(3))
    print("after deleting the root 3")
    print("\n")
    print("\n")
    print("\n")
    print2D(t1.getRoot())

    print("\n")
    print("\n")
    print("\n")
    print(t1.delete(3))
    print("after deleting the root 4")
    print("\n")
    print("\n")
    print("\n")
    print2D(t1.getRoot())



    print("\n")
    print("\n")
    print("\n")
    print(t1.delete(1))
    print("after deleting the root 5")
    print("\n")
    print("\n")
    print("\n")
    print2D(t1.getRoot())


    print("\n")
    print("\n")
    print("\n")
    print(t1.delete(1))
    print("after deleting the root 6")
    print("\n")
    print("\n")
    print("\n")
    print2D(t1.getRoot())

    print("\n")
    print("\n")
    print("\n")
    print(t1.delete(1))
    print("after deleting the root 7")
    print("\n")
    print("\n")
    print("\n")
    print2D(t1.getRoot())


    print("\n")
    print("\n")
    print("\n")
    print(t1.delete(0))
    print("after deleting the root 8")
    print("\n")
    print("\n")
    print("\n")
    print2D(t1.getRoot())


    '''
    







    





import random    
def insert_delete(i):
    
    t = AVLTreeList()
    count = 0
    for j in range(int(1000*(2**int(i-1)))):
        ind = random.randint(0, t.length())
        t.insert(ind,'a')
    for j in range(int(1000*(2**(i-2)))):
        ind = random.randint(0, t.length())
        count += t.insert(ind,'a')
        ind = random.randint(0, t.length()-1)
        count += t.delete(ind)
        
    return count
        

'''for i in range(1,11):
    print("for i = : " + str(i))
    print("the count is : " + str(insert_delete(i)))
    print("\n")'''


  
    
COUNT = [4]    
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




    
