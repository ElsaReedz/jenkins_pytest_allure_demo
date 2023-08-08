import os
import yaml

class YamlUtil:

    def read_extract_yaml(self, key):
        with open(os.getcwd() + "./extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    def write_extract_yaml(self, data):
        with open(os.getcwd() + "./extract.yml", mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)# 允许使用unicode编码

    def clear_extract_yaml(self):
        with open(os.getcwd() + "./extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()
