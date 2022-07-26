from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from PreProcess import sent_pre_process
from sklearn.metrics import classification_report
from Utils import boostan_data


class Classification:

    def __init__(self):
        self.vectorizer = TfidfVectorizer(strip_accents='unicode',
                                          analyzer='char',
                                          preprocessor=self._preprocessor,
                                          ngram_range=(2, 6),
                                          min_df=4,
                                          max_features=15000)
        self.data = boostan_data
        self.X_train = boostan_data['poem']
        self.y_train = boostan_data['chapter']
        self.classifier = LinearSVC(class_weight='balanced')
        self.fit(self.X_train, self.y_train)

    def _preprocessor(self, x):
        return ' '.join(sent_pre_process(x, normalize=False, remove_stopwords=True, lemmatize=False))

    def search(self, query, k):
        return self.classifier.predict(self.vectorizer.transform(query))

    def fit(self, X_train, y_train):
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        self.classifier.fit(X_train_tfidf, y_train)

    def evaluation(self, X_test, y_test):
        return classification_report(y_test, self.predict(X_test), output_dict=True)
