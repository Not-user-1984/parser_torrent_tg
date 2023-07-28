from bs4 import BeautifulSoup

import re
from unidecode import unidecode


def generate_filename(text):
    text_lower = text.lower()
    movie_name_translit = re.sub(r'\s+', '_', unidecode(text_lower))
    return movie_name_translit


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_html_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def parse_movies_to_html(soup, text, output_file):
    target_link = soup.find('a', text=text)
    if target_link:
        parent_element = target_link.parent
        next_block = parent_element.find_next_sibling()
        if next_block:
            write_html_file(output_file, next_block.prettify())
            print(f"Блок после заголовка '{text}' сохранен в файл '{output_file}'.")
        else:
            print("Следующий блок не найден.")
    else:
        print("Заголовок не найден.")


def parse_movie_info(soup, text):
    movie_elements = soup.find_all('a', class_='downgif', href=True)
    if movie_elements:
        for movie_element in movie_elements:
            movie_name_element = movie_element.find_parent('td')
            movie_name = movie_name_element.text.strip()
            download_link = movie_element['href']
            size_element = movie_name_element.find_next('td', attrs={'align': 'right'})
            size =size_element.find_next_sibling('td')
            print(f"Название: {movie_name}")
            print(f"Ссылка на скачивание: http:{download_link}")
            print(f"Размер: {size.text}")
            print("---")
    else:
        print("Фильмы не найдены.")


file_path = 'parser/my_html/rutor_top.html'
html_content = read_html_file(file_path)

soup = BeautifulSoup(html_content, 'html.parser')


text = 'Зарубежные фильмы'
name__path = generate_filename(text)
movie_path = f"parser/my_html/{name__path}.html"

parse_movies_to_html(soup, text, movie_path)

movie_content = read_html_file(movie_path)
soup_movie = BeautifulSoup(movie_content, 'html.parser')

parse_movie_info(soup_movie,text)
