from bs4 import BeautifulSoup
import requests
import json


def getInformationComic(url):
    try:
        res = requests.get("https://komiku.id" + url)
        soup = BeautifulSoup(res.text, "html.parser")
        getMainElement = soup.find("main").find("article")
        genreData = []
        totalChapter = 0

        informationSection = getMainElement.find("section", {"id": "Informasi"})
        title = (
            informationSection.find("table", {"class": "inftable"})
            .find_all("tr")[0]
            .find_all("td")[1]
            .text
        )
        cover_comic = informationSection.find("div").find("img").get("src")
        typeComic = (
            informationSection.find("table", {"class": "inftable"})
            .find_all("tr")[2]
            .find_all("td")[1]
            .find("b")
            .text
        )
        author = (
            informationSection.find("table", {"class": "inftable"})
            .find_all("tr")[4]
            .find_all("td")[1]
            .text
        )
        status = (
            informationSection.find("table", {"class": "inftable"})
            .find_all("tr")[5]
            .find_all("td")[1]
            .text
        )

        for genre in informationSection.find("ul").find_all("li"):
            getGenre = genre.find("a").find("span").text
            genreData.append(getGenre)
        
        chapters = getMainElement.find("table", {"id": "Daftar_Chapter"})

        for index, _ in enumerate(chapters.find_all("tr")):
            totalChapter = index

        return {
            "title": title,
            "source": "https://komiku.id" + url,
            "informations": {
                "cover_comic": cover_comic,
                "type": typeComic,
                "author": author,
                "status": status,
            },
            "genres": genreData,
            "total_chapter": totalChapter
        }
    except Exception as e:
        return {"status": 500, "message": str(e), "data": []}