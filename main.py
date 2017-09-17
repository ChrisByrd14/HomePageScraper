#!/usr/local/bin/python3

import classes.cliparser as cli
import classes.pageretreiver as pr
import classes.imagegetter as ig
import sys


def main():
    parser = cli.CLIParser()
    args = parser.parse_args()

    retreiver = pr.PageRetreiver(args.query, args.num_pages)
    retreiver.get_pages()

    if len(retreiver.pages) == 0:
        print('No pages were retreived. Exiting application.')
        sys.exit(1)

    links = retreiver.get_links()

    getter = ig.ImageGetter(links, args.directory)
    getter.scrape_homepages()


if __name__ == '__main__':
    main()
