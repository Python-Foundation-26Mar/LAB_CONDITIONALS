# LAB_CONDITIONALS
# You want to recommend a movie to a friend based on the rating and popularity . To accomplish this do the following : 

movie = "Born a King"  # Create a variable for the movie (choose any movie you like)
rating_the_movie:int = 3  # - Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
popularity_score:float= 72.65   # - Create a popularity score of type float , let it be 72.65


# - Using an if statement 
if rating_the_movie >= 4 and popularity_score > 80:
    print("Highly recommended")
elif rating_the_movie >= 3 and popularity_score > 70:
    print("I recommended it . It is good")   
elif rating_the_movie <= 2 and popularity_score > 60:
    print("You should check it out!")
elif rating_the_movie <= 2 and popularity_score < 50:
    print("Don't watch it. It is a waste of time")  