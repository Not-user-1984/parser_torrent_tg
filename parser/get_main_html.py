
import requests
import logging


def get_and_save_html(url, file_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)

        print(f'HTML-документ сохранен в файл: {file_path}')
    except requests.exceptions.RequestException as e:
        logging.error(f'Не удалось получить доступ к странице по URL: {url}')
        logging.exception(e)
