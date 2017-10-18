#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from search.models import OpenVector
from numpy import array, math, linalg


def get_unknown_word(word):
    word = word.lower()
    try:
        r = requests.get("http://api.openmeaning.org/vectors/" + word + "/")
        if r.status_code == 200:
            openvector = OpenVector()
            openvector.word = word
            openvector.vector = r.json()['vector']
            openvector.save()
            return openvector
        return False
    except Exception:
        return False


def normalise(v):
    norm = linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def query_distribution(query):
    if not query:
        return None
    words = query.rstrip('\n').split()
    # Only retain arguments which are in the distributional semantic space
    vecs_to_add = []
    for word in words:
        word_vec = OpenVector.objects.filter(word=word).first()
        if not word_vec:
            word_vec = get_unknown_word(word)
        if word_vec:
            vecs_to_add.append(word_vec)
    vbase = array([])
    # Add vectors together
    vbase = array([float(i) for i in vecs_to_add[0].vector.split(',')])
    for vec in vecs_to_add[1:]:
        if vec.entropy and math.log(vec.entropy.entropy + 1) > 0:
            weight = float(1) / float(math.log(vec.entropy.entropy + 1))
            vbase = vbase + weight * array([float(i) for i in vec.vector.split(',')])
        else:
            vbase = vbase + array([float(i) for i in vec.vector.split(',')])
    vbase = normalise(vbase)
    return vbase
