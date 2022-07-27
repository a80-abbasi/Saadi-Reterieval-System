# Saadi1401-5_23

1401/Spring/InformationRetrieval/g5+23  
***************
* Mohammad Javad Hezareh: 98101074
* Ali Abbasi: 98105879
* Matin Shoja: 
* Maziar Shamsipour:
* Yasin Moosavi:
* Amir Ali Ebrahimzadeh:
***************

* **Boolean.py**  
On initialization, this module creates a boolean matrix with Boostan Beits.
  You can add Golestan data and/or make each datapoint the whole Beits of one poem with `__init__` arguments.  
  * get_vectors: returns Boolean Matrix of its instance
  * search: returns k most similar datapoints to query (Boolean Retreival)
    
* **TFIDF.py**  
On initialization, this module creates a tf-idf matrix with Boostan Beits using TfidfVectorizer.
  You can add Golestan data and/or make each datapoint whole Beits of one poem with `__init__` arguments.  
  * get_vectors: returns tf-idf Matrix of its data
  * search: returns k most similar datapoints to query based on cos of their angle (TF-IDF Retreival)

* **Clustering.py**  
Initializes a K-means module and clusters Boostan Beits based into 11 clusters (assuming to be close to their Babs). 
  It can be done on whole poems by setting poem_based=True. 
  * get_clusters: returns a dictionary of 11 classes and poems in each.
  * predict_cluster: returns the closest cluster and poems in it to the query.
    
* **LinkAnalysis.py**  
creates an adjacency matrix from Boostan Beits and runs Pagerank and HITS algorithms on it.
  * get_pagerank_results: return k most important Beits of Boostan based on Pagerank algorithm.
  * get_authority_hubs_results: return k most important Beits of Boostan based on HITS algorithm.