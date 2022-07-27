from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from PreProcess import sent_pre_process
from sklearn.metrics import classification_report
from Utils import boostan_data

Boostan_Babs = [
    'در نیایش خداوند',
    'باب اول در عدل و تدبیر و رای',
    'باب دوم در احسان',
    'باب سوم در عشق و مستی و شور',
    'باب چهارم در تواضع',
    'باب پنجم در رضا',
    'باب ششم در قناعت',
    'باب هفتم در عالم تربیت',
    'باب هشتم در شکر بر عافیت',
    'باب نهم در توبه و راه صواب',
    'باب دهم در مناجات و ختم کتاب'
]


class Classification:

    def __init__(self, classifier=None, voctorizer=None):
        self.vectorizer = voctorizer if voctorizer else TfidfVectorizer(strip_accents='unicode',
                                                                        analyzer='char',
                                                                        preprocessor=self._preprocessor,
                                                                        ngram_range=(2, 6),
                                                                        min_df=4,
                                                                        max_features=15000)
        self.data = boostan_data
        self.X_train = boostan_data['poem']
        self.y_train = boostan_data['chapter']
        self.classifier = classifier if classifier else LinearSVC(class_weight='balanced')
        self.fit(self.X_train, self.y_train)

    def _preprocessor(self, x):
        return ' '.join(sent_pre_process(x, normalize=False, remove_stopwords=True, lemmatize=False))

    def search(self, query, k=1):
        i = self.classifier.predict(self.vectorizer.transform([query]))[0]
        return [int(i), Boostan_Babs[i]]

    def fit(self, X_train, y_train):
        X_train_tfidf = self.vectorizer.fit_transform(X_train)
        self.classifier.fit(X_train_tfidf, y_train)

    def evaluation(self, X_test, y_test):
        y_pred = self.classifier.predict(self.vectorizer.transform(X_test))
        return classification_report(y_test, y_pred, output_dict=True)
