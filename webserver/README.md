# Server

Here you can find the documentation of our web server and how to deploy it yourself.

---

## How to run server?

### Elastic engine

If you want to use elastic engine you should follow below tutorial to download and run elastic engin. If you don't want elastic you can simply skip this part and go to _Run Server_ part.
<details>
<summary>Install Elastic</summary>
 
To use this service first you need to download and run elastic search engine from [here](https://www.elastic.co/downloads/elasticsearch) (version `7.8.1` is recommended).

For this project we use `parsi` analyzer (thanks to [NarimanN2](https://github.com/NarimanN2/ParsiAnalyzer#build)) for our index so you need to download and add this plugin to your elastic engine. If you have elastic version `7.8.1` you can download it from [here](https://drive.google.com/file/d/1yqCDjcydati3s4BRda4c3kiGXoNGshGU/view?usp=sharing) and follow step 8 of [this](https://github.com/NarimanN2/ParsiAnalyzer#build) link. If you have version `7.13.1` you can use [this](https://github.com/NarimanN2/ParsiAnalyzer#installation) link. If you have another version of elastic engine you need to download and complie the code of this plugin from [here](https://github.com/NarimanN2/ParsiAnalyzer#build) for your own elastic version (note: if you have problem with step 8 in the previous link, just unzip file and copy its content to `{your-elastic-path}/plugins/farsi/`).

</details>

### Run Server
After cloning project, go to _webserver_ directory and follow these steps:

  1. Build a virtual envirement. You can run `python -m venv venv` to do so.
  2. Activate your virtual envirement by running `venv\Scripts\activate\` in your console.
  3. Install all requirements using `pip install -r requirements.txt`.
  4. Download [this](https://www.dropbox.com/s/tlyvnzv1ha9y1kl/spell.zip?dl=0) file and after extraction copy spell\ directory to \venv\Lib\site-packages\parsivar\resource\.
  5. All done! Now you can run server by running `python server.py`. If you want to run server with elastic engin, run `python server.py --e`.

Your server will be up on port `8080`. You can change this by changing `PORT` variable in _server.py_ file.

---

## Documentation

We have different classes which you can find out how to use them below:

- Elasticsearch.py
- Boolean.py
- TFIDF.py
- Clustering.py
- LinkAnalysis.py

### Elasticsearch.py
On initialization, this module will build an index with name 'saadi-ir' on elastic cluster and index poems to it. Then you will be able to search for your poem.

```python
from Elasticsearch import ElasticSearch

es = ElasticSearch(url='http://localhost:9200')
es.search('باید اول به تو گفتن که چنین خوب چرایی')
```

### Boolean.py

On initialization, this module creates a boolean matrix with Boostan Beits.
  You can add Golestan data and/or make each datapoint the whole Beits of one poem with `__init__` arguments.  

- get_vectors: returns Boolean Matrix of its instance
- search: returns k most similar datapoints to query (Boolean Retreival)


### TFIDF.py  

On initialization, this module creates a tf-idf matrix with Boostan Beits using TfidfVectorizer.
  You can add Golestan data and/or make each datapoint whole Beits of one poem with `__init__` arguments.  

- get_vectors: returns tf-idf Matrix of its data
- search: returns k most similar datapoints to query based on cos of their angle (TF-IDF Retreival)


### Clustering.py

Initializes a K-means module and clusters Boostan Beits based into 11 clusters (assuming to be close to their Babs).
  It can be done on whole poems by setting poem_based=True.

- get_clusters: returns a dictionary of 11 classes and poems in each.
- predict_cluster: returns the closest cluster and poems in it to the query.


### LinkAnalysis.py

creates an adjacency matrix from Boostan Beits and runs Pagerank and HITS algorithms on it.

- get_pagerank_results: return k most important Beits of Boostan based on Pagerank algorithm.
- get_authority_hubs_results: return k most important Beits of Boostan based on HITS algorithm.
