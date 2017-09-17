'''Stores logic to parse CLI arguments.
'''

import argparse


class CLIParser:
    def __init__(self):
        '''Initialize ArgumentParser'''
        parser = argparse.ArgumentParser()

        parser.add_argument('-q',
                            '--query',
                            type=str,
                            help='The search query to run.')
        parser.add_argument('-n',
                            '--num-pages',
                            type=int,
                            help=('Max number of search pages to scrape.'
                                  'Default value is 1 page.'),
                            default=1)
        parser.add_argument('-d', '--directory',
                            type=str,
                            help=('The directory to download the images'
                                  ' to. Defaults to your home directory.'),
                            default='~')

        self.parser = parser

    def parse_args(self):
        '''Parses CLI arguments and returns named tuple'''
        return self.parser.parse_args()
