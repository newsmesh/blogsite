from sqlite3 import IntegrityError
from django.db.utils import IntegrityError as djangoDB_IntegrityError
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import time
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from requests_html import HTMLSession
# from googletrans import Translator
# translater=Translator()
from deep_translator import GoogleTranslator
from blog.models import Blog

  
def get_links():
  url = 'https://timesofindia.indiatimes.com/'
  s1 = HTMLSession()
  r1 = s1.get(url).text
  soup = BeautifulSoup(r1, 'lxml')
  links = []
  div_tag = soup.find_all('div', class_='col_l_6')
  anchor = soup.find_all('a', class_='_3SqZy') # list of a tags
  #print(anchor[0].get('href'))  # get the href attribute from first link in anchor list
  for a_tag in div_tag:
    link = a_tag.find('a')
    if link == None or link == '' or link == 'None':
      pass
    else:
      links.append(link.get('href'))
  s1.close()
  #print(links[0])
  return links

def pargraph(links):
    blog_model = Blog()
    s2 = HTMLSession()
    r2 = s2.get(links).text
    soup = BeautifulSoup(r2, 'lxml')
    title = soup.find('h1', class_='_1Y-96')
    c_div = soup.find('div', class_='_1nPcO')
    if c_div == None:
      pass
    else:
      category = c_div.find_all('li')
      if category == None:
        pass
      else:
        #print('category', category[1].text)
        blog_model.category = category[1].text
    if title == None:
      pass
    else:
      # print('title', title.text)
      # ------ for image ----#
      img_div_tag = soup.find('div', class_='_3gupn')
      if img_div_tag == None:
        pass
      else:
        img_tag = img_div_tag.find('img')
        if img_tag == None:
          pass
        else:
          blog_model.img_src = img_tag['src']

      title_to_translate = title.text
      translated_title = GoogleTranslator(source='english', target='hindi').translate(title_to_translate)
      #print("News",translated_title)
      blog_model.title = translated_title
      for_slug = translated_title.replace(' ', '-')
      blog_model.slug = for_slug
      para = soup.find('div', class_='_3YYSt clearfix')
      def summary(par):
        # Input text - to summarize
        text = str(par)
  
        # Tokenizing the text
        stopWords = set(stopwords.words("english"))
        words = word_tokenize(text)
  
        # Creating a frequency table to keep the
        # score of each word
        freqTable = dict()
        for word in words:
          word = word.lower()
          if word in stopWords:
            continue
          if word in freqTable:
            freqTable[word] += 1
          else:
            freqTable[word] = 1
  
        # Creating a dictionary to keep the score
        # of each sentence
        sentences = sent_tokenize(text)
        sentenceValue = dict()
        for sentence in sentences:
          for word, freq in freqTable.items():
            if word in sentence.lower():
              if sentence in sentenceValue:
                sentenceValue[sentence] += freq
              else:
                sentenceValue[sentence] = freq
  
        sumValues = 0
        for sentence in sentenceValue:
          sumValues += sentenceValue[sentence]
  
        # Average value of a sentence from the original text
        average = int(sumValues / len(sentenceValue))
  
        # Storing sentences into our summary.
        summary = ''
        for sentence in sentences:
          if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
        #print("+++++++++++++++++ SUMMARY +++++++++++++++++++++++++++++++++++++++++++++++")
        #print(summary)
        #print("=============================== TRANSLATION  ===========================")
        summary.lower()
        #out=translater.translate(summary,dest="hindi")
        summary_to_translate = summary
        translated_summary = GoogleTranslator(source='english', target='hindi').translate(summary_to_translate)
        #print(translated) # summary
        blog_model.content = translated_summary
        blog_model.discription = translated_summary[:100] + '...'
      if para == None:
        pass
      else:
        s = para.text
        #print('para', para.text)
        summary(s)
      try:
        blog_model.save()
      except djangoDB_IntegrityError:
        pass
""" for i in range(0,len(links)):
    s = pargraph(links[i]) """