# entertainment_center.py is using to create movie instances though
# fresh_tomatoes.py

import media
import fresh_tomatoes

# movie list:
# - Despicable Me2
# - Coco
# - Forrest Gump
# - Dead Poets Society
# - WALL-E
# - Inside Out


despicable_me2 = media.Movie(
    "Despicable Me2",
    "",
    "https://upload.wikimedia.org/wikipedia/en/2/29/Despicable_Me_2_poster.jpg",
    "https://www.youtube.com/watch?v=yM9sKpQOuEw")

coco = media.Movie(
    "Coco",
    "",
    "https://upload.wikimedia.org/wikipedia/en/9/98/Coco_%282017_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=xlnPHQ3TLX8")

forrest_gump = media.Movie(
    "Forrest Gump",
    "",
    "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
    "https://www.youtube.com/watch?v=bLvqoHBptjg")

dead_poets_society = media.Movie(
    "Dead Poets Society",
    "",
    "https://upload.wikimedia.org/wikipedia/zh/4/49/Dead_poets_society.jpg",
    "https://www.youtube.com/watch?v=4lj185DaZ_o")

wall_e = media.Movie(
    "WALL-E",
    "",
    "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
    "https://www.youtube.com/watch?v=8-_9n5DtKOc")

inside_out = media.Movie(
    "Inside Out",
    "",
    "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=seMwpP0yeu4")

# create above movies' instances and assign variables
movies = [
    despicable_me2,
    coco,
    forrest_gump,
    dead_poets_society,
    wall_e,
    inside_out]

# Using fresh_tomatoes.py to generate the HTML file.
fresh_tomatoes.open_movies_page(movies)
