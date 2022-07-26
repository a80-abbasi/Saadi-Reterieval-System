import json
import requests


class ElasticSearch:
    def __init__(self, url):
        self.base_url = url
        self.headers = {'Content-type': 'application/json'}

    def check_exists(self, index_name):
        code = requests.head(url=self.base_url + index_name).status_code
        if code != 200:
            return False
        return True

    def delete_index(self, index_name):
        if self.check_exists(index_name):
            code = requests.delete(url=self.base_url + index_name).status_code
            if code != 200:
                print('something wrong happend!')
            else:
                print(f'index \"{index_name}\" deleted successfully.')
        else:
            print(f'index \"{index_name}\" does not exists!')

    def _make_mapping(self):
        mapping = {
            "mappings": {
                "properties": {
                    "content": {
                        "type": "text",
                        "analyzer": "parsi_standard"
                    }
                }
            }
        }

        return json.dumps(mapping)

    def create_index(self, index_name):
        if self.check_exists(index_name):
            print(f'index {index_name} already exists!')
        else:
            data = self._make_mapping()
            code = requests.put(url=self.base_url + index_name,
                                data=data, headers=self.headers).status_code
            if code != 200:
                print('something wrong happend!')
            else:
                print(f'index \"{index_name}\" created successfully.')

    def search(self, query, index_name, size=5):
        q = {
            "query": {
                "match": {
                    "content": f'\"{query}\"'
                }
            },
            "size": size
        }
        q = json.dumps(q)

        response = requests.get(
            url=self.base_url + index_name + '/_search', data=q, headers=self.headers)
        body = json.loads(response.content)

        results = []
        for out in body['hits']['hits']:
            res = out['_source']
            res['score'] = out['_score']
            results.append(res)

        return results

    def _ready_for_bulk(self, docs, index_name):
        array = []
        for d in docs:
            array.append({'index': {'_index': index_name}})
            array.append(d)
        return array

    def _make_docs(self, docs):
        temp = '['
        for d in docs:
            temp += '{\"content\":' + f'\"{d}\"' + '},'
        temp = temp[:-1] + ']'
        return json.loads(temp, strict=False)

    def bulk(self, docs, index_name):
        docs = self._make_docs(docs)
        array = self._ready_for_bulk(docs, index_name)

        data = ''
        for e in array:
            data += json.dumps(e) + '\n'

        response = requests.post(
            url=self.base_url + index_name + '/_bulk', data=data, headers=self.headers)
        if response.status_code == 200:
            print('bulk was successfull.')
        else:
            print('something wrong happened!')
