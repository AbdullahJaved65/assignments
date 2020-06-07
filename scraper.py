import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.findAll("a"):
            url = tag.get("href")
            print("\n" + url)


##scrape = Scraper("https://news.google.com")
##scrape.scrape()
news = "https://news.google.com"
Scraper(news).scrape()