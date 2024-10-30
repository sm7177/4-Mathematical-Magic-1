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





# def pf(n):
#     print("The factors are:")
#     for i in range(1,n+1):
#         if n%i == 0:
#             print(i)
# num=int(input("Enter a number:"))
# pf(num)







def romantoint(n):
    roman={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    int_form=0
    for i in range(len(n)):
        if i+1<len(n) and roman[n[i]]<roman[n[i+1]]:
            int_form-=roman[n[i]]
        else:
            int_form+=roman[n[i]]
    return int_form
n=input("Enter a roman number:")
print("Integer form of",n,"is",romantoint(n))
    