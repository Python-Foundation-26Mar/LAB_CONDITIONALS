
## - Create a variable for the movie (choose any movie you like)
movie = "Breking Bad"

## - Create a variable of type int to hold the rating of the movie out of 5 . Give this movie 3
rating_the_movie = 3

## - Create a popularity score of type float , let it be 72.65
popularity_score = 72.65

## - - Check if the movie rating is 4 or greater and the popularity is greater than 80 , print "Highly recommended"
if rating_the_movie >= 4 and popularity_score > 80:
     print("Highly recommended")

## - - else if the movie rating is 3 or greater and the popularity is greater than 70 , print "I recommended it . It is good"
if rating_the_movie >= 3 and popularity_score > 70:
     print("I recommended it . It is good")

## - - else if the movie rating is 2 or less and the popularity is greater than 60 , print "You should check it out!"
if rating_the_movie <= 2 and popularity_score > 60:
     print("You should check it out!")

## -  - else  the movie rating is 2 or less and the popularity is less than 50 , print "Don't watch it. It is a waste of time"
if rating_the_movie <= 2 and popularity_score > 50:
     print("Don't watch it. It is a waste of time")

