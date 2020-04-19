import ast
import time
import re
import math
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from jsonschema import validate
import html2text
from itertools import zip_longest
import sys

from constant.crawler_contants import SCHEMA

def remove_accents(input_str):
    s1 = u'ÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝàáâãèéêìíòóôõùúýĂăĐđĨĩŨũƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẼẽẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỲỳỴỵỶỷỸỹ'
    s0 = u'AAAAEEEIIOOOOUUYaaaaeeeiioooouuyAaDdIiUuOoUuAaAaAaAaAaAaAaAaAaAaAaAaEeEeEeEeEeEeEeEeIiIiOoOoOoOoOoOoOoOoOoOoOoOoUuUuUuUuUuUuUuYyYyYyYy'
    s = ''
    for c in input_str:
        if c in s1:
            s += s0[s1.index(c)]
        else:
            s += c
    return s


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def second_to_hhmmss(second):
    return time.strftime('%H:%M:%S', time.gmtime(math.ceil(second)))


def to_Date(string):
    date = string[:4] + "-" + string[4:6] + "-" + string[6:8]
    time = string[9:11] + ":" + string[11:13] + ":" + string[13:]
    date_time = datetime.strptime(date+" "+time, "%Y-%m-%d %H:%M:%S")
    return date_time


def is_validate_json(json_object):
    try:
        return validate(instance=json_object, schema=SCHEMA)
    except Exception as e:
        return str(e)


def keep_one_white_space(string):
    return re.sub(' +', ' ', string)


def extract_raw_text_from_html(html_text):
    if html_text == "":
        return ""
    else:
        text = html2text.html2text(html_text)
        text = re.sub('(\*|\||\_|\-)', '', text)
        text = text.replace("\\", "")
        text = re.sub(r'\n\s*\n', '\n\n', text)
        return keep_one_white_space(text)


def countdown(t):
    while t > 0:
        timeformat = time.strftime('%d:%H:%M:%S', time.gmtime(t))
        sys.stdout.write('\rDuration : {}s'.format(timeformat))
        t -= 1
        sys.stdout.flush()
        time.sleep(1)
