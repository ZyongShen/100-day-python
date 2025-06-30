from bs4 import BeautifulSoup

with open("day-45-beautiful-soup/bs4-start/website.html") as fd:
    contents = fd.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.prettify())