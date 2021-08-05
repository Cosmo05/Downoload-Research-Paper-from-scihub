import requests 
from bs4 import BeautifulSoup
url= input("Paste Your URL/DOI here")
page = requests.get("https://sci-hub.se/"+url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

soup.find_all(id="buttons")
for item in soup.select("button[onclick^=\"location.href=\"]"):
    onclick = item["onclick"]
    href = onclick.split("=")[1]
    href = href.strip("'")
    href1 = href.replace("?download","")
print(href1)
url1 = "https:"+ href1
pdf1 = requests.get("https:"+str(href1))

pdf = open("paper.pdf", 'wb') 
pdf.write(pdf1.content) 
pdf.close()
