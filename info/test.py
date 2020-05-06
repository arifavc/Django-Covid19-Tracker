import json
import requests
import schedule 




class Covid():

    def __init__(self,name,url):
        self.name = name
        self.url = url
        self.endpoint = f'https://corona-api.com/' 



    def convert(self):            
        try:      
            with open('ulkeler.json' ,encoding="utf8") as f:
                data = json.load(f)  
            for code, country_name in data.items():
                if country_name.lower() == self.name.lower():
                    return code    
        except Exception:
            print("Convert fonksiyonu düzgün çalışmadı..")


    def fetch(self):
        try:    
            response = requests.get(self.url)
            if response.status == "200":   
                response = response.json()
                return response
            else:
                print('Veri çekilemedi..')
        except Exception:
            print('fetch fonksiyonu düzgün çalışmadı')



class World(Covid):
    endpoint = f'https://corona-api.com/' 
    timeline = "12"
        


    

class Country(Covid):
    def __init__(self,name):
        self.name = name
         

        #  to-do


        











