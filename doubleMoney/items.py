# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoublemoneyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 开奖日期
    date = scrapy.Field()
    # 期号
    period = scrapy.Field()
    # 中奖号码
    number = scrapy.Field()
    # 奖池
    money = scrapy.Field()
    # 一等奖个数
    first_prize = scrapy.Field()
    # 二等奖个数
    second_prize = scrapy.Field()
