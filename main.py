import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

best_movies_web_page = requests.get(URL).text

soup = BeautifulSoup(best_movies_web_page, "html.parser")

get_movies = soup.find_all(name="h3", class_="title")

movies = [movie.getText() for movie in get_movies]
movies.reverse()
movies[58] = "59) E.T. - The Extra Terrestrial"

with open("top_100_movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
