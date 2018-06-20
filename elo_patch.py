#!/usr/bin/env python
# -*- coding: utf8 -*-


import sys
import logging


def initDefaultEncoding():
    '''Set default system encoding as utf8'''
    reload(sys)
    sys.setdefaultencoding('utf8')


def initLogger():
    '''Initialize logger'''
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)


def expect_prob(A, B):
    """
    Calculate expected score of A in a match against B
    :param A: Elo rating for player A
    :param B: Elo rating for player B
    """
    return 1 / (1 + 10 ** ((B - A) / 400))


def rate(old, exp, score, k=32):
    """
    Calculate the new Elo rating for a player
    :param old: The previous Elo rating
    :param exp: The expected score for this match
    :param score: The actual score for this match
    :param k: The k-factor for Elo (default: 32)
    """
    return old + k * (score - exp)
    

if __name__ == "__main__":

    initDefaultEncoding()
    initLogger()
    
