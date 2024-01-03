#parameters that will pack all arguments into a dictionary useful so that a function can accept a varying amount of keywork argumendef 

def hello(**kwargs):
    print("hello",end=" ")
    for key,value in kwargs.items():
        print(key,value,end=" ")

hello(first="itohan",middle="test",last="itohan")