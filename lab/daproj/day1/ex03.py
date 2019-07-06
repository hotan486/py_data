list1 = [1,2,3,4,5]

print(list1)
print(list1[1])
print(list1[0:2])


c = ""

c.count('\n')
print(c.count('\n'))

a = 'this is a string'

# 변경은 안되고 다른 객체에 추가는 가능
b = a.replace('string', 'longer string')

print(b)


a= 5.6
s = str(a)
print(s)

s = 'python'

print(list(s))

s = r'this\has\no\special\char'

print(s);

list2 = [[1,2,3],[4,5,6]]

print(list2[0][2])

template = '{0:.2f}{1:s} are worth US${2:d}'
template1 =  template.format(4.5560,' Argentine Pesos', 1)
print(template1)


val = "espanol"
print(val)
val_uft8 = val.encode('utf-8')
print(val_uft8)
print(type(val_uft8))














