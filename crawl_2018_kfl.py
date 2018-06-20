#!/usr/bin/env python
# -*- coding: utf8 -*-


import sys
import logging
import os
import json
import urllib, urllib2
import time

from BeautifulSoup import BeautifulSoup


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

    ##############################################
    # 2018 k league
    ##############################################

    url_template = "http://www.goal.com/kr/k%EB%A6%AC%EA%B7%B8-%ED%81%B4%EB%9E%98%EC%8B%9D/%EC%9D%BC%EC%A0%95-%EA%B2%B0%EA%B3%BC/%EB%9D%BC%EC%9A%B4%EB%93%9C-" 

    for i in xrange(1, 15):
        logging.debug('crawl: %s round' % i)
        r = str(i)
        url = url_template + r + "/avs3xposm3t9x1x2vzsoxzcbu"
        req = urllib2.Request(url)
        logging.debug('GET request: %s' % req.get_full_url())
        res = urllib2.urlopen(req).read().strip()
        
        soup = BeautifulSoup(res)
        items = soup.findAll('div', attrs={'class': 'match-row  status-pld'})
        for item in items:
            match_data = item.findAll('div', attrs={'class': 'match-data'})[0]
            home_team = match_data.findAll('div', attrs={'itemprop': 'homeTeam'})[0]
            home_score = home_team.findAll('span', attrs={'class': 'goals'})[0].text.strip()
            home_player = home_team.findAll('span', attrs={'class': 'team-name'})[0].text.strip().replace(' ', '')
            away_team = match_data.findAll('div', attrs={'itemprop': 'awayTeam'})[0]
            away_score = away_team.findAll('span', attrs={'class': 'goals'})[0].text.strip()
            away_player = away_team.findAll('span', attrs={'class': 'team-name'})[0].text.strip().replace(' ', '')
            print '\t'.join([r, home_player, home_score, away_score, away_player])

        time.sleep(1)
