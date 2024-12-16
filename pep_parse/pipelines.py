import csv
from datetime import datetime

from pep_parse.settings import BASE_DIR, DATA


class PepParsePipeline:
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        DATA[item['status']] = DATA.setdefault(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        filename = (
            f'{BASE_DIR}/results/status_summary_'
            f'{datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S")}.csv'
        )
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            writer = csv.writer(f, dialect='unix')
            writer.writerows(DATA.items())
            f.write(f'Total,{sum(DATA.values())}\n')
