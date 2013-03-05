#!/usr/bin/env python

# :copyright:	2009 - Andrea Grandi
# :author: 	Andrea Grandi
# :contact: 	a.grandi@gmail.com
# :license: 	LGPL
# :version:	0.1

from credit_checker import *
from HTMLParser import HTMLParser

class YoigoES(CreditChecker):
    login_url = 'https://miyoigo.yoigo.com'
    login_check_url = 'https://miyoigo.yoigo.com/selfcare/login'
    mypanel_url = 'https://miyoigo.yoigo.com/balance'

    def __init__(self, username, password):
        super(YoigoES, self).__init__(username, password)
        super(YoigoES, self).cookie_init(self.login_url)
        
    def login(self):
        login_values = {'account_cli':self.username,
                        'password':self.password}
        
        self.post_data(self.login_check_url, login_values)
        
    def get_credit(self):
        res = self.request_page(self.mypanel_url)
        parser = YoigoEsParser()
        data = res.read()
        data = self.__sanitize_page__(data)
        parser.feed(data)
        parser.close()
        return parser.credit
    
    def __sanitize_page__(self, data):
        data = data.replace("'<sc'+'ript'", "'<script")
        data = data.replace("</sc'+'ript>", "</script>")
        return data
    
class YoigoEsParser(HTMLParser):
    credit_flag = 0
    credit = ""
    
    def handle_data(self, data):
        print data.strip()
        
        if(self.credit_flag == 1):
            self.credit_flag = 0
            self.credit = data.strip()
            
        if(data.strip() == 'total_balance'):
            self.credit_flag = 1
