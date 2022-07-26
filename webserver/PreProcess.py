from hazm import *
from webserver.Utils import punctuations
from webserver.Utils import replace_dict
from webserver.Utils import stopwords

normalizer = Normalizer()
stemmer = Stemmer()
lemmatizer = Lemmatizer()


def replace_function(string):
    if string in replace_dict:
        return replace_dict[string]
    return string


def sent_pre_process(sentence, normalize=True, remove_stopwords=False, stemme=False, lemmatize=True, replace=True,
                     remove_punctuations=True, is_first=True):
    # replace some charachters
    replace_char = {'هٔ': 'ه',
                    'ۀ': 'ه',
                    'ه‌ی': 'ه'}

    if remove_punctuations:
        for char in punctuations:
            replace_char[char] = " "

    for key, value in replace_char.items():
        sentence = sentence.replace(key, value)

    if normalize:
        sentence = normalizer.normalize(sentence)
    if stemme:
        sentence = stemmer.stemme(sentence)
    if lemmatize:
        sentence = lemmatizer.lemmatize(sentence)

    tokens = word_tokenize(sentence)

    if replace:
        tokens = [replace_function(token) for token in tokens]
    if remove_stopwords:
        tokens = [token for token in tokens if token not in stopwords]

    if is_first:
        return sent_pre_process(" ".join(tokens), normalize, remove_stopwords, stemme, lemmatize, replace,
                                remove_punctuations, False)

    return tokens


def pre_process(sentences, normalize=True, remove_stopwords=False, stemme=False, lemmatize=True, replace=True,
                remove_punctuations=True, is_first=True, MIN_COUNT=3, put_index=False):
    if put_index:
        processed = [(sent_pre_process(sent, normalize, remove_stopwords, stemme, lemmatize, replace,
                                       remove_punctuations, is_first), i) for i, sent in enumerate(sentences)]
        return [t for t in processed if len(list(t[0])) > MIN_COUNT]
    processed = [
        sent_pre_process(sent, normalize, remove_stopwords, stemme, lemmatize, replace, remove_punctuations, is_first)
        for sent in sentences]
    return [t for t in processed if len(list(t)) > MIN_COUNT]


def bi_sent_pre_process(sentence, normalize=True, remove_stopwords=False, stemme=False, lemmatize=True, replace=True,
                        remove_punctuations=True, is_first=True):
    tokens = sent_pre_process(sentence, normalize, remove_stopwords, stemme, lemmatize, replace, remove_punctuations,
                              is_first)
    y = []
    for i in range(len(tokens) - 1):
        y.append(f'{tokens[i]} {tokens[i + 1]}')
    return y

