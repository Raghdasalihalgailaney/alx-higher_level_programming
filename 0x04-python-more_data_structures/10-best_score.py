#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxval = 0
    maxkey = None
    for K, V in a_dictionary.items():
        if V > maxval:
            maxval = V
            maxkey = K
            return maxkey
