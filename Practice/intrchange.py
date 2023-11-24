# # Python program to interchange first and last elements in a list

# def reverse(new):
#     size=len(new)
#     temp=new[0]
#     new[0]=new[size-1]
#     new[size-1]=temp
#     return new

# new=[1,2,3,4,5,6]
# # print(reverse(new))

# def reverse2(new):
#     start,*middle,end=new
#     new=[end,*middle,start]
#     return new
# print(reverse2(new))

# def sqr(n):
#     sum=0
#     for i in range(1,n+1):
#         sum=sum+(i*i)
#     return sum

# print(sqr(4))

# # array
# arr=[1,2,3,4]
# def sum(arr):
#     sum=0
#     for i in arr:
#         sum=sum+i
#     return sum
# print("sum of an array is",sum(arr))

# swapposition
# def swap(list,pos1,pos2):
#     list[pos1],list[pos2]=list[pos2],list[pos1]
#     return list
# list=[1,2,3,4,5,6,7,8,9]
# pos1=1
# pos2=4
# print(swap(list,pos1,pos2))

#length of list
lst=[1,2,3,4,5,6,7]
# print(len(lst))

# sum=0
# for i in lst:
#     sum=sum+1
# print(sum)

# print(str(sum(1 for i in lst)))

#list length using recursion 
# def recursion(lst):
#     if not lst:
#         return 0
#     return 1 + recursion(lst[1:])
# print(recursion(lst))


number1 = input("First number: ")
number2 = input("\nSecond number: ")
 
# Adding two numbers
# User might also enter float numbers
sum = float(number1) + float(number2)
 
# Display the sum
# will print value in float
print("The sum of {0} and {1} is {2}" .format(number1,number2, sum))