# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import xlsxwriter

class LianjiaPicSpiderPipeline(object):
    def __init__(self, filename, fileds_to_export):
        self.filename = filename #os.path.abspath(filename)
        self.fileds_to_export = fileds_to_export

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            filename = crawler.settings.get('EXCEL_FILENAME'),
            fileds_to_export = crawler.settings.get('FIELDS_TO_EXPORT')
        )

    def append_row(self, item):
        for f in self.fileds_to_export:
            self.active_sheet.write(self.cur_row, self.cur_col, item[f])
            self.cur_col += 1
        
        self.cur_row += 1
        self.cur_col = 0

    def open_spider(self, spider):
        self.workbook = xlsxwriter.Workbook(self.filename)
        self.active_sheet = self.workbook.add_worksheet()
        self.cur_row = 0
        self.cur_col = 0

        for f in self.fileds_to_export:
            self.active_sheet.write(self.cur_row, self.cur_col, f)
            self.cur_col += 1
        
        self.cur_row += 1
        self.cur_col = 0

    def close_spider(self, spider):
        self.workbook.close()

    def process_item(self, item, spider):
        self.append_row(item)
        return item