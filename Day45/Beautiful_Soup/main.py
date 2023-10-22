from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
ys_web_page = response.text

soup = BeautifulSoup(ys_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
sorted_upvotes = sorted(article_upvotes, reverse=True)
# print(sorted_upvotes)
# print(article_upvotes.index(456))

for upvote in sorted_upvotes:
    print(f"{upvote} {article_texts[article_upvotes.index(upvote)]} {article_links[article_upvotes.index(upvote)]}")
