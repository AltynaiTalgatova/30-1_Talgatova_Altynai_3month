import datetime
import requests
from bs4 import BeautifulSoup
from pprint import pprint


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/"
              "apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}


def get_url(year, month, day, ordering):
    url = f"https://www.securitylab.ru/news/" \
          f"{year}-{month}-{day}" \
          f"&order={ordering}"
    return url


def get_html(url):
    response = requests.get(url=url, headers=HEADERS)
    return response


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all(
        "div",
        class_="article-card",
        limit=8
    )
    parserd_data = []
    for item in items:
        parserd_data.append({
            "title": item.find("h2", class_="article-card-title").getText(),
            "time": item.find("time").get("datetime"),
            "url": item.find("a", class_="article-card").get("href"),
            "image": item.find("img").get("src")
        })
    return parserd_data


def parser():
    current_date = datetime.datetime.now()
    url = get_url(current_date.year, current_date.month, current_date.day, "time")
    html = get_html(url)
    parsed_data = get_data(html.text)
    return parsed_data
