# def arithmetic(a,b):
#     if c==1:
#         return a+b
#     elif c==2:
#         return a-b
#     elif c==3:
#         return a*b
#     elif c==4:
#         return a//b
#     else:
#         return "Incorrect Choice"
# a=int(input("Enter the First value: "))
# b=int(input("Enter the Second Value: "))
# c=int(input("Enter your Choice (1.Addition 2.Subraction 3.Multiplication 4.Division): "))
# print(arithmetic(a,b))
   
# for i in range(1,25):
#     print(i)pk

# def reverse(n):
#     for i in n:
#         return i
# n="row"
# print(reverse(n))


#strong number

# def str_num(num):.
#     num1=num
#     sum=0
#     while num>0:
#         x=num%10
#         fact=1
#         while x>=1:
#             fact=fact*x
#             x-=1
#         sum+=fact
#         num=num//10
#     print("sum of",num1,"=",sum)
#     if (sum==num1):
#         return "it is a strong number"
#     else:
#         return "it is not a strong number" 
# print(str_num(145))


#palindrom number
# def palin(num):
#     num1=num
#     rev=0
#     while num>0:
#         x=num%10
#         rev=rev*10+x
#         num=num//10
#     print(rev)   
#     if (rev==num1):
#         return "it is a palindrom number"
#     else:
#         return "It is a not palindrom number" 
# print(palin(1321))


#Amstrong number
# def Armstrong(num):
#     num1=num
#     sum=0
#     count=len(str(num))
#     while num>=1:
#         x=num%10
#         sum+=x**count
#         num=num//10
#     print(sum)
#     if(sum==num1):
#         return "It is a Amstrong number"
#     else:
#         return "It is not a Amstrong"  
# print(Armstrong(1634))


def arm_str(num):
    num1=num
    y=num
    sum=0
    count=0
    while num>=1:
        num=num//10
        count+=1
    print(count)    
    while num1>=1:
        x=num1%10
        sum+=x**count
        num1=num1//10
    print(sum)   
    if(sum==y):
        return "It is a Amstrong number" 
    else:
        return "It is not a Amstrong"
print(arm_str(1634))