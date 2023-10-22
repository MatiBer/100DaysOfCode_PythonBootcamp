from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text
soup = BeautifulSoup(empire_web_page, 'html.parser')

# film_titles = []
# for film_tag in soup.find_all()
all_titles = soup.find_all(name="h3", class_="title")

movie_titles = [title.getText() for title in all_titles]

movie_titles.reverse()
print(movie_titles)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for title in movie_titles:
        file.write(f"{title}\n")