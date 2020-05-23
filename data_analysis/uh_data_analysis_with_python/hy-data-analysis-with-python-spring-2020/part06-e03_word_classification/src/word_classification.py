#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    # a has the owrds 1D np array
    vectorizer = CountVectorizer(token_pattern=r"(?u)\w|-", analyzer='char', vocabulary=alphabet_set)
    vectorized = vectorizer.transform(a).toarray()
    return np.hstack((vectorized[:, 1:], vectorized[:, 0].reshape(-1, 1)))

def contains_valid_chars(s):
    '''
        Checks if the given character is in the alphabet
    '''
    for i in s:
        if i not in alphabet:
            return False
    return True

def filter_words(words, test=True):
    if test:
        all_words_lower_case = [word.lower() for word in words]
    else:
        all_words_lower_case = [word.lower() for word in words if word[0].islower()]
    allowed_words = [word for word in all_words_lower_case if contains_valid_chars(word)]
    return allowed_words

def get_features_and_labels():
    features, labels = None, None
    finnish_allowed_words = filter_words(load_finnish())
    english_allowed_words = filter_words(list(load_english()), False)
    # features and target
    fi_features = get_features(finnish_allowed_words)
    fi_targets = np.zeros((len(finnish_allowed_words), 1))
    en_features = get_features(english_allowed_words)
    en_targets = np.ones((len(english_allowed_words), 1))
    return np.concatenate((fi_features, en_features)), np.concatenate((fi_targets, en_targets))


def word_classification():
    X, y = get_features_and_labels()
    model = MultinomialNB()
    kfold = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    return cross_val_score(model, X, np.ravel(y), cv=kfold)


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
