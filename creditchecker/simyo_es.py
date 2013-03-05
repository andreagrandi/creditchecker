#!/usr/bin/env python

# :copyright:	2009 - Andrea Grandi
# :author: 	Andrea Grandi
# :contact: 	a.grandi@gmail.com
# :license: 	LGPL
# :version:	0.1

from credit_checker import *
from HTMLParser import HTMLParser

class SimyoES(CreditChecker):
    login_url = 'https://www.simyo.es/simyo/portal/action/login'
    login_check_url = 'https://www.simyo.es/simyo/portal/j_security_check'
    mypanel_url = 'https://www.simyo.es/simyo/portal/customer/action/my-panel'
    
    def __init__(self, username, password):
        super(SimyoES, self).__init__(username, password)
        super(SimyoES, self).cookie_init(self.login_url)
        
    def login(self):
        login_values = {'j_username':self.username,
                        'j_password':self.password}
        
        self.post_data(self.login_check_url, login_values)
        
    def get_credit(self):
        res = self.request_page(self.mypanel_url)
        parser = SimyoEsParser()
        data = res.read()
        data = self.__sanitize_page__(data)
        parser.feed(data)
        parser.close()
        return parser.credit
    
    def __sanitize_page__(self, data):
        data = data.replace("'<sc'+'ript'", "'<script")
        data = data.replace("</sc'+'ript>", "</script>")
        return data
    
class SimyoEsParser(HTMLParser):
    credit_flag = 0
    credit = ""
    
    def handle_data(self, data):
        if(self.credit_flag == 1):
            self.credit_flag = 0
            self.credit = data.strip()
            
        if(data.strip() == 'Saldo disponible'):
            self.credit_flag = 1
