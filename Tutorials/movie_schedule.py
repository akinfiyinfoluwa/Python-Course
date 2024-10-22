
current_movies = {
    "The Shawshank Redemption": '5: 00pm',
    "The Godfather": '6: 00pm',
    "The Dark Knight": '7: 0pm',
    "12 Angry Men": '8: 00pm',
}

print("we are currently showing the following movies:")
for key in current_movies:
  print(key)

movie = input('What movie would you like for the showtime for\n')

showtime = current_movies.get(movie)

if showtime == None:
     print("Requested Movie isn't available")
else:
    print(movie, 'is playing at', showtime)
