from flask import Flask, request
from webserver.Elasticsearch import ElasticSearch
from webserver.Boolean import Boolean
from webserver.TFIDF import TFIDF

PORT = 8080
DEBUG = True

app = Flask(__name__)

services = {
    'elastic': ElasticSearch(),
    'boolean': Boolean(),
    'tfidf': TFIDF(),
    # 'transformer':
    # 'fasttext':
    # 'classification':
}


@app.route("/search", methods=['GET'])
def search():
    # data = request.get_json()
    method = request.args.get('method')
    query = request.args.get('query')
    n = request.args.get('n')

    result = services[method].search(query=query, k=n)
    output = {
        'result': result
    }

    return output


@app.route("/clustering", methods=['GET'])
def clustering():
    pass


@app.route("/linkanalysis", methods=['GET'])
def linkanalysis():
    pass


if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
