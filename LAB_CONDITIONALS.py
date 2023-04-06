x = 72.65

y=5

y = int(input("rating:"))
x = float(input("popularity:"))

if  y >= 4 & x >= 80:
    print("highly recommended") 
 
elif y >= 80 & x >= 3:
    print("i recommenteded it. it is good ")
 
elif y >= 60 & y <2 :
    print("you should check out  ")
 
elif y < 50 & x <2 :
    print("don't watch it . it is a wast time")