import requests
from bs4 import BeautifulSoup
import pprint


class ScapeYCombinator():

    def scape_live():
        url = "https://news.ycombinator.com/news"

        response = requests.get(url)
        yc_page = response.text

        soup = BeautifulSoup(yc_page, "html.parser")
        items = soup.find_all("span", {"class": "titleline"})
        scores = soup.find_all("span", {"class": "score"})


        # scrape title, htmnl link, and upvote count

        for i in range(len(items)):
            item = items[i]
            score = scores[i]
            result = {
                "title": "",
                "link": "",
                "upvote count": ""
            }
            result["title"] = item.text
            result["link"] = item.find("a").get("href")
            result["upvote count"] = score.text
            pprint.pprint(result)




