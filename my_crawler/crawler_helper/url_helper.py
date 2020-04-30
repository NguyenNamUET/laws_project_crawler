import requests
import re

from bs4 import BeautifulSoup


def load_url(url, return_content=False):
    response = requests.get(url)
    try:
        response.raise_for_status()
        if not return_content:
            return response
        else:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
    except Exception as e:  # This is the correct syntax
        print(e)


def get_id_from_url(url):
    regex = re.search('(/[0-9]+/)|(-[0-9]+.aspx)', url)
    id_index = list(regex.span())
    result = url[id_index[0]:id_index[1]]
    return re.sub(".aspx|/|-", "", result)


def get_id_from_url__vbpl(url):
    regex = re.search('(=[0-9]+)', url)
    id_index = list(regex.span())
    return url[id_index[0]+1 : id_index[1]]



