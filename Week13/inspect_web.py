import requests, bs4
res = requests.get('http://nostarch.com')
res.raise_for_status()

nSoup = bs4.BeautifulSoup(res.text, 'html.parser' )
exampleFile = open('my_web_file.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')

elems = exampleSoup.select('title')
type(elems)
len(elems)
#print(len(elems))

str(elems[0])
elems[0].getText()
titulo = elems[0].getText()
print(titulo)

pElems = exampleSoup.select('a')

str(pElems[0])
pElems[0].getText()
texto = pElems[0].getText()
print(texto)

str(pElems[1])
pElems[1].getText()
texto = pElems[1].getText()
print(texto)
