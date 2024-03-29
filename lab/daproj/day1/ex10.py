

###################################
# 두개 반환하는 함수
###################################
def sub(x,y):
    return x-y,x+y
x,y = sub(10,9)
print(x,y);


###################################
# 인자 디폴트 가능 함수
###################################
def sub(x,y=0):
    return x-y

print(sub(10));


###################################
# 가변 길이 인수
###################################
def subs(*args):
    print("가변=",len(args))
    sum = 0
    for arg in args:
        sum += arg
    return sum


print(subs(10,34,345,345,345,34,53,45,34,5))


###################################
# 가변 길이 인수
###################################
def subs(op,*args):
    if op == "+":
        total = 0
        for arg in args:
            total += arg
        return total
    elif op == "*":
        total = 1
        for arg in args:
            total *= arg
        return total
    else:
        print("못합니다");


print(subs("*",10,34,345,345,345,34,53,45,34,5))