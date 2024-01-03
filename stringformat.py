import this

#str.format()=optional method that gives uses more control when displaying output

# animal="cow"
# item="moon"

#print("the {} jumped over the {}".format("cow","moon"))#the curly braces are place holders for the variables
#print("the {} jumped over the {}".format(animal,item))#the curly braces are place holders for the variables
# print("the {0} jumped over the {1}".format(animal,item))#positional arguments
# print("the {} jumped over the {}".format(animal="cow",item="moon"))#keyword argument
#print("my name is {:>10}.nice to meet you".format(animal))#padding 
#print("my name is {:^10}.nice to meet you".format(animal))#centre align

# first_name="itohan"
# last_name="eregie"
# full_name=f"{first_name} {last_name}"
# message=f"Hello,{full_name.title()}!" #.title() formats the  sentnce to title case
# #print(message,"\nsee \nyou\nlater")#print on new line
# print(message,"\n\tsee \n\tyou\n\tlater")#print on new line and tab

website="https://www.google.com"
noprefix=website.removeprefix("https://")
print(noprefix)

