import requests
from bs4 import BeautifulSoup

def get_text_from_web(url):
    """
    Скачивает страницу и возвращает весь текст из абзацев
    """
    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "lxml")

    paragraphs = soup.find_all("p")

    text = "\n".join(p.get_text() for p in paragraphs)

    return text
