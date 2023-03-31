Mymovie="Interstellar"
print ("Welcome to the movice rating page ", Mymovie)
print("-"*60)
RateMovice=int(input("Please enter your rating for the movie out of 5    "))
print("your rate is ",RateMovice)
CommonScore:float=72.65
print("CommonScore is ",CommonScore)

if RateMovice >=4 and CommonScore > 80:
      print("Highly Recommended")
elif RateMovice>=3 and CommonScore>70:
    print("I recommended it. It's good") 
elif RateMovice<=2 and CommonScore>60:
     print("You must check it out!")
elif RateMovice<=2 and CommonScore<50:
    print("Don't watch it. It's a waste of time. ")
else:
     ("Don't watch it. It's a waste of time.")