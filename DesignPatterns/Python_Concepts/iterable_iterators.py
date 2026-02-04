"""
# What is iteration ?
 ANS Iteration is a process of traverrsing one by one on an object. For ex traversing through a list containing numbers or strings

# What is iterator?
ANS: Iterator is an object which gives us the capability to perform iteration on an iterable without having to store the entire data in the memory. In technical an object which contains __iter__() and __next__() method definition are known as iterator. 


# What is iterable ?
 ANS: Iterable is an object, which one can iterate over, or in technical we can say that such object which contains the __iter__() method is known as iterable. It generates an Iterator when passed to iter() method.

 
# Point to remember
    Every Iterator is also and Iterable
    Not all Iterables are Iterators

# How to find whether an object is Iterable or Iterator?
ANS: Every Iterable has an {iter} function
     Every Iterator has both {iter} function as well as a {next} function    

# In Python withot having any increment operator how does For-Loop iterates over a set of values? 
ANS: This behaviour is possible only because of the iterator. What for-loop internally does is it takes the iterable over which it have to traverse, creates an iterator from the iterable obj by calling the iter() method, uses the while loop and then prints the stuff using the next method     
"""

# Writting custom for loop

def custom_for_loop(iterable):
    iterator = iter(iterable) #creating an iterator

    while True:
        try:
            print(next(iterator))# each iterator contains the next() which always points to the next item in the terable, and throws StopIteration exception when all items finishes.
        except StopIteration as e:
            break

a = [1,2,3,4,5]
b= (1,2,3)
c= {1,2,3}
d='strings'
e={1,2,3}
x = range(1,10)
custom_for_loop(a) # can pass all the above iterable. Right now it will print 1 2 3 4 5

"""
# We know that when we pass iterable to iter() it returns the iterator but what if we pass an iterator to iter(), So in that case it will return the same Iterator. 
You can verify it by calling id() function on iterator

a = [1,2,3,4,5]
it1 = iter(a)
it2 = iter(it1)
print(id(it1)) #132197057190816 (memory location)
print(id(it2)) #132197057190816
"""