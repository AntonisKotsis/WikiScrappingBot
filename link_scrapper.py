import bs4 as bs
import httplib2
from bs4 import SoupStrainer
initial_link="https://en.wikipedia.org/wiki/List_of_films:_F#F"
file_name="wikilinksV2.txt"
http=httplib2.Http()
status,response=http.request(initial_link)
file=open(file_name,"a")
for link in bs.BeautifulSoup(response,"html.parser", parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])
        file.write(link['href'])
        file.write("\n")
file.close()