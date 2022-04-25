import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    parsed_link = urlparse(url)
    link = parsed_link[1] + parsed_link[2]
    response = requests.get(
        'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(link),
        headers=headers
        )
    return response.ok


def shorten_link(token, url):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    body = {
        'long_url': url
    }
    response = requests.post(
        'https://api-ssl.bitly.com/v4/bitlinks',
        headers=headers,
        json=body
        )
    response.raise_for_status()
    return response.json().get('link')


def count_clicks(token, url):
    parsed_url = urlparse(url)
    url_path = parsed_url[1] + parsed_url[2]
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(
            url_path),
        headers=headers
    )
    response.raise_for_status()
    return response.json().get('total_clicks')


def is_url_viable(url):
    response = requests.get(url)
    response.raise_for_status()


if __name__ == "__main__":
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser(
        description='Ссылка для формирования битлинка или возврата кол-ва кликов'
    )
    parser.add_argument('url', help='Ссылка')
    args = parser.parse_args()
    url = args.url
    is_url_viable(url)
    try:
        if not is_bitlink(token, url):
            print('Битлинк:', shorten_link(token, url))
        else:
            print('Количество кликов:', count_clicks(token, url))
    except requests.exceptions.HTTPError:
        print('Неверная ссылка')
