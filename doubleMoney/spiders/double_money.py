import scrapy
import string
from doubleMoney.items import DoublemoneyItem


class DoubleMoneySpider(scrapy.Spider):
    name = "doubleMoney"
    start_urls = ["http://kaijiang.zhcw.com/zhcw/html/ssq/list_1.html"]

    def parse(self, response):
        base_url = "http://kaijiang.zhcw.com/zhcw/html/ssq/list_"
        last_tr = response.xpath('//table//tr')[-1]
        amount = last_tr.xpath("td[1]//p[2]//strong//text()").extract()[0]
        for i in range(1, int(amount)+1):
            url = base_url+str(i)+".html"
            print(url)
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):
        tr_values = response.xpath('//table//tr')
        for value in tr_values[2:]:
            date = value.xpath('td[1]//text()').extract_first()
            if date.strip() != '':
                item = DoublemoneyItem()
                period = value.xpath('td[2]//text()').extract_first()
                number = value.xpath('td[3]//em//text()').extract()
                money = value.xpath('td[4]//strong//text()').extract_first()
                first_prize = value.xpath('td[5]//strong//text()').extract_first()
                second_prize = value.xpath('td[6]//strong//text()').extract_first()
                item['date'] = date
                item['period'] = period
                item['number'] = number
                item['money'] = money
                item['first_prize'] = first_prize
                item['second_prize'] = second_prize
                yield item

