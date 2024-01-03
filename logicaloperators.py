#and,or,not

temp=int(input("what is the temperature outside?:"))

# if temp >= 0 and temp <= 30:
#     print("the temp is good today")
#     print("go outside")
# elif  temp < 0 or temp > 30:
#     print("the temp is bad today")
#     print("stay inside")

if not(temp >= 0 and temp <= 30):
    print("the temp is bad today")
    print("dont go outside")
elif not(temp < 0 or temp > 30):
    print("the temp is good today")
    print("go outside")