#importing requests
import requests
from requests import HTTPError
#using API

#class for communicating with API
class Currency:
    #initializaing all required attributes
    def __init__(self,amount,frm,frmto):
        #got from call 'Funtion'
        self.frm = frm
        self.to = frmto
        self.a = amount
        #attribues for API
        self.api = open("api_key").readline().strip()
        self.url = f"https://v6.exchangerate-api.com/v6/{self.api}/pair/{self.frm}/{self.to}/{self.a}"
    #method for sending request to API
    def check(self):
        try:
            self.response = requests.get(self.url)
            #self.status = self.response.status_code
        except:
            raise HTTPError(">>poor_connecton<<")
    #method for printing the result 
    def prnt(self):
        self.result = self.response.json()
        #storing the usage data of API
        with open("api_history.txt",'a') as f:
            f.write(str(self.result))
            f.write("done1\n")
        #printing Result
        print(f'\nconverted to {self.to} : ',str(round(self.result['conversion_result'],2)))
#end
