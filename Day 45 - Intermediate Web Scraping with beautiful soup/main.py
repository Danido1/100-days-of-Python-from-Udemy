import requests
from bs4 import BeautifulSoup
import requests
# import lxml

response = requests.get("https://news.ycombinator.com/front")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

#Get first text, url and upvote
first_article_text = soup.find(name="span", class_="titleline").find(name="a").getText()
first_article_url = soup.find(name="span", class_="titleline").find(name="a").get("href")
first_article_points = soup.find(name="span", class_="score").getText()

#Get all text, urls and upvotes and add it to a list
all_articles_text_list = []
all_articles_url_list = []
all_articles_points_list = []

all_articles_span = soup.find_all(name="span", class_="titleline")
for span in all_articles_span:
    text_of_articles = span.find(name="a").getText()
    all_articles_text_list.append(text_of_articles)

for span in all_articles_span:
    url_of_articles = span.find(name="a").get("href")
    all_articles_url_list.append(url_of_articles)

all_article_upvotes = soup.find_all(name="span", class_="score")
for article in all_article_upvotes:
    points_of_articles = int(article.getText().split()[0])
    all_articles_points_list.append(points_of_articles)

print(all_articles_text_list)
print(all_articles_url_list)
print(all_articles_points_list)



# all_article_url = soup.find(name="span", class_="titleline").find(name="a").get("href")
# all_article_points = soup.find(name="span", class_="score").getText()

max_index = all_articles_points_list.index(max(all_articles_points_list))
print(max_index)

print(all_articles_text_list[max_index], all_articles_url_list[max_index])






# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.h1)
#
# all_anchor_tags = soup.find_all(name="a") #Search by tag name and return a list of all the items that match the search query
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#    #print(tag.getText)
#     print(tag.get("href")) #Get the values of all attributes of HTML
#
# heading = soup.find(name="h1", id="name") #Only find the first item that matchs the query
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading") #we use class_ in order to not clash with the class keyword.
# print(section_heading)
# print(section_heading.name)
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
#
# headings = soup.select(".heading")
# print(headings) #return a list of headings