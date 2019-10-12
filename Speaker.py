# -*- coding:utf-8 -*-

import pyttsx3
import feedparser
import json


def speaker(list):
    engine = pyttsx3.init()
    for item in list:
        engine.say(item)
    engine.runAndWait()


def rssParser(url):
    page_dict = feedparser.parse(url)
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(page_dict, f, ensure_ascii=False, indent=4)
    something = [page_dict.feed.title]
    for content in page_dict.entries:
        something.append(content.title)
    print(something)
    return something


if __name__ == '__main__':
    talklist = rssParser("https://www.douban.com/feed/review/book")
    speaker(talklist)

