# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import codecs
import json


class DoublemoneyPipeline(object):
    def process_item(self, item, spider):
        file_name = './data/'+item['period']+'.json'
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with codecs.open(file_name, "w", encoding="utf-8") as outfile:
            json.dump(dict(item), outfile, ensure_ascii=False)

