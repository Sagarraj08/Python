# import sys,datetime
# print("""Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are""")

# print('python version',sys.version)
# now=datetime.datetime.now()
# print(now.strftime('%Y-%m-%d %H:%M:%S'))
# r=complex(input())
# A=3.14*r*r
# print(format(A,'.4f'))

# A=input()
# list=A.split(",")
# tuple=tuple(list)
# print(list)
# print(tuple)

# filename=input()
# extention=filename.split(".")
# print((extention[-1]))

# color_list = ["Red","Green","White" ,"Black"]
# print( "%s  %s"%(color_list[0],color_list[-1]))

# exam_st_date = (11, 12, 2014)
# print("%i/%i/%i"%exam_st_date)

# n=int(input())
# print(n+(int("%s%s"%(n,n)))+(int("%s%s%s"%(n,n,n))))
#Doc string print(abs.__doc__)

# import calendar
# print(calendar.month(2023,8))
# from datetime import date
# dt1=date(2023,2,8)
# dt2=date(1994,2,8)
# print(dt1-dt2)
# n=int(input())
# if n>17:
#     print((n-17)*2)
# else:
#     print(17-n)
# lkist=[1,2,3,4,4,5,6,7,7,7,7]
# print(lkist.__contains__(7))

# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# for i in numbers:
#     if i==237:
#           break
#     elif i%2==0:
#          print(i,end=',')

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))