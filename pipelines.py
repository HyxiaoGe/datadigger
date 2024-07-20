import json
from utils.date_utils import format_date


class DatadiggerPipeline:
    def __init__(self):
        self.items = []

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        with open(f'{spider.name}_items.json', 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)

    def process_item(self, item, spider):
        if 'date' in item and item['date']:
            item['date'] = format_date(item['date'])
        self.items.append(dict(item))
        return item
