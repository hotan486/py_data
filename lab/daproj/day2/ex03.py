########################################################
#  클래스
#
########################################################

numbers = [1,2,3]

print(type(numbers))
print(numbers)
numbers.append(4)
print(numbers)

numbers.insert(1,100)
numbers.insert(2,101)
print(numbers)

numbers.pop(3)
print(numbers)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point: [x={0}, y={1}]'.format(self.x,self.y)

    def moveX(self, deltaX):
        self.x = self.x + deltaX

    def moveY(self, deltaY):
        self.y = self.y + deltaY

    def display(self):
        print('Point(',self.x,',',self.y,')')


pt1 = Point(1,1)
pt1.display()
pt1.moveY(1)
pt1.display()

pt1 =  Point(1,1)
print(type(pt1))
print(pt1)
