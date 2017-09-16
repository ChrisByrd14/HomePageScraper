'''Retrieves HTML from Google search page
'''

import requests


class PageRetreiver:
    url = 'https://www.google.com/search?q={}&ie=utf-8&oe=utf-8'

    @staticmethod
    def get(query):
        query.replace(' ', '+')
        page = requests.get(PageRetreiver.url.format(query))

        if page.status_code != 200:
            raise PageRetreiverException('Retrieved page returned HTTP status'
                                         ' code {}.'.format(page.status_code))

        return page.content


class PageRetreiverException(Exception):
    pass
