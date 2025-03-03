# string
x = "frog"
print(x[0])

#list
x = ["pig","cow","horse"]
print(x[1])

#tuple
x=("kevin","niklas","jenny","craig")
print(x[0])

#slicing slice out substrings sublists,subtuples using indexes [start:end+1:step] 
#start include end not include and step is by default 1 if the end is leave by default we go to the end
#same with the start
x='computer'
print(x[1:5:3]) # take [1] to [5] exclude and apply a gap of 3 steps so ompu -> ou
print(x[-1]) # last elem
print(x[-3:]) # last 3 elem
print(x[-3]) # 3 en partant de la fin donc t
print(x[:-2]) # tout sauf les 2 dernier

#adding/concat using +
x = 'horse' + 'shoe' #horseshoe

# list
y = ['pig','cow'] + ['horse'] # ["pig","cow","horse"]

# tuple
z=("kevin","niklas","jenny") + ("craig",) # We need the comas "," otherwise python isn't consider it a tuple ('kevin', 'niklas', 'jenny', 'craig')

# multiply with *
x= 'bug'*3 #bugbugbug

#list
y=[8,5]*3 #[8,5,8,5,8,5]

#tuple
z=(2,4)*3 #(2,4,2,4,2,4)

#checking membership
x = 'bug'
print('u' in x) #True

y = ['pig','cow','horse'] ;print('cow' not in y) #False

z = ('Kevin' ,'Niklas','Jenny','Craig') 
print('Niklas' in z) #True

#iteration name are arbitrary
x= [7,8,3]
for item in x:
    print(item)

y =[7,8,3]
for index, item in enumerate(y):
    print(index,item)

# number of items with len
#minimum value min for words first letter first
#maximum value max for words first letter first

#sum but need to be the same type
y = [2,5,8,12]
print(sum(y)) #27
print(sum(y[-2:])) # 2 dernier donc 20

#tuple
z=(50,4,7,19)
print(sum(z)) #80

#sorting it return a new list 
x='bug'
print(sorted(x)) #['b','g','u']

#list
y=['pig','cow','horse']
print(sorted(y)) #['cow','horse','pig']

#tuple
z=("Kevin","Niklas","Jenny","Craig")
print(sorted(z)) #['Craig','Jenny','Kevin','Niklas']

# sorting by the second letter
z = ("Kevin","Niklas","Jenny","Craig")
print(sorted(z,key=lambda k:k[1])) # ['Kevin','Jenny','Niklas','Craig']


#count of item
x='hippo'
print(x.count('p')) #2

#return the index of the first occurence of an item
x='hippo'
print(x.index('p')) #2

#unpacking it's going to assign them to each variable
x = ('pig','cow','horse') #even with an list
a,b,c = x
print(a,b,c)

#-----------------------------------------------------------------#

# Lists
#General purpose
#Most widely used data structure
#Grow and shrink size as needed
#sequence type
#sortable

#constructor multiple type
x = list()
y=['a',25,'dog',8.43]
#we can create a tuple and then create a list from there
tuple1=(10,20)
z=list(tuple1)

#list comprehension

a = [m for m in range(8)]
print(a) #[0,1,2,3,4,5,6,7]
b = [i**2 for i in range(10) if i>4]
print(b) #[25,36,49,64,81]

#delete an item with del
x = [5,3,8,6]
del(x[1])
print(x) #[5,8,6]


#append append an item
x = [5,3,8,6]
x.append(7)
print(x) # [5,3,8,6,7]

#extend append a sequence to a list similar to +
x = [5,3,8,6]
y=[12,13]
x.extend(y)
print(x) # [5,3,8,6,12,13]

#insert insert an element a an given position 

x = [1,2,3]
x.insert(1,7) 
print(x) #[1,7,2,3]

#pop it's pop the last item we can pop it or print it

x = [5,3,8,6]
x.pop() #pop the 6
print(x) # [5,3,8]
print(x.pop()) #8

#remove remove first instance of an item
x=[5,3,8,6,3]
x.remove(3)
print(x) #[5,8,6,3]

#reverse reverse the order of the list . it's an in-place sort meaning it changes the original list

x = [5,3,8,6]
x.reverse()
print(x) #[6,8,3,5]

#  x.sort() returns a new sorted list without changing the original and sorted(x) gives us an new one 
x = [5,3,8,6]

#reverse sort in place meaning that we have the same object
x = [5,3,8,6]
x.sort(reverse=True)

