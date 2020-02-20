import matplotlib.pyplot as plt
from wordcloud import WordCloud
from bs4 import BeautifulSoup
import nltk
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from urllib.request import urlopen

url = "https://ktk.kz/ru"
html = urlopen(url).read()
soup = BeautifulSoup(html)
features="html.parser"

for script in soup(["script", "style"]):
    script.extract()    
print(soup)


text = soup.get_text()
stop_words = set(stopwords.words('russian'))
words = word_tokenize(text)
print(words)
wordsFiltered = [word.lower() for word in words if word.isalpha()]
print(wordsFiltered)
filtered_words = [word for word in wordsFiltered if word not in stopwords.words('russian')]
print(filtered_words)


wc = WordCloud(max_words=100, margin=10, background_color='white',
scale=3, relative_scaling = 0.5, width=500, height=400,
random_state=1).generate(' '.join(filtered_words))
plt.figure(figsize=(30,15))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()

