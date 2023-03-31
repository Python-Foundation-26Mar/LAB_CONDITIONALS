#Movie Recommendation For A Friend
myMovie = "Interstellar"
print (f"The movie name is: {myMovie}")

movieRate : int = 3 
print (f"The Movie Rating is: {movieRate} out of 5 ")

moviePop : float = 72.65
print (f"The Movie Popularity Score is: {moviePop} ")

if movieRate >= 4 and moviePop > 80:
    print ("Highly recommended")
    
elif movieRate >=3 and moviePop > 70:
    print("I recommend it. It is good") 
           
elif movieRate <=2 and moviePop > 60:
    print ("You should check it out!")
    
else:
    print("Don't watch it. It is a waste of time")        