# number=int(input("Enter a number:"))

# result=0
# temp=number

# while temp!=0:
#     digit=temp%10
#     result=result+digit**3
#     temp=temp//10
# print(result)

# if number==result:
#     print("The number is an Armstrong number.")
# else:
#     print("The number is not an Armstrong number.")





def pf(n):
    print("The factors are:")
    for i in range(1,n+1):
        if n%i == 0:
            print(i)
num=int(input("Enter a number:"))
pf(num)