#------------------------------------------------------------------------#

#Tuples
#Immutable (can't add /change)
#Useful for fixed data
#Faster than Lists
#Sequence type

#Constructors
x= ()
x = (1,2,3)
x=1,2,3
x=2, #the comma is mandatory
print(x,type(x)) # (2,) <class 'tuple'>

list1 = [2,4,6]
x = tuple(list1)
print(x,type(x)) # (2,4,6) <class 'tuple'>

#tuples are immutable but member of objects can be mutable
x=(1,2,3)
#del(x[1]) #fails!
#x[1]=8  same fails! but
y=([1,2],3)
del(y[0][1])
print(y) #([1],3)
#concatenating two tuple would work
y +=(4,)
print(y)#([1],3,4)

#_____________________________________________________________________________________________

#Sets
# Store non-duplicate items by hashing them
#Math Set ops (union,intersect)
#Sets are Unordered
#Constructors   

x = {3,5,3,5}
print(x) # {3,5}

y= set()
print(y) #set()

list1 = [2,3,4]
z=set(list1)
print(z) #{2,3,4}

#Operations
x = {3,8,5}
x.add(7)

x.remove(3) #remove 3

print(len(x)) # get length of set x 

print(5 in x) #check if 5 is in it

print(x.pop(),x) #pop random item from set x and gives us the item

x.clear() #delete all items from set x

# Math operation
#intersection (AND): set1&set2*
#union (OR): set1 | set1
#symmetric difference (XOR):set1^set2 difference:set1-set2
#subset(set2 contains set1):set1 <=set2
#superset(set1 contains set2): set1 >=set2
#so
s1 = {1,2,3}
s2 = {3,4,5}
print(s1 & s2) #{3}
print(s1 | s2) #{1,2,3,4,5}
print(s1 ^ s2) #{1,2,4,5} ou exclusif
print(s1 - s2) # {1,2} renvoie tout les elements de s1 qui ne sont pas dans s2
print(s1 <= s2)  #false
print(s1 >= s2) # false

#_____________________________________________________________________________________________________________
#Dictionaries Key Values Pairs

#Key/Value pairs
#Associative array
#Dicts are Unordered
#Constructors
x={'pork':25.3,'beef':33.8,'chicken':22.7}
x=dict({("pork",25.3),("beef",33.8),("chicken",22.7)})
x=dict(pork=25.3,beef=33.8,chicken=22.7)

#Operation
x['shrimp'] = 38.2 #it's create if already existant update
del(x['shrimp']) #to delete
len(x) # the size
x.clear()#delete all items from dict x
del(x)  #delete dict x
y =x={'pork':25.3,'beef':33.8,'chicken':22.7}
#accessing value

print(y.keys()) #dict_keys(['pork,'beef','chicken'])
print(y.values()) #dict_values([25.3,33.8,22.7])
print(y.items) #dict_items([('pork',25.3),('beef',33.8),('chicken',22.7)])

print('beef' in y) #check membership in y_keys (only looks in keys,not values)
print('clams' in y.values()) #check membership in values

#iterating a dict 
for key in y:
    print(key,y[key])

for k,v in y.items():
    print(k,v)

#_____________________________________________

#Python List Comprehensions
#basic format : new_list = [transform sequence [filter]]
import random
under_10= [x for x in range(10)]
print('under-10:' + str(under_10)) # 'under-10':[0,1,2,3,4,5,6,7,8,9]
squaers=[x**2 for x in range(10)]
print("squares: " + str(squaers))
odds = [x for x in under_10 if x%2 ==1]
print('odds:' + str(odds)) #[1,3,5,7,9]

s = 'I love 2 go t0 the store 7 times a w3ek'
nums = [x for x in s if x.isnumeric()]
print('nums:' + ''.join(nums)) #2073

# get index of a list item using enumerate

names= ["Cosmo",'Pedro','Anu','Ray']
idx= [k for k,v in enumerate(names) if v=='Anu']
print('index= ' + str(idx[0])) #index=2

#delete an item from a list
#We shuffle the list and filters the letter C
letters = [x for x in 'ABCDEF'] # [A,B,C,D,E,F]
random.shuffle(letters)
letrs = [a for a in letters if a !='C']
print(letters,letrs)

#____________________________________________________
#Stacks LIFO (Last In First Out)
#Push an item onto the stack
#Pop an item off of the stack
#LIFO Last In First Out
#All push and pop operation are to/from the top of the stack

