from flask import Flask, request
from Elasticsearch import ElasticSearch
from Boolean import Boolean
from TFIDF import TFIDF

PORT = 8080
DEBUG = True

app = Flask(__name__)

services = {
    'elastic': ElasticSearch(url='http://localhost:9200/', index_name='ir-saadi'),
    'boolean': Boolean(),
    'tfidf': TFIDF(),
    # 'transformer':
    # 'fasttext':
    # 'classification':
}


@app.route("/search", methods=['GET'])
def search():
    try:
        method = request.args.get('method')
        query = request.args.get('query')
        n = int(request.args.get('n'))

        result = services[method].search(query=query, k=n)
        output = {
            'result': list(result)
        }
    except Exception as e:
        output = f'Error: {str(e)}'

    return output


@app.route("/clustering", methods=['GET'])
def clustering():
    pass


@app.route("/linkanalysis", methods=['GET'])
def linkanalysis():
    pass


if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
