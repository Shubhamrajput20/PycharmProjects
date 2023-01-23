from bs4 import BeautifulSoup
with open("beautifulsoup4 · PyPI.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

print(soup.prettify())
for link in soup.find_all('a'):
    print(link.get('href'))

heading_tags = ["h1", "h2", "h3"]
for tags in soup.find_all(heading_tags):
    print(tags.text.strip())
