'''Downloads each homepage in the provided list of links
'''

import os
from urllib.parse import urlparse


class ImageGetter:
    def __init__(self, links, directory):
        if director[-1] != '/':
            directory += '/'
        self.dir = directory
        self.links = links
        self.webkit_call = 'webkit2png --dir={} {}'

    def scrape_homepages(self):
        for link in self.links:
            parsed_url = urlparse(link)
            download_dir = '{}{}'.format(self.dir, parsed_url.netloc)
            self.make_directory(download_dir)
            self.download(download_dir, link)

    def download(self, directory, link):
        self.system_call(self.webkit_call.format(directory, link)

    def make_directory(self, directory):
        self.system_call('mkdir {}'.format(directory))

    def system_call(self, call):
        try:
            os.system(call)
        except Exception as e:
            print("Exception occurred: {}".format(str(e)))
