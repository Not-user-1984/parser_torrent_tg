from parser.get_main_html import get_and_save_html

url = 'http://rutor.info/top'
file_path = 'parser/my_html/rutor_top.html'


def main():
    get_and_save_html(
        url=url,
        file_path=file_path)


if __name__ == "__main__":
    main()
