import bs4 as bs
import urllib.request
sauce = urllib .request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce,'lxml')
nav = soup.nav
############## praragraphs Links text############
#print(soup.find_all('p'))
#print(soup.get_text())
#for paragraph in soup.find_all('p'):
 #   print(paragraph)
##for url in soup.find_all('a'):
##    print(url.get('href'))

#####################Navigating Tags###################

##for url in nav.find_all('a'):
##    print(url.get('href'))

##body = soup.body
##for paragraph in body.find_all('p'):
##    print(paragraph.text)
##for div in soup.find_all('div', class_='body'):  #### all text between div text########
##    print(div.text)

############### Tables and XML#############################
##table = soup.table
##table = soup.find('table')
##table_rows = table.find_all('tr')
##for tr in table_rows:
##    td = tr.find_all('td')
##    row = [i.text for i in td]
##    print(row)
###################### Pandas way of html scraping################
import pandas as pd
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header = 0)
for df in dfs:
     print(df)


