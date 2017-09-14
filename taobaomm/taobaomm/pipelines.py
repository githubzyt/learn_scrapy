# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TaobaommPipeline(object):

    def open_spider(self, spider):
        self.file = open('taobaomm.jl', 'w')
        
    def process_item(self, item, spider):
        print item
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()       