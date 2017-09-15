import scrapy
from ..items import TaobaommItem
from bs4 import BeautifulSoup
from scrapy_splash import SplashRequest


class TaobaommSpider(scrapy.Spider):
    name = "taobaomm"

    # start_urls = [
    #     'http://mm.taobao.com/json/request_top_list.htm',
    # ]

    custom_settings = {}

    def start_requests(self):
        yield scrapy.Request('http://mm.taobao.com/json/request_top_list.htm', self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        mm_list = []
        for info_blk in soup.find_all('div', class_='personal-info'):
            name_blk = info_blk.find('a', 'lady-name')
            mm_name = name_blk.string
            mm_home_page = 'http:'+name_blk['href']
            age_blk = name_blk.find_next_sibling()
            age = age_blk.get_text()
            location = age_blk.find_next_sibling().get_text()
            user_id = mm_home_page.split('user_id=')[1]
            mm =TaobaommItem(name=mm_name, home_page=mm_home_page, age=age, location=location,
                user_id=user_id)
            mm_list.append(mm)
            yield mm

        # for mm in mm_list:
        #     r=SplashRequest(mm['home_page'], self.parse_hg, endpoint='render.html',
        #      args={'user_id': mm['user_id']})
        #     r.meta['mm'] = mm
        #     yield r
        # for mm in mm_list:
        #     r=SplashRequest('https://www.baidu.com', self.parse_hg, endpoint='render.html',
        #      args={'user_id': mm['user_id']})
        #     r.meta['mm'] = mm
        #     yield r

    def parse_hg(self,response):
        self.logger.info('start scrapy home page: %s' %response.url)
        self.logger.info('mm info is %s' %response.meta['mm'])
        # for img in response.xpath('//img/@href'):
        #     yield {'img': img}