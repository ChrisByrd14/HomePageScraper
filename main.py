#!/usr/local/bin/python3

import cliparser
import pageretreiver
import scraper
import sys


def main():
    parser = cliparser.CLIParser()
    arguments = parser.parse_args(sys.argv[1:])

    try:
        page = pageretreiver.PageRetreiver.get(arguments.query)
    except pageretreiver.PageRetreiverException as e:
        print('Exception raised: {}'.format(str(e)))
        sys.exit(1)

    print(page)


if __name__ == '__main__':
    main()
