
########################################################
#  익명함수 lambda
#  함수는 객체 자바스크립트와 동일
########################################################

## lambda ():

#print_mag = test
#print(type(print_mag))
#print_mag('hello')


def outer():
    def test(x):
        print('hello', x)
    #test('abc')
    return test

print(outer());

result = outer()
print(type(result))
result("홍길동");



def add(x,y):
    return  x+y
def sub(x,y):
    return x -y



############################
# 기존
############################
def calculator(x,y,op):
    return op(x,y)

############################
# 람다 변경
############################
calculator = lambda x,y,op :  op(x,y)

############################






def make_list(some_list, filter):
    result = []
    for x in some_list:
        if filter(x):
            result.append(x)
    return result

def is_long_than_3(string):
    return len(string) > 3
original_list = ['python', 'big', 'data', 'hb']
new_list = make_list(original_list,is_long_than_3)
print(new_list)


new_list = make_list(original_list, lambda x: len(x) < 3)




result = calculator(1,2,add)
print(result);

result = calculator(1,2,sub)
print(result);


result =calculator(10,20, lambda x,y:x*y)
print(result)



























import pygame
import pygame as pg

#pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the height and width of the screen
#size = [1000, 1000]
#screen = pygame.display.set_mode(size)

#pygame.display.set_caption("Game Title")

# Loop until the user clicks the close button.
#done = False
#clock = pygame.time.Clock()

#while not done:

    #clock.tick(10)

    # Main Event Loop
   # for event in pygame.event.get():  # User did something
    #    if event.type == pygame.QUIT:  # If user clicked close
     #       done = True  # Flag that we are done so we exit this loop


    #screen.fill(WHITE)


   # pygame.display.flip()

