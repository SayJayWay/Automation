#1 python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

print('Googling...')    # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a broser tab for each result.
linkElems = soup.select('. r') # Google class tags may be different than 'r' now
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.ca' + linkElems[i].get('href'))
