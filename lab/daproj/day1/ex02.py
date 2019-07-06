from numpy.random import randn
import numpy as np
data = {i:randn() for i in range(7)}
data = {i:np.random.randn() for i in range(7)}
print(data)

x = 10
y = 20

print(x, y)
print(x)
print(y)

an_apple = 27
an_example = 4

print(x // y)
print(x % y)
print(x ** y)

b = {1,2,3}

print(b)

import numpy as np
my_1 = np.arange(10000)
my_2 = list(range(10000))
print(my_1)
print(my_2)

for _ in range(10): my_3 = my_1 *2

##########################################################

x = 5
y = 7

if x <1:
    x +=1

    print(x)

    y =8

print(x, y)



a = [1,2,3]

b =a

a.append(4)
a.append(5)
print(a)

print(b)


def append_element(some_list, element):
    some_list.append(element)

data = [1,2,3]

append_element(data , 4)

print(data)



a = 'fpp'




print(a)

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(isiterable(1))
print(isiterable(a))


import some_module
re = some_module.f(5)
pi = some_module.PI

print(re)
print(pi)
