import requests
from bs4 import BeautifulSoup
from datetime import datetime

r = requests.get("https://qz.com/latest/")
r.text

if r.status_code == 200:
    soup = BeautifulSoup(r.text, "html.parser")
    articles = soup.find_all("article")

    for article in articles:
        title = article.find("h2")
        title_text = title.get_text(strip=True)if title else "Title not found"
        link = article.find("a")["href"] if article.find("a") else "Link not found"

        date = article.find("time")
        date_text = date["datetime"] if date else "Date not found"
        
        try:
            article_date = datetime.fromisoformat(date_text) if date_text != "Date not found" else "Date not found"
        except ValueError: article_date = "Invalid date format"
        
        print(f"Title: {title_text}")
        print(f"Published at: {article_date}")
        print(f"Link: {link}\n")
