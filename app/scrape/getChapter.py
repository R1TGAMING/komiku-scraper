from bs4 import BeautifulSoup
import requests
import json


def getChapter(url, title):
    try:
        comicData = []
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        totalPage = 0

        if res.status_code != 200:
            return {"status": res.status_code, "message": "failed to fetch, comic not found or chapter not found", "data": []}

        comic = soup.find("div", {"id": "Baca_Komik"}).find_all("img")
        title = soup.find("div", {"id": "Baca_Komik"}).find("h2").text

        for index, comic in enumerate(comic):
            comicData.append({"page": index, "image": comic.get("src")})
            totalPage = index

        return {
            "status": res.status_code,
            "message": "success",
            "data": {"title": title, "total_page": totalPage, "chapters": comicData},
        }
    except Exception as e:
        return {"status": 500, "message": str(e), "data": []}
