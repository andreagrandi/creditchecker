#!/usr/bin/env python

# :copyright:	2009-2010 Andrea Grandi
# :author: 	Andrea Grandi
# :contact: 	a.grandi@gmail.com
# :license: 	LGPL
# :version:	0.1

from credit_checker import *
from BeautifulSoup import BeautifulSoup

class TreIT(CreditChecker):
    # this page should give the cookie and initialize session
    login_url = 'http://areaclienti.tre.it/selfcare/areaclienti133/4552_infoCosti_ITA_LOGGED.xsl'
    
    # this must be the FORM POST result page
    login_check_url = 'http://areaclienti.tre.it/selfcare/login'
    
    # the page that must be checked for data
    mypanel_url = 'http://areaclienti.tre.it/selfcare/areaclienti133/4552_infoCosti_ITA_HTML.xsl'
    
    # page containing informations about Internet data traffic
    soglie_url = 'http://areaclienti.tre.it/selfcare/areaclienti133/4552_soglie_ITA_LOGGED.xsl'
    
    def __init__(self, username, password):
        super(TreIT, self).__init__(username, password)
        super(TreIT, self).cookie_init(self.login_url)
        
    def login(self):
        login_values = {'username':self.username,
                        'password':self.password,
                        'proposition':'consumer'}
        
        self.post_data(self.login_check_url, login_values)
        
    def get_credit(self):
        credit = 0        
        res = self.request_page(self.mypanel_url)
        data = res.read()
        soup = BeautifulSoup(data)
        l = soup.findAll('b')
        temp_credit = "".join(l[1])
        temp_credit = temp_credit.replace("<b>", "")
        credit = temp_credit.replace("&euro;", "")
        return credit
    
    def get_naviga3_info(self):
        info = Naviga3Info()
        
        res = self.request_page(self.soglie_url)
        data = res.read()
        
        soup = BeautifulSoup(data)
        t = soup.findAll('table')
        mb = t[13].findAll('td')             # table where Naviga3 data is located
        
        traffic_done = "".join(mb[1])
        info.traffic_done = traffic_done.replace(" MB&nbsp;&nbsp;", "")
        
        traffic_remaining = "".join(mb[2])
        info.traffic_remaining = traffic_remaining.replace(" MB&nbsp;&nbsp;", "")
        
        traffic_total = "".join(mb[3])
        info.traffic_total = traffic_total.replace(" MB&nbsp;&nbsp;", "")
        
        return info
    
class Naviga3Info():
    traffic_done = 0
    traffic_remaining = 0
    traffic_total = 0

    def __init__(self):
        pass
