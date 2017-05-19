import json
import codecs

class MovieSpiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('movie_info.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == "":
            item['content'] = item['content'][-2]
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
            return item
        else:
            line = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.file.write(line)
            return item

    def spider_closed(self, spider):
        self.file.close()
