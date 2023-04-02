print("")
move_name="The Matrix"
move_rating : int =3
move_populartiy : float=72.65

print(f"movie name: {move_name}")
print(f"movie rating: {move_rating} /5")
print(f"movie populartiy: {move_populartiy} /100")

if move_rating >= 4 and move_populartiy > 80:
    print("Highly recommended")
elif move_rating >= 3 and move_populartiy > 70:
    print("I recommended it . It is good")
elif move_rating <=2 and move_populartiy > 60:
    print("You should check it out!")
elif move_rating <=2 and move_populartiy <50:
    print("Don't watch it. It is a waste of time") 
print("")
