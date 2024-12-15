from pep_parse.constants import data, filename


class PepParsePipeline:
    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        if item['status'] in data:
            data[item['status']] += 1
        else:
            data.setdefault(item['status'], 1)
        data['total'] += 1
        return item

    def close_spider(self, spider):
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in data.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{data["total"]}\n')
