import time

import requests
from bs4 import BeautifulSoup


class MakeHeadLine:
    def __init__(self, url, limit, opt):
        self.opt = opt
        self.url = url  # 크롤링할 url
        self.limit = limit  # 가져올 뉴스 기사 수

    def _creat_soup(self):
        try:
            res = requests.get(self.url)
        except:
            time.sleep(2)
            res = requests.get(self.url)

        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        return soup

    def crawl_headline_news(self):
        soup = self._creat_soup()
        news_list = soup.find("ul", attrs={"class": "hdline_article_list"}).find_all("li", limit=self.limit)
        res = []
        for i, news in enumerate(news_list):
            title = news.find("a").get_text().strip()
            link = self.url + news.find("a")["href"]
            print("{}. {}", format(i + 1, title))
            print(" (링크 : {}".format(link))
            res.append([title, link])
        return res


if __name__ == '__main__':

    opt = 1
    if opt == 1: # 정치
        url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
    elif opt == 2: #경체
        url = 'http://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=101'
    elif opt == 3: #사회
        url = 'http://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=102'
    elif opt == 4: #생활/문화
        url = 'http://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=103'
    elif opt == 5: #IT/과학
        url = 'http://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105'
    elif opt == 6: #세계
        url = 'http://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=104'
    ins_hl = MakeHeadLine(opt=1, url=url, limit=5)
    res = ins_hl.crawl_headline_news()
