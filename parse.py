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
    

if __name__ == "__main__":

    initDefaultEncoding()
    initLogger()
    
    with open(sys.argv[1]) as f:
        lines = [x.strip() for x in f.read().strip().split('')]
        
