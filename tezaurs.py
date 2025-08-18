import requests
from typing import Dict, List, Optional, Literal, Tuple
import xmltodict

class Tezaurs:
    def __init__(self):
       self.url = 'http://api.tezaurs.lv:8182'
       self.version = 'v1'

    def analyze(self, word: str, lang: Optional[Literal['en']] = None) -> List[Dict]:
        if lang is not None:
            url = f'{self.url}/analyze/{lang}/{word}'
        else: 
            url = f'{self.url}/analyze/{word}'
        response = requests.get(url)
        return response.json()
    
    def analyze_sentence(self, sentence: str) -> List[Dict]:
        sentence.strip("%20")
        url = f'{self.url}/analyzesentence/{sentence}'
        response = requests.get(url)
        return response.json()
    
    def inflect(self, word: str, format: Optional[Literal['xml']] = 'json', lang: Optional[Literal['en']] = None) -> List[Dict]:
        if lang is not None:
            url = f'{self.url}/inflect/{format}/{lang}/{word}'
        else:
            url = f'{self.url}/inflect/{format}/{word}'
        response = requests.get(url)
        if(format == 'xml'):
            result = xmltodict.parse(response.text)  
        else:
            return response.json()
        return result
    
    def inflect_phrase(self, phrase: str, category: Optional[Literal['person', 'org', 'loc']] = None) -> List[Dict]:
        phrase.strip("%20") 
        url = f'{self.url}/inflect_phrase/{phrase}'
        if category is not None:
            url += f"?category={category}"
        response = requests.get(url)
        return response.json()
    
    def inflect_people(self, name: str, format: Optional[Literal['xml']] = 'json', gender: Optional[Literal['m', 'f']] = None) -> List[Dict]:
        url =  f'{self.url}/inflect_people/{format}/{name}'
        if gender is not None:
            url += f'?gender={gender}'
        response = requests.get(url)
        if(format == 'xml'):
            result = xmltodict.parse(response.text)  
        else:
            return response.json()
        return result

    def inflections(self, word: str, paradigm: Optional[Literal['noun-4f', 'verb-1']] = None, stems: Tuple[str, str, str] = None) -> List[Dict]:
        url = f'{self.url}/v1/inflections/{word}'
        if paradigm is not None:
            url += f'?paradigm={paradigm}'
            if stems is not None:
                url += f'&stem1={stems[0]}&stem2={stems[1]}&stem3={stems[2]}'
        response = requests.get(url)
        return response.json()

    def normalize(self, phrase: str, category: Optional[Literal['person', 'org', 'loc']] = None) -> List[Dict]:
        phrase.strip("%20")
        url = f'{self.url}/normalize_phrase/{phrase}'
        if category is not None:
            url += f"?category={category}"
        response = requests.get(url)
        return response.text
    
    def suitable_paradigm(self, word: str) -> List[Dict]:
        url = f'{self.url}/suitable_paradigm/{word}'
        response = requests.get(url)
        return response.json()
    
    def morphotagger(self, phrase: str) -> List[Dict]:
        url = f'{self.url}/morphotagger/{phrase}'
        response = requests.get(url)
        return response.json()

    def __str__(self):
        return f'[{self.url}] version {self.version}'