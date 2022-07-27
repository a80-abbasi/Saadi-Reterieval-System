import re
import os
import requests
from bs4 import BeautifulSoup
import csv

url_dict = {'golestan': 'https://ganjoor.net/saadi/golestan/dibache',
            'boostan': 'https://ganjoor.net/saadi/boostan/niyayesh/sh1'}


def main_spider(root_url, main_url, directory):

    url = root_url
    chapter_number = 0

    while True:
        source_code = requests.get(url)
        soup = BeautifulSoup(source_code.text, features='html.parser')
        section = url.split('/')[-1]

        filename = f'{directory}/bab{chapter_number}/{section}.txt'
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding='utf-8') as f:
            for div in soup.findAll('div', {'class': ['b', 'n']}):
                for m in div.findAll('p'):
                    f.write(f'{m.get_text()}\n')
                f.write('\n')

        next_link = soup.find('div', {'class': 'navleft'})
        a_tag = next_link.find('a')
        if not a_tag:
            break
        url = main_url + a_tag.attrs.get('href')

        if not re.match(r".*/sh\d", url):
            url += '/sh1'
            print(f'{directory}/bab{chapter_number}/{section}')
            chapter_number += 1


def get_information(url):
    source_code = requests.get(url)
    soup = BeautifulSoup(source_code.text, features='html.parser')
    par_list = []
    for paragraph in soup.findAll('p'):
        par_list.append(paragraph.text)
    return '\n'.join(par_list)


main_spider(url_dict['golestan'], 'https://ganjoor.net/', 'golestan')
