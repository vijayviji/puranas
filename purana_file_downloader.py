# -*- coding: utf-8 -*-
import hashlib
import os
import string

from requests import get
from dev_to_iast import devanagari_to_iast
from lxml import html

WEB = "https://sa.wikisource.org"

TYPE1 = {
    'titles': '//div[@class="mw-parser-output"]/table[3]//li/a/text()',
    'links': '//div[@class="mw-parser-output"]/table[3]//li/a/@href'
}

TYPE2 = {
    "titles": '//div[@class="CategoryTreeItem"]/a/text()',
    "links": '//div[@class="CategoryTreeItem"]/a/@href'
}

pathstoCheck = [
    '//div[@class="poem"]/p/text()',
    '//div[@class="poem"]/p[2]/span/text()',
    '//div[@class="poem"]/p/font/text()'
]


def is_leafpage(html_content):
    tree = html.fromstring(html_content)
    for xpathItem in pathstoCheck:
        content = tree.xpath(xpathItem)
        if len(content) != 0:
            return True

    return False


def parse_content(html_content):
    tree = html.fromstring(html_content)
    final_content = []
    for xpathItem in pathstoCheck:
        content = tree.xpath(xpathItem)
        print(xpathItem, content)
        if len(content) > 1:
            final_content += content
        elif len(content) > 0 and len(content[0]) > 5:
            final_content += content

    return final_content


def transliterate_page(html_content):
    result = []
    content = parse_content(html_content)
    for item in content:
        item = ' '.join(item.split())
        result.append(devanagari_to_iast(item))

    return result


def scrap_links_intermediate_page(html_content):
    tree = html.fromstring(html_content)
    titles = tree.xpath(TYPE1["titles"])
    links = tree.xpath(TYPE1["links"])
    result = {}
    for i in range(len(titles)):
        title = devanagari_to_iast(titles[i])
        result[title] = WEB + links[i]

    return result


def cache_content(title, content):
    digest = hashlib.md5(title.encode('utf-8')).hexdigest()
    with open("./cache/" + digest, "wb") as f:
        f.write(content)


def get_from_cache(title):
    digest = hashlib.md5(title.encode('utf-8')).hexdigest()
    if os.path.exists("./cache/" + digest):
        with open("./cache/" + digest, "rb") as f:
            return f.read()

    return None


def walk(url):
    result = {}

    page_content = get_from_cache(url)
    if page_content is None:
        response = get(url)
        page_content = response.content
        cache_content(url, page_content)

    if is_leafpage(page_content):
        return transliterate_page(page_content)
    else:
        links_dict = scrap_links_intermediate_page(page_content)
        for title, link in links_dict.items():
            print("Walking: ", title)
            result[title] = walk(link)

        return result
