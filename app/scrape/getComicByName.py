from bs4 import BeautifulSoup
import requests
import json
from .getInformationComic import getInformationComic

def getComicByName(url):
    try :
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        data = []

        if res.status_code != 200:
            return {"status": res.status_code, "message": "failed to fetch, comic not found", "data": []}
        
        findElement = soup.find_all("div", {'class': 'bge'})

        for element in findElement:
            src = element.find("a").get("href")
            data.append(getInformationComic(src))

        return {"status": res.status_code, "message": "success", "data": data}
    except Exception as e:
        return {"status": 500, "message": str(e), "data": []}