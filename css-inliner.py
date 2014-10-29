#!/usr/bin/python

# Example:
# ./css-inliner.py -f index.html -c main.css

from lxml import html
from converter import Conversion
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename", help="Input file")
parser.add_option("-c", "--css",  dest="css",      help="Css file")

def main():
    (options, args) = parser.parse_args()
    if options.filename is None or options.css is None:
        raise Exception("Missing arguments filename and css")

    htmlFile = open(options.filename)
    htmlString = htmlFile.read()
    cssFile = open(options.css)
    css = cssFile.read()

    document = html.fromstring(htmlString)

    converter = Conversion()
    converter.perform(document, document, css)

    print converter.convertedHTML

if __name__ == '__main__':
    main()
