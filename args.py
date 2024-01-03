#*args = parameter that will pack all arguments into a tuple . this is useful so that a functionc can accept varying amount of arguments

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

#print(add(1,2,3,3))
# result=add(1,2,2,4,5)
# print(result)