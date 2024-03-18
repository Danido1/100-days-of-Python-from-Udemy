import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
webpage = response.text


soup = BeautifulSoup(webpage, "html.parser")



all_titles = soup.find_all(name="h3", class_="title")

all_titles_list = [title.getText() for title in all_titles]
print(all_titles_list)



inverselist = all_titles_list[::-1]
print(inverselist)

with open("topmovies.txt", "w", encoding="utf-8") as file:
    for movie in inverselist:
        file.write(f"{movie}\n")

