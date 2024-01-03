# magicians=["pluto","alice","jono"]
# for magician in magicians:
#     print(f"{magician.title()} , you did a great job")
#     print(f" we are looking forward to your next trick.{magician.title()}\n")
# print("thank you all")

# pizzas=["pepperoni","bbq","range"]
# for pizza in pizzas:
#     print(f" I like {pizza.title()} pizza")
# print("I really love: " )
# print(pizzas)

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# for value in range(1,5):
#     print(value)

#convert range into a list 
# numbers =list(range(1,6))
# print(numbers)

# squares=[]
# for value in range(1,11):
#     square= value**2
#     squares.append(square)
#     print(squares)

    #list comprehension
    #assign a descriptive name to the list 
# squares=[value**2 for value in range(1,11)]
# print(squares)

    #define the expression for the values you want to store in the list
    #write the for loop

#count 1 to 20
# for count in range(1,21):
#     print(count)

#make a list of numbers from 1 to 1m
# number_list=[]
# for count in range(1,1000001):
#     number_list.append(count)
#     print(max(number_list))
    #print(number_list)
# number_list=list(range(1,1000001))
# min(number_list)
# max(number_list)
# sum(number_list)
# print(min(number_list))
# print(max(number_list))
# print(sum(number_list))

# odd_numbers=list(range(1,21,2))
# for count in odd_numbers:
#    print(count)

# multiplesofthirty=list(range(3,30,3))
# for item in multiplesofthirty:
#     print(item)

# firsttencubes=list(range(1,11))
# for item in firsttencubes:
#     cubes=item**3
#     print(cubes)
# firsttencubes= [item**3 for item in range(1,11)]
# print(firsttencubes)

#squares=[value**2 for value in range(1,11)]
#my_foods = ['pizza', 'falafel', 'carrot cake','banana']
# for items in my_foods[:3]:
#     print(f"the items are {items.title()}")

# middle_list=(len(my_foods)/2)
# print(middle_list)
# for items in middle_list:
#     print(items)

# for food in my_foods[:2]:
#     print(my_foods)

    #copying lists
# mylist=list(range(1,4))
# print(mylist)

# new_food_list=my_foods[:]
# print(new_food_list)

#tuple
# dimensions=(200,50)
# dimensions[0]=290
# print(dimensions)

# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)
    #tuples cannot be changed but over written. by defining the entire tuple with a new value

foods=("rice","beans","plantain","eggs","bread")

foods=("spaghetti","okro","plantain","eggs","bread")
for items in foods:
    print (items)