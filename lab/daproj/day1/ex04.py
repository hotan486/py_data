t1 = (1,2,3,4,5)

print(t1)

a,b,c,d,e = t1
print(a)
print(b)
print(c)
print(d)
print(e)

print(type(t1))


import pandas as pd


obj = pd.Series([4,7,-5,3])
print("===========================================")
print(obj)
print("===========================================")
print(obj.values)
print("===========================================")
print(obj.index)
print("===========================================")
obj2 = pd.Series( [4,7,-5,3] , index=['d','b','a','c'])
print(obj2)

print("===========================================")
print(obj2.index)
print("===========================================")
print(obj2['a'])
print("===========================================")
obj2['d'] = 6
print(obj2['d'])
print(obj2[['c','a','d']])
print(obj2[obj2 > 0])

print("===========================================")
print("===========================================")


sdata  = {
    'Ohio':35000,
    'Texas':71000,
    'Oregon':16000,
    'Utah':5000
}

obj3 = pd.Series(sdata)

print(obj3)

print("===========================================")
print("===========================================")

state = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=state)
print(obj4)
print(pd.notnull(obj4))
print(pd.isnull(obj4))

print(obj4.isnull())

print(obj3 + obj4)


print("===========================================")
print("===========================================")
print("===========================================")
obj4.name = 'population'

obj4.index.name = 'state'
print(obj4.name)
print("===========================================")
print(obj4)










