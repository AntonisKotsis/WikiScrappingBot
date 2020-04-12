from bs4 import BeautifulSoup
from urllib.request import urlopen
input_file=open("wikilinksV2.txt","r")
path=input_file.readline()
out_file_name=""


while(path!="end"):
    html = urlopen("https://en.wikipedia.org/" + path)
    data = html.read()
    wiki = BeautifulSoup(data, "html.parser")

    for t in wiki.select('title'):
        #print(t.getText())
        out_file_name = t.getText()
       # print(out_file_name)
        file = open(out_file_name, "w")
        file.write(out_file_name + "\n" + "\n")
    for i in wiki.select('p'):
       # print(i.getText())
        file.write(i.getText() + "\n")
    path = input_file.readline()
   # print(path)
