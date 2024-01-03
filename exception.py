
try:

    numerator =int(input("enter a number to divide: "))
    denominator =int(input("enter a number to divide by: "))
    result= numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print(e)
    print("you cant divide by zero")
except ValueError as e:
     print(e)
     print("enter only numbers please")   
except Exception as e:
    print(e)
    print("something went wrong ")

