import requests
from bs4 import BeautifulSoup as BS
import re


def free_proxy():
    url = 'https://free-proxy-list.net/'
    request = requests.get(url)
    bs = BS(request.text, 'lxml')
    table = bs.find('table', class_='table').find_all('tr')
    all_proxies = []
    for el in table:
        proxies = list(map(lambda x: x.findNext('td').text, el))[-2:]
        if re.match(r'\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}', proxies[1]):
            all_proxies.append(proxies[::-1])
    print(f'Обнаружено {len(all_proxies)} бесплатных прокси:')
    for i, c in enumerate(all_proxies, 1):
        print(f'{i}) {c[0]} ({c[1]})')


if __name__ == '__main__':
    free_proxy()
