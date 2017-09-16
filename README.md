# HomePageScraper

## About
Gets a screenshot of pages returned from a Google search. This application requires the webkit2png command line tool. If you don't already have it you can learn about getting it [here](http://www.paulhammond.org/webkit2png).

## Dependencies
This application works on Python 3, and you'll need `pip` to install its Python-related dependencies. You can install its requirements by running the following in the terminal:

```bash
pip install -r requirements.txt
```

## Usage
```bash
usage: main.py [-h] [-q QUERY] [-n NUM_PAGES]

optional arguments:
  -h, --help            show this help message and exit
  -q QUERY, --query QUERY
                        The search query
  -n NUM_PAGES, --num-pages NUM_PAGES
                        Max number of search pages to scrape
```
