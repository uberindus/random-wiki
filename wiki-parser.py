import urllib.request, urllib.error, urllib.parse
import re
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Special:Random'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

content_body = soup.findChildren("div", class_="mw-parser-output")[0]

heading = soup.find_all("h1")[0].text

result_string = heading + "\n" + "-------------------------------------------------------------\n"

text_bodies = content_body.findChildren(["p", "h2", "h3", "ul"], class_=False, recursive=False)
for tag in text_bodies: 
	if tag.name == "h2" or tag.name == "h3":
		h_text = tag.text
		h_text = re.sub(r'\[edit\]', "", h_text)
		result_string += "\n" + h_text + "\n" + "\n"
	elif tag.name == "ul":
		for child in tag.find_all("li"):
			result_string += "*  " + child.text + "\n"
	else:
		result_string += tag.text + "\n"

print(result_string)