#We can use python list
my_stack= list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)

my_stack.pop() #19 first
my_stack.pop() #12 then



# We can create a wrapper class stack

class Stack():
    def __init__(self):
        self.stack=list()
    def push (self,item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack)>0:
            self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else: 
            return None
    def __str__(self):
        return str(self.stack)
    
#test code 
my_stack = Stack()
my_stack.push(1)
my_stack.push(30)
print(my_stack)


#______________________________________________________________
#Queues anything that is in the line FIFO (First In First Out) 53:35

from collections import deque
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
my_queue.popleft()
print(my_queue)


class Bestdeque():
    def __init__(self):
        self.bestdeque=deque()
    def push (self,item):
        self.bestdeque.append(item)
    def pop(self):
        if len(self.bestdeque)>0:
            self.bestdeque.popleft()
        else:
            return None
    def peek(self):
        if len(self.bestdeque) > 0:
            return self.bestdeque[len(self.bestdeque)-1]
        else: 
            return None
    def __str__(self):
        return str(self.bestdeque)
        
myqueue2=Bestdeque()
myqueue2.push(5)
myqueue2.push(6)
myqueue2.push(7)
print(myqueue2)
myqueue2.pop()
print(myqueue2)

# MaxHeap complete binary tree every node <= Parent Complexity Insert in O(log n) Get Max in O(1) and remove max (log n) so pretty fast 
# it's implement using a list and the top with index 1 then left 2 right 3 child or left 4 ,5 and so on
# if for ex we want to access the numner 5 which is the index 4 we know the parent is i/2 so 4/2 so 2 and number 5 left child is i*2 so 4*2 so 8 
# and right one so i*2+1 = 9
#Operation Push (insert) Peek (get max) Pop (Remove max)
#[Push] Add value to end of array float it up to it's proper position to do that we ask if he is greater than his parent if it's the case we swap them
#Otherwise he stay there
#[Peek] return the value at heap[0] so the max
#[Pop] move max to end of array , delete it , Buddle Down the item at index 1 to it's proper position & return max
#So we swap position between our max and the last element , delete it and then bubble down to get this to his correct position 
#so in case we have 11 with left 16 and right 24 we promote 24 and then 11 is the parent we see if his children are greater or not
#So we have public and private function so the user can't see them public (push,peek,pop) and private (swap,__floatUp__,__bubbleDown____str)

class MaxHeap:
    def __init__(self,items=[]):
        super().__init__()
        self.heap=[0] # we start at index n1
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap)-1) #len(self.heap)-1 renvoie bien le premier element puis le deuxieme puis le 3e ect
    
    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)
    
    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False
        
    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1,len(self.heap)-1)
            print(self.heap)
            max=self.heap.pop()
            print(self.heap)
            self.__bubbleDown(1)
            print(self.heap)
        elif len(self.heap)==2:
            max=self.heap.pop()
            print(self.heap)
        else:
            max= False
        return max
    
    def __swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    

    def __floatUp(self,index):
        parent = index//2
        if index <=1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index,parent)
            self.__floatUp(parent)

    def __bubbleDown(self,index):
        left = index * 2
        right = index*2+1
        largest = index
        if len(self.heap) > left and self.heap[largest] < self.heap[left]:
            largest=left
        if largest != index:
            self.__swap(index,largest)
            self.__bubbleDown(largest)
    
    def __str__(self):
        return str(self.heap)
    


m = MaxHeap([1,2,3,4])
m.push(10)
print(m)
print(m.pop())
print(m.peek())

#_____________________________________________________________
#Linked List
#Attributes Root pointer to the beggining of the list , Size number of nodes in List
#Operations find(data) add(data) remove(data) print_list()
#[Add]We start by creating the data then our node.next is going to point to the current root data and then we attribute the root to our data
#[Remove] we start a the root we see if the data is our data to remove if not we continue our walk when we find it to delete it 
#We take the previous node and made it point the next node


#Node Class

class Node:
    def __init__(self,d,n=None,p=None):
        self.data=d
        self.next_node=n
        self.prev_node=p
    
    def __str__(self):
        return ('('+ str(self.data)+')')
    

#LinkedList Class

