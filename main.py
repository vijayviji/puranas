#!/usr/bin/env python
# -*- coding: utf-8 -*-

# logic taken from https://github.com/vlastavesely/sanskrit-iast/
import json

from purana_file_downloader import transliterate_page, scrap_links_intermediate_page, walk

if __name__ == "__main__":
    data = walk(
        "https://sa.wikisource.org/wiki/%E0%A4%B5%E0%A4%BE%E0%A4%AE%E0%A4%A8%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D/%E0%A4%B7%E0%A4%A1%E0%A5%8D%E0%A4%B5%E0%A4%BF%E0%A4%82%E0%A4%B6%E0%A4%A4%E0%A4%BF%E0%A4%A4%E0%A4%AE%E0%A5%8B%E0%A4%BD%E0%A4%A7%E0%A5%8D%E0%A4%AF%E0%A4%BE%E0%A4%AF%E0%A4%83")
    with open('puranas/naother.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
