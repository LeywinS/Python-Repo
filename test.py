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