class LinkedList:
    
    def __init__(self,r=None):
        self.root =r 
        self.size = 0

    def add(self,d):
        new_node=Node(d,n=self.root)
        self.root = new_node
        self.size +=1
    
    def find(self,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data==d:
                return d
            else:
                this_node=this_node.next_node
        return None

    def remove(self,d):
        this_node =self.root
        prev_node = None
        while this_node is not None:
            if this_node.data == d: 
                if prev_node is not None: #data is in non-root
                    prev_node.next_node = this_node.next_node    
                else: # data is in root node 
                    self.root=this_node.next_node
                self.size -=1
                return True #data removed
            else:
                prev_node=this_node
                this_node=this_node.next_node
        return False #data not found
    
    def print_list(self):
        this_node = self.root
        while this_node is not None:
            print(this_node,end='->')
            this_node = this_node.next_node

        print('None')

#Test Code 


myList=LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
myList.print_list()
print("size= "+str(myList.size))
myList.remove(8)
print("size = "+str(myList.size))
print(myList.find(5))
print(myList.root)


#Circular Linked List
#Advantage is for modeling continuous looping objects like a monopoly board or race tracking.
#Same as regular linkedList but to add an object we insert it a  the second node bcs our last node point back to the first node

class CircularLinkedList:
    def __init__(self, r=None):
        self.root=r
        self.size=0
    
    def add(self,d):
        if self.size == 0:
            self.root= Node(d)
            self.root.next_node=self.root
        else:
            new_node = Node(d,self.root.next_node)
            self.root.next_node=new_node
        self.size +=1

    def find(self,d):
        this_node = self.root
        while True:
            if this_node.data ==d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node= this_node.next_node
    
    def remove(self,d): #We track the 2 nodes
        this_node = self.root
        prev_node = None

        while True:
            if this_node.data==d: #found
                if prev_node is not None:
                    prev_node.next_node=this_node.next_node
                else:
                    while this_node.next_node !=self.root:
                        this_node = this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node
                self.size -=1
                return True
            elif this_node.next_node == self.root:
                return False
            prev_node= this_node
            this_node = this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node != self.root:
            this_node=this_node.next_node
            print(this_node, end="->")
        print() 

cll = CircularLinkedList()
for i in [8,7,3,8,9]:
    cll.add(i)

print("size="+str(cll.size))
print(cll.find(8))
print(cll.find(12))

my_node = cll.root
cll.print_list()

#Doubly Linked List point to the precedent and next Item

class DoublyLinkedList:
    def __init__(self,r= None):
        self.root =r 
        self.last =r 
        self.size = 0

    def add (self,d):
        if self.size == 0:
            self.root = Node(d)
            self.last = self.root
        else:
            new_node = Node(d,self.root)
            self.root.prev_node = new_node
            self.root = new_node
        self.size +=1

    def find (self,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                return d 
            elif this_node.next_node == None:
                return False
            else:
                this_node = this_node.next_node

    def remove(self,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                if this_node.prev_node is not None:
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node = this_node.next_node
                        this_node.next_node.prev_node = this_node.prev_node
                    else:
                        this_node.prev_node.next_node=None
                        self.last = this_node.prev_node
                else:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -=1
                return True
            else:
                this_node = this_node.next_node
        return False
    
    def print_list(self):
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end="->")
        while this_node.next_node is not None:
            this_node=this_node.next_node
            print(this_node, end="->")
        print() 

print("#####################")
# Test Code

dll = DoublyLinkedList()

for i in  [5,9,3,8,9]:
    dll.add(i)

print("size="+str(dll.size))
dll.print_list()
dll.remove(8)
print("size="+str(dll.size))
print(dll.remove(15))
print(dll.remove(5)) # Sa execute bien la fonction meme dans un print
dll.print_list()

#Binary Tree with this data struct we can find in max 30 guess a number between 1 and 10 million
#A tree is compose of node that are connect with a edge a the top we have a root also have (parent node and children node in a binary tree , the parent
#can have up to 2 child , the child from the same parent are called siblings and the node at the really bottom are call leaf)
# Ancestor are each node that are above the parent node descendant are the other way arround
#In binary Search Tree each node is greater than every node in its let subtree (Donc tu connais a droite plus grand gauche plus petit)
#Bst Insert we always insert as a leaf
# we compare the root if greather -> right otherwise left ect...
# Find we start at the root
#Same we compare if greather or lower than the root then look up for the left or right side
#Delete 3 different cases : leaf node , 1 child , 2 children
#Leaf node easy we just delete them
#1 child we promote the child node to the target node position
#2 children find the next higher node so take the right side and go all the way to the left and swap them and we can remove the node
#Get Size is recursive like almost all the other size =1 + size(left subtree)+size(right subtree)
#Preorder Traversal
#Visit root before visiting the root's subtrees 1->root 2->root of left subtree 3->left of root of left subtree ect when left side clear we go to right
#side and do the same with the left side then right side
#Inorder Traversal
#Visit root between visiting the root's subtrees gives values in sorted order so 1 -> Total left 2->his parent 3->right side 4-> the ancestor ect
#Advantages of binary search Trees?
# Because trees use recursion for most operations they are fairly easy to implemenet but the speed us really good
#Insert , Delete , Find in 
#O(h) = O(log n) where h is the height of the tree 

class Tree:
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right
    def insert(self, data):
        if self.data == data:
            return False  # Évite les doublons
        elif data < self.data:
            if self.left is not None:
                return self.left.insert(data)
            else:
                self.left = Tree(data)
                return True
        else:
            if self.right is not None:
                return self.right.insert(data)
            else:
                self.right = Tree(data)
                return True
    def find (self,data):
        if self.data == data:
            return data 
        elif self.data > data:
            if self.left is None:
                return False
            else:
                return self.left.find(data)
        elif self.data < data:
            if self.right is None:
                return False
            else:
                return self.right.find(data)
    def get_size(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.get_size() + self.right.get_size()
        elif self.left:
            return 1 + self.left.get_size()
        elif self.right:
            return 1 + self.right.get_size()
        else:
            return 1
    
    def preorder(self):
        if self is not None:
            print(self.data, end=" ")
            if self.left is not None:
                self.left.preorder()
            if self.right:
                self.right.preorder()
    
    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data, end=" ")  # Impression de la valeur actuelle
        if self.right is not None:
            self.right.inorder()


print("############################")
tree = Tree(7)
tree.insert(9)
print(tree.preorder())
for i in [15,10,2,12,3,1,13,6,11,4,14,9]:
    tree.insert(i)
    
for i in range(16):
    print(tree.find(i),end=" ")
print ("\n", tree.get_size())

print(tree.preorder())
print(tree.inorder())
# Vertex (sommet) A-B-C etc and (A->B) le segment est un edge
#Undirected Graph bidirectional both way arround (Social network connection)
#Directed Graph 1 way use for modeling flight in airplane for ex (where it's may go to one city but not the other)
#We can represent them with Adjancency List which gives all the connection for ex : A: B,C,E -> B:A,C ect... or an Adjacency Matrix
# Which have from and to so 
#  A B C D
#A 0 1 1 0
#B 1 0 1 0
#C 1 1 0 1
#D 0 1 0 0
# So if there is a 1 that means that it's connect otherwise it's not
#If we have to implement weight it's much better to use a matrix bcs u can put directly the weight instead of 1 where in the list you have a implement
#a tuple
# Same with with Directed graph the only diff is that the matrix isn't symetric
#There is 2 type of Graph (Dense Graph) -> graph where |E| = |V|² le nombre de edge = nb de vertex au carré (Un grand nombre)
#Sparse Graph where |E| = |V| donc pas enormement de connexion
#Which one better?
# Adjacency List
#Pro : Faster and uses less space for Sparse graphs
#Con ; Slower for Dense graphs

#Adjacency Matrix
#Pro: Faster for dense graphs
#Pro:Simpler for Weighted edges
#Con:Uses more space

#Vertex Class
class Vertex:
    def __init__(self,n):
        self.name= n
        self.neighbors=set()

    def add_neighbor(self,v):
        self.neighbors.add(v)


class Graph:
    vertices = {}

    def add_vertex(self,vertex):
        if isinstance(vertex,Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
        
    def add_edge(self,u,v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False
        
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key,sorted(list(self.vertices[key].neighbors)))

#Test Code 3 way to add vertex to our graph (Sommet)
g = Graph()
a=Vertex("A")
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord("A"),ord('K')): #ord gives us the numerical equivalent to permit to loop throught
    g.add_vertex(Vertex(chr(i)))
g.print_graph()
print("###############")
edges=["AB","AE","BF","CG","DE","DH","EH","FG","FI","FJ","GJ",'IH']
for edge in edges:
    g.add_edge(edge[0],edge[1])
g.print_graph()

#See the course for the matrix implement one
#
#
#
##
##
##
##
##
#
##
#