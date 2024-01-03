#loop control is used to change the execution of loops execution from its normal sequence 
#break=to terminate the loop
#continue=skips to the next iteration of the loop
#pass=does nothing 

# while True:
#     name=input("what is your name:")
#     if name !="":
#         break

# phone_number="000-000"

# for i in phone_number:
#     if i =="-":
#         continue
#     print(i,end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i,end="")