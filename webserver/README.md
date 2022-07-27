# Server

Here you can find the documentation of our web server and how to deploy it yourself.

We have different classes which you can find out how to use them below:

- Elasticsearch.py
- Boolean.py
- TFIDF.py
- Clustering.py
- LinkAnalysis.py

---

### Elasticsearch.py

To use this service first you need to download and run elastic search engine from [here](https://www.elastic.co/downloads/elasticsearch) (version `7.8.1` is recommended).

For this project we use `parsi` analyzer (thanks to [NarimanN2](https://github.com/NarimanN2/ParsiAnalyzer#build)) for our index so you need to download and add this plugin to your elastic engine. If you have elastic version `7.8.1` you can download it from [here](https://drive.google.com/file/d/1yqCDjcydati3s4BRda4c3kiGXoNGshGU/view?usp=sharing) and follow step 8 of [this](https://github.com/NarimanN2/ParsiAnalyzer#build) link. If you have version `7.13.1` you can use [this](https://github.com/NarimanN2/ParsiAnalyzer#installation) link. If you have another version of elastic engine you need to download and complie the code of this plugin from [here](https://github.com/NarimanN2/ParsiAnalyzer#build) for your own elastic version (note: if you have problem with step 8 in the previous link, just unzip file and copy its content to `{your-elastic-path}/plugins/farsi/`).

---

### Boolean.py

On initialization, this module creates a boolean matrix with Boostan Beits.
  You can add Golestan data and/or make each datapoint the whole Beits of one poem with `__init__` arguments.  

- get_vectors: returns Boolean Matrix of its instance
- search: returns k most similar datapoints to query (Boolean Retreival)

---

### TFIDF.py  

On initialization, this module creates a tf-idf matrix with Boostan Beits using TfidfVectorizer.
  You can add Golestan data and/or make each datapoint whole Beits of one poem with `__init__` arguments.  

- get_vectors: returns tf-idf Matrix of its data
- search: returns k most similar datapoints to query based on cos of their angle (TF-IDF Retreival)

---

### Clustering.py

Initializes a K-means module and clusters Boostan Beits based into 11 clusters (assuming to be close to their Babs).
  It can be done on whole poems by setting poem_based=True.

- get_clusters: returns a dictionary of 11 classes and poems in each.
- predict_cluster: returns the closest cluster and poems in it to the query.

---

### LinkAnalysis.py

creates an adjacency matrix from Boostan Beits and runs Pagerank and HITS algorithms on it.

- get_pagerank_results: return k most important Beits of Boostan based on Pagerank algorithm.
- get_authority_hubs_results: return k most important Beits of Boostan based on HITS algorithm.
