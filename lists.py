#list is used to store multiple items within a single variable

# food = ["pizza","hamburgers","spaghetti","hotdog"]

# # food[0] ="sushi"
# #print(food[-1].title())

# #loop list
# #food.append("ice cream")
# # food.sort()
# # for x in food:
# #     print(x)

# # # list and x is the item
# # print(food)
# message=f"my first food was {food[0].title()}"
# print(message)

#exercise
guest=["ebube","ogo","kelani","ify","adeola"]
print(guest,"\nyou are all invited to  my dinner")

# guest[0]="marvelous"
# print(f"\n{guest}nyou are all invited to  my dinner" )

guest.insert(0,'zena')
print(guest)

# guest.insert(2,'james')
# print(guest)

# guest.append("asher")
# print(guest)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)

# cars.reverse()
# print(cars)

# del guest[-1]
# print(guest)

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)

# popped_motorcycle=motorcycles.pop()
# print(popped_motorcycle)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)

# cars.reverse()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# print(len(cars))
#age  = int (input("how old are you ?:"))
#N = int(input(""))
if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(my_list)
        elif command[0] == "remove":
            my_list.remove(int(command[1]))
        elif command[0] == "append":
            my_list.append(int(command[1]))
        elif command[0] == "sort":
            my_list.sort()
        elif command[0] == "pop":
            my_list.pop()
        elif command[0] == "reverse":
            my_list.reverse()
