# add two number
# a=int(input())
# b=int(input())
# print(max(a,b))
#factorial

# def fact(n):
#     return 1 if (n==1 or n==0) else n*fact(n-1)
# print(fact(5))

#simple interest
# t=int(input())
# p=int(input())
# i=int(input())
# cinterest=p*((1+i/100)**t)
# print(cinterest)

# prime number
# def prime(x,y):
#     primelist=[]
#     for i in range(x,y):
#         if i==0 or i==1:
#             continue
#         else:
#             for j in range(2,int(i/2)+1):
#                 if i%j==0:
#                     break
#                 else:
#                     primelist.append(i)
#     return primelist
# starting=2
# ending=70
# lst=prime(starting,ending)
# if len(lst)==0:
#     print("no prime numbers")
# else:
#     print("prime numbers are",lst)

# n=5
# if n>1:
#     for i in range(2,int(n/2)+1):
#         if (n%i)==0:
#             print("is not prime number")
#             break
#         else:
#             print("n is prime number")
# else:
#     print("is not prime number")

# ascii
# n='g'
# print(ord(n))
# fibonnacci series
# def fibonacci(n):
#     if n<=0:
#         print("incorrect input")
#     elif n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

#square of natural numbers

def square(n):
    sm=0
    for i in range(1,n+1):
        sm=sm+(i*i)
    return sm
print(square(4))





    
