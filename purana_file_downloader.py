# -*- coding: utf-8 -*-
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


def is_leafpage(html_content):
    tree = html.fromstring(html_content)
    content = tree.xpath('//div[@class="poem"]/p/text()')
    if len(content) == 0:
        return False

    return True


def parse_content(html_content):
    tree = html.fromstring(html_content)
    content = tree.xpath('//div[@class="poem"]/p/text()')
    return content


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


def walk(url, level):
    result = {}
    response = get(url)
    if is_leafpage(response.content):
        return transliterate_page(response.content)
    else:
        links_dict = scrap_links_intermediate_page(response.content)
        for title, link in links_dict.items():
            print("Walking: ", title)
            result[title] = walk(link, level+1)

        return result
