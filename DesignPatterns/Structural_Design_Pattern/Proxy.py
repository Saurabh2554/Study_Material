"""
https://medium.com/@kalanamalshan98/proxy-design-pattern-a-comprehensive-guide-73688bbd8e93
https://chatgpt.com/c/68d0d0c1-62d4-832b-8352-37b9d974cdae
"""


"""
Problem Stat: You need to implement a scenario where you block the access of user to any banned sites. First checks whether website is banned or not.
"""

#The proxy design pattern gives us the option to intercept incoming/outgoing request and perform the action required.

from abc import ABC, abstractmethod

class IInternet(ABC):
    @abstractmethod
    def connect_to_sites(site_url:str)->None:pass


class RealInternet(IInternet):
    def connect_to_sites(self,site_url:str)->None:
        print(f"Connected to {site_url}")


#Here insted of calling the RealInternet directly by user we are intercepting the call and then delegating it to the real internet. Also below you will see the concept of lazy object creation.(Often required when you do not want to allow to create object unless it is required)

class ProxyInternet(IInternet):
    banned_sites = ["abc.com", "xyz.com", "banned.com"]

    def __init__(self):
        self.internet = None 

    def connect_to_sites(self,site_url)->None:
        if site_url in ProxyInternet.banned_sites:
            print(f"Url '{site_url}' are not allowed.")
        else :
            self.internet = RealInternet()
            self.internet.connect_to_sites(site_url)   
            
        

if __name__ == "__main__":
    proxy_internet:IInternet = ProxyInternet()
    proxy_internet.connect_to_sites("apple.com")        