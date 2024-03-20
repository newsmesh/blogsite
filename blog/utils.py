from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

""" try:
    page = requests.get('https://timesofindia.indiatimes.com/')
except Exception as e:
    print('error scraping this page')
time.sleep(2) """
url = 'https://timesofindia.indiatimes.com/'
s1 = HTMLSession()
r1 = s1.get(url).text
soup = BeautifulSoup(r1, 'lxml')
links = []
div_tag = soup.find_all('div', class_='col_l_6')
anchor = soup.find_all('a', class_='_3SqZy') # list of a tags
print(anchor[0].get('href'))  # get the href attribute from first link in anchor list
for a_tag in div_tag:
  link = a_tag.find('a')
  if link == None or link == '' or link == 'None':
    pass
  else:
    links.append(link.get('href'))
#print(links[0])
s1.close()

def pargraph(links):
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
        print('category', category[1].text)
    if title == None:
      pass
    else:
      print('title', title.text)
    para = soup.find('div', class_='_3YYSt clearfix')
    if para == None:
      pass
    else:
      print('para', para.text)  
      
for i in range(0,len(links)):
    pargraph(links[i])
  
""" s2 = HTMLSession()
r2 = s2.get(anchor[0].get('href')).text
soup = BeautifulSoup(r2, 'lxml')
title = soup.find('h1', class_='_1Y-96')
para = soup.find('div', class_='_3YYSt clearfix')
print(title.text)
print(para.text) """
""" data=[]
for i in link:
    data.append(i.text)
    #print(i.text)
    print(end='')
df = pd.DataFrame(data)
df.to_csv('file2.csv', header=False, index=False) """