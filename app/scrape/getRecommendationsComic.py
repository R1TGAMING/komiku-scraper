from bs4 import BeautifulSoup
import requests
import json
from .getInformationComic import getInformationComic


def getRecommendationsComic(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = []

    findElement = (
        soup.find(id="Rekomendasi_Komik")
        .find("div", {"class": "perapih"})
        .find("div", {"class": "ls112"})
        .find("div", {"class": "ls12"})
    )

    for item in findElement.find_all("article"):
        src = item.find("div", {"class": "ls2v"}).find("a").get("href")

        data.append(getInformationComic(src))

    if res.status_code != 200:
        return {"status": res.status_code, "message": "failed", "data": []}
    else:
        return {"status": res.status_code, "message": "success", "data": data}
