'''Retreives the href values from each link in the provided list of links
'''

import bs4

class Scraper:
    def __init__(self):
        self.links = list()
        self.search_pages = list()

    def get_links_from_page(self, page, num_pages):
        soup = bs4.BeautifulSoup(page, 'html.parser')

        if len(self.search_pages) == 0 and num_pages > 1:
            # get Google footer links
            self.search_pages = soup.find_all('a', {'class': 'fl'})

        self.clean_up_links(soup.find_all('div', {'class': 'g'}))

    def clean_up_links(self, data):
        '''Whittle down data list until we just have the hrefs'''
        for div in data:
            link = div.find('a')['href']
            link = link.split('&sa=')[0]
            link = link.replace('/url?q=', '')

            # if not internal Google link
            if '/search?q=' not in link.lower():
                self.links.append(link)

    def next_url(self):
        if len(self.search_pages) == 0:
            return ''
        return self.search_pages.pop(0)['href']
