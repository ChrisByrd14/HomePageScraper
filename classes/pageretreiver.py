'''Retrieves HTML from Google search page, sends to
   Scraper to whittle down to just links
'''

import requests
import classes.scraper as scraper


class PageRetreiver:
    def __init__(self, query, num_pages):
        query.replace(' ', '+')
        self.url = ('https://www.google.com/search?q={}'
                    '&ie=utf-8&oe=utf-8'.format(query))
        self.pages = list()
        self.requested_pages = num_pages
        self.scraper = scraper.Scraper()

    def get_pages(self):
        try:
            self.loop_over_pages()
        except Exception as e:
            print('Exception raised: {}'.format(str(e)))

        return self.pages

    def loop_over_pages(self):
        while self.requested_pages > 0:
            self.get_page()
            self.scraper.get_links_from_page(self.pages[-1],
                                             self.requested_pages)
            next_url = self.scraper.next_url()
            self.url = 'https://www.google.com{}'.format(next_url)
            self.requested_pages -= 1

    def get_page(self):
        page = requests.get(self.url)

        if page.status_code != 200:
            raise Exception('Retrieved page returned HTTP status'
                            ' code {}.'.format(page.status_code))

        self.pages.append(page.content)

    def get_links(self):
        return self.scraper.links
