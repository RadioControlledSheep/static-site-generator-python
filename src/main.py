import sys

from copystatic import copy_files_recursive
from generate_html import generate_pages_recursive


def main():
    if len(sys.argv) != 2:
        copy_files_recursive("./static", "./docs")
        generate_pages_recursive("./content", "template.html", "./docs", "/")
        sys.exit(0)
    # book_filepath = "books/frankenstein.txt"
    basepath = sys.argv[1]
    copy_files_recursive("./static", "./docs")
    generate_pages_recursive("./content", "template.html", "./docs", basepath)
    print(basepath)


main()
