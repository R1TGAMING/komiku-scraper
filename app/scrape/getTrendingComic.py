from bs4 import BeautifulSoup
import requests
import json


def getTrendingComic(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = []

    findElement = (
        soup.find(id="Trending_Komik")
        .find("div", {"class": "perapih"})
        .find("div", {"class": "ls112"})
        .find("div", {"class": "ls12"})
    )

    for item in findElement.find_all("article"):
        title = item.find("div", {"class": "ls2j"}).find("h3").find("a").text
        image = item.find("div", {"class": "ls2v"}).find("a").find("img").get("src")
        src = "https://komiku.id/" + item.find("div", {"class": "ls2v"}).find("a").get(
            "href"
        )
        genre = item.find("div", {"class": "ls2j"}).find("span").text
        latestChapter = item.find("div", {"class": "ls2j"}).find("a").text
        srcLatestChapter = "https://komiku.id/" + item.find(
            "div", {"class": "ls2j"}
        ).find("a").get("href")

        json = {
            "title": title,
            "image": image,
            "source": src,
            "genre": genre,
            "latestChapter": latestChapter,
            "srcLatestChapter": srcLatestChapter,
        }
        data.append(json)

    if res.status_code != 200:
        return {"status": res.status_code, "message": "failed", "data": []}
    else:
        return {"status": res.status_code, "message": "success", "data": data}
