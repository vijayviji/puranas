#!/usr/bin/env python
# -*- coding: utf-8 -*-

# logic taken from https://github.com/vlastavesely/sanskrit-iast/
import json

from purana_file_downloader import transliterate_page, scrap_links_intermediate_page, walk

if __name__ == "__main__":
    data = walk(
        "https://sa.wikisource.org/wiki/%E0%A4%85%E0%A4%97%E0%A5%8D%E0%A4%A8%E0%A4%BF%E0%A4%AA%E0%A5%81%E0%A4%B0%E0%A4%BE%E0%A4%A3%E0%A4%AE%E0%A5%8D", 0)
    with open('puranas/agni.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
