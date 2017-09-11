import scrapy


class QuotesSpider(scrapy.Spider):
    name = "taobaomm"

    def start_requests(self):
        urls = [
            'http://mm.taobao.com/json/request_top_list.htm',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)