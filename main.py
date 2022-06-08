from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_archive_webpage = response.text
soup = BeautifulSoup(web_archive_webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movies_list = [movie.getText() for movie in movies]
movies_list = movies_list[::-1]

with open("movies.txt", "a") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
