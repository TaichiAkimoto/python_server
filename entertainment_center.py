import media
import fresh_tomatoes

# Toy Story: movie title, storyline, poster image and movie trailer
toy_story = media.Movie(
    "Toy Story",
    "A story of a boy and his toys that come to life",
    "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

# Avatar: movie title, storyline, poster image and movie trailer
avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
    )

# Imitation game: movie title, storyline, poster image and movie trailer
imitation_game = media.Movie(
    "Imitation_Game",
    "A story of a mathmatical genius who broke german military message encryption",
    "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM"
    )

# Beauty and the beast: movie title, storyline, poster image and movie trailer
beauty_and_the_beast = media.Movie(
    "Beauty and the beast",
    "A story of a beautiful girl and a handsome princes who was turned into a beast",
    "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",
    "https://www.youtube.com/watch?v=S5CjKEFb-sM"
    )

# Your name: movie title, storyline, poster image and movie trailer
your_name = media.Movie(
    "Your name",
    "A story of a boy and a girl who was supposed to be dead",
    "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",
    "https://www.youtube.com/watch?v=AbeZsdlkAVc"
    )

# The great gatsby: movie title, storyline, poster image and movie trailer
great_gatsby = media.Movie(
    "Great Gatsby",
    "A sad story",
    "https://upload.wikimedia.org/wikipedia/en/c/c2/TheGreatGatsby2013Poster.jpg",
    "https://www.youtube.com/watch?v=rARN6agiW7o")

# Set the movies that will be passed to the movie file
movies=[
    toy_story,
    avatar,
    imitation_game,
    beauty_and_the_beast,
    your_name, great_gatsby
    ]

# Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
