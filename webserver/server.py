import os
import argparse
from logging import raiseExceptions
from flask import Flask, request
from Elasticsearch import ElasticSearch
from ModuleCreator import *
from TFIDF import get_tfidf


# constants
PORT = 8080
DEBUG = True
ELASTIC_HOST = 'http://localhost:9200/'

# web server app
app = Flask(__name__)

# build a directory to save files
path = '../resources/saved-models/'
if not os.path.exists(path):
    os.makedirs(path)

# input arguments
parser = argparse.ArgumentParser()
parser.add_argument("--e", action="store_true")
args = parser.parse_args()
elastic = args.e

# services of the web server
services = {
    'boolean': get_boolean(Golestan=True),
    'tfidf': get_tfidf(Golestan=True),
    'transformer': get_transformer(Golestan=True),
    'fasttext': get_embedding(Golestan=True),
    'classification': get_classification(),

    'clustering': get_clustering(),
    'linkanalysis': get_link_analysis(),
    'expansion': get_query_expansion()
}
if elastic:
    services['elastic'] = ElasticSearch(url=ELASTIC_HOST, Golestan=True)

print('service initialization done!')


#####################################
#   below are provided URLs         #
#####################################
@app.route("/search", methods=['GET'])
def search():
    try:
        method = request.args.get('method')
        query = request.args.get('query')
        if request.args.get('n'):
            n = int(request.args.get('n'))
        else:
            n = 0

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
            output = 'Error: method must be one of \"hits\" or \"page rank\"'
    except Exception as e:
        output = f'Error: {str(e)}'

    return output


@app.route("/expansion", methods=['GET'])
def query_expansion():
    try:
        query = request.args.get('query')
        service = services['expansion']

        correct = service.correct_spell_error(query)
        next_word = service.suggest(correct)

        output = {"result": f'{correct} {next_word}'}
    except Exception as e:
        output = f'Error: {str(e)}'

    return output


@app.route("/classification", methods=['GET'])
def classification():
    return 'under developement!'


if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG)
