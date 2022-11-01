import requests
URL = 'https://en.wikipedia.org/wiki/Michelangelo'
'''The wikipedia page is about the legendary artist Michel Angelo'''

from bs4 import BeautifulSoup



def get_citations_needed_count(url):
    '''A function that findes the html tags a ref for needed citations and returns the length of them'''
    URL = url
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = len(soup.find_all('a', text='citation needed'))
    return citations


def get_citations_needed_report(url):
    '''A function that findes the html tags a ref for needed citations and saves its contents and returns the content 
    with needed citation '''
    URL = url
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all('a', text='citation needed')
    entries = []
    for c in citations:
        entries.append(c.find_parents('p')[0].text.strip())
    result = '\n\n'.join(entries)
    return result

count = get_citations_needed_count(URL)
citations = get_citations_needed_report(URL)

print(f"{count} citations needed: \n\n")
print(citations)