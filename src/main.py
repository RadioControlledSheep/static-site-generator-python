from copystatic import copy_files_recursive
from generate_html import generate_page


def main():
    copy_files_recursive("./static", "./public")
    generate_page("./content/index.md", "template.html", "./public/index.html")


main()
