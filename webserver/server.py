from logging import raiseExceptions
from flask import Flask, request
from Elasticsearch import ElasticSearch
from ModuleCreator import *

PORT = 8080
DEBUG = True
ELASTIC_HOST = 'http://localhost:9200/'

app = Flask(__name__)

services = {
    'elastic': ElasticSearch(url=ELASTIC_HOST, Golestan=True),
    'boolean': get_boolean(Golestan=True),
    'tfidf': get_tfidf(Golestan=True),
    # 'transformer': get_transformer(Golestan=True),
    # 'fasttext': get_embedding(Golestan=True),
    # 'classification':,
    'clustering': get_clustering(),
    'linkanalysis': get_link_analysis()
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
    try:
        method = request.args.get('method')
        query = request.args.get('query')
        service = services['clustering']

        if method == 'all':
            output = dict()
            clusters = service.get_clusters()
            # print(clusters)
            for i in range(len(clusters)):
                output[f'class{i}'] = list(clusters[i])
        elif method == 'search':
            _, prediction = service.predict_cluster(query)
            output = {'class': list(prediction)}
        else:
            raiseExceptions()
    except Exception as e:
        output = f'Error: {str(e)}'

    return output


@app.route("/linkanalysis", methods=['GET'])
def linkanalysis():
    try:
        method = request.args.get('method')
        n = int(request.args.get('n'))
        service = services['linkanalysis']

        if method == 'hits':
            output = {'authority': service.get_authority_hubs_results(k=n)}
        elif method == 'page rank':
            output = {'nodes': service.get_pagerank_results(k=n)}
        else:
            raiseExceptions()
    except Exception as e:
        output = f'Error: {str(e)}'

    return output


if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
