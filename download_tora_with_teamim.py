import os
import requests
import bs4
import re


def download():
    def filter(soup, name=None, attrs={}):
        for span in soup.find_all(name, attrs):
            span.decompose()

    psukim = []
    for i in range(1, 55):
        URL = "http://www.shabat-shalom.info/books/Tanach-he/t/{}.htm".format(i)
        print(URL)
        response = requests.get(URL)
        soup = bs4.BeautifulSoup(response.content.decode("UTF-8"), "html.parser")
        filter(soup, "span", {"class": "chNmb"})
        filter(soup, "span", {"class": "chSofP"})
        filter(soup, "span", {"class": "chSofS"})
        filter(soup, "span", {"class": "chAliya"})
        filter(soup, "span", {"class": "chRev"})
        filter(soup, "br")

        chapter = soup.find_all("p", {"class": "chText"})

        for parshia in chapter:
            for pasuk in parshia.text.split("׃"):
                pasuk = re.sub(r"{ש}", "", pasuk)  # remove end of Humash marking
                pasuk = re.sub(r"\n", "", pasuk)  # remove end of line
                pasuk = re.sub(' +', ' ', pasuk) # remove double spaces
                pasuk = pasuk.strip()
                if pasuk:
                    psukim.append(pasuk)

    return psukim


fName = "raw_data.txt"


def get_data():
    if os.path.exists(fName):
        return open(fName).readlines()
    psukim = download()
    with open(fName, "w", encoding="utf-8") as outFile:
        outFile.write("\n".join(psukim))
    return psukim
