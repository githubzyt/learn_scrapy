import scrapy
from taobaomm.items import TaobaommItem

class TaobaommSpider(scrapy.Spider):
    name = "taobaomm"

    start_urls = [
        'http://mm.taobao.com/json/request_top_list.htm',
    ]

    custom_settings = {}

    def parse(self, response):
        for url in response.xpath('//a[contains(@href, "user_id")]'):
            yield TaobaommItem(
                name=url.xpath('text()').extract_first().encode('utf-8'),
                home_page=url.xpath('@href').extract_first()
                )
