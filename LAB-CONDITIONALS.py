movie="Beauty and the beast"
movie_rating :int=3
popularity:float=72.60

if movie_rating >=4 and popularity>80:
 print("Highly recommended")
elif movie_rating >=3 and popularity>70:
 print("I recommended it . It is good")
elif movie_rating <=2 and popularity>60:
 print("I recommended it . It is good ")
else:     # elif movie_rating<=2 and popularity<50: print("Don't watch it. It is a waste of time")?
 print("Don't watch it. It is a waste of time")
