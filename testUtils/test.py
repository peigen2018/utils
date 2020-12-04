import sys
from nose.tools import nottest, istest
from nose.plugins.attrib import attr

class TestLogin:
#    def __init__(self,userName) -> None:
#       self.userName=userName
    
    #@istest
    @attr(tag='stable')
    def test_login(self):
        
        #print(self.userName +": I'm login")


if __name__ == '__main__':
    
    #loginObj = TestLogin('hello')
    #loginObj.doLogin()
    #print(loginObj.userName)
    pass