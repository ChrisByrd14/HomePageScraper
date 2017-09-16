'''Stores logic to parse CLI arguments.
'''

import argparse


class CLIParser:
    def __init__(self):
        '''Initialize ArgumentParser'''
        parser = argparse.ArgumentParser()

        parser.add_argument('-q', '--query', type=str, help='The search query')
        parser.add_argument('-n', '--num-pages',
                            type=int,
                            help='Max number of search pages to scrape',
                            default=1)

        self.parser = parser

    def parse_args(self, arguments):
        '''Parses provided arguments and returns named tuple'''
        return self.parser.parse_args(arguments)
