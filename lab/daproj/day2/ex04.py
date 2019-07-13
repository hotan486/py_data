########################################################
#  클래스 연습
#
########################################################

class Array:
    def __init__(self,x=0,y=0,z=0):
        self.array = []
        self.array.append(x)
        self.array.append(y)
        self.array.append(z)
    def __str__(self):
        return '({0},{1},{2})'.format(self.array[0],self.array[1],self.array[2])

    def plus(self,other):
        if isinstance(other, Array):
            for i in range(len(self.array)):
                self.array[i] = self.array[i] + other.array[i]

        else:
            raise TypeError()



arr1 = Array()
print(type(arr1))
print(arr1)

arr2 = Array(1,2,3)
print(type(arr2))
print(arr2)

a=1
arr1.plus(arr2)
print(arr1)
print(arr2)
