'''Downloads each homepage in the provided list of links
'''

import os
from urllib.parse import urlparse


class ImageGetter:
    def __init__(self, links, directory):
        self.dir = directory
        self.links = links

    def scrape_homepages(self):
        for link in self.links:
            self.download(link)

    def download(self, link):
        try:
            parsed_url = urlparse(link)
            download_dir = '{}{}'.format(self.dir, parsed_url.netloc)
            os.system('mkdir {}'.format(download_dir))
            webkit_call = 'webkit2png --dir={} {}'.format(download_dir, link)
            os.system(webkit_call)
        except Exception as e:
            print("Exception occurred: {}".format(str(e)))
