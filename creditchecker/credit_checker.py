#!/usr/bin/env python

# :copyright:	2009 - Andrea Grandi
# :author: 	Andrea Grandi
# :contact: 	a.grandi@gmail.com
# :license: 	LGPL
# :version:	0.1

import urllib2
from urllib import urlencode

class CreditChecker(object):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    username = ""
    password = ""
    credit = ""
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def cookie_init(self, url):
        req = urllib2.Request(url)
        self.cookie_response = self.opener.open(req)
        
    def post_data(self, url, values):
        data = urlencode(values)
        req = urllib2.Request(url, data)
        response = self.opener.open(req)
        return response
    
    def request_page(self, url):
        req = urllib2.Request(url)
        response = self.opener.open(req)
        return response
    
    def login(self):
        pass 
    
    def get_credit():
        pass
