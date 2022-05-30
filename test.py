from newspaper import Article

# 크롤링할 url 주소 입력
url = 'https://www.mk.co.kr/star/broadcasting-service/view/2022/05/459717/'

article = Article(url, language='ko') # 한국어 language='ko'
article.download()
article.parse()

# 기사 제목 가져오기
newTitle = article.title
print(newTitle)

text = article.text
print(text)

