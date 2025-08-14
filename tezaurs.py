import requests
from typing import Dict, List, Optional, Literal
import xmltodict

class Tezaurs:
#    def __init__(self, word: str):
#        self.word = word

    def analyze(self, word: str) -> List[Dict]:
        url = f'http://api.tezaurs.lv:8182/analyze/{word}'
        response = requests.get(url)
        return response.json()
    
    def analyze_sentence(self, sentence: str) -> List[Dict]:
        sentence.strip("%20")
        url = f'http://api.tezaurs.lv:8182/analyzesentence/{sentence}'
        print(url)
        response = requests.get(url)
        return response.json()
    
    def inflect(self, word: str, format:str = 'json') -> List[Dict]:
        url = f'http://api.tezaurs.lv:8182/inflect/{format}/{word}'
        response = requests.get(url)
        if(format == 'xml'):
            result = xmltodict.parse(response.text)  
        else:
            return response.json()
        return result
    
    def inflect_phrase(self, phrase: str, category: Optional[Literal['person', 'org', 'loc']] = None) -> List[Dict]:
        phrase.strip("%20") 
        url = f'http://api.tezaurs.lv:8182/inflect_phrase/{phrase}'
        if category is not None:
            url += f"?category={category}"
        response = requests.get(url)
        return response.json()
    
    def inflections(self, word: str) -> List[Dict]:
        url = f'http://api.tezaurs.lv:8182/v1/inflections/{word}'
        response = requests.get(url)
        return response.json()

    def normalize(self, phrase: str, category: Optional[Literal['person', 'org', 'loc']] = None) -> List[Dict]:
        phrase.strip("%20")
        url = f'http://api.tezaurs.lv:8182/normalize_phrase/{phrase}'
        if category is not None:
            url += f"?category={category}"
        response = requests.get(url)
        return response.text
    
