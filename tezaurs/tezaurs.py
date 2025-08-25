import requests
from typing import Dict, List, Optional, Literal, Tuple
import xmltodict
from .exceptions import *
import json

class Tezaurs:
    """
    Tezaura API ietvars. 
    Nodrošina metodes latviešu valodas vārdu un frāžu analīzei, locīšanai un morfoloģiskai marķēšanai.
    """
    def __init__(self):
       self.url = 'http://api.tezaurs.lv:8182'
       self.version = 'v1'

    def analyze(self, word: str, lang: Optional[Literal['en']] = None) -> List[Dict]:
        """
        Analizē vārdu, izmantojot Tezaura API.

        Izsauc `/analyze` servisu un atgriež morfoloģisko informāciju par vārdu.

        Argumenti:
            word (str): Vārds, ko analizēt.
            lang (Optional[Literal['en']]): Atbildes valoda 'lv' (pēc noklusējuma) vai 'en'.

        Returns:
            List[Dict]: Morfoloģiskās analīzes rezultāti JSON formātā.
        """
        if not isinstance(word, str):
            raise TezaursTypeError(f"Parametram 'word' jābūt str, bet saņēma {type(word).__name__}")
        
        if lang is not None:
            url = f'{self.url}/analyze/{lang}/{word}'
        else: 
            url = f'{self.url}/analyze/{word}'

        try:
            response = requests.get(url)    
            data = response.json()
            if data == []:
                return f'Vārds "{word}" neeksistē'
            return data
        
        except json.JSONDecodeError:
            raise TezaursJSONError("Kļūda: serveris neatgrieza derīgu JSON!")
        except requests.exceptions.RequestException as e:
            raise TezaursNetworkError(f"Tīkla kļūda: {e}")

    
    def analyze_sentence(self, sentence: str) -> List[Dict]:
        sentence = sentence.replace(' ', '%20')
        url = f'{self.url}/analyzesentence/{sentence}'

        try:
            response = requests.get(url)
            data = response.json()
            if data == []:
                return f'"{sentence}" nav derīgs teikums'
            return data
        
        except json.JSONDecodeError:
            raise TezaursJSONError("Kļūda: serveris neatgrieza derīgu JSON!")
        except requests.exceptions.RequestException as e:
            raise TezaursNetworkError(f"Tīkla kļūda: {e}")

    def inflect(self, word: str, format: Optional[Literal['xml']] = 'json', lang: Optional[Literal['en']] = None) -> List[Dict]:
        if lang is not None:
            url = f'{self.url}/inflect/{format}/{lang}/{word}'
        else:
            url = f'{self.url}/inflect/{format}/{word}'

        try:
            response = requests.get(url)
            if format == 'xml':
                result = xmltodict.parse(response.text)  
            else:
                return response.json()
            return result
        
        except json.JSONDecodeError:
            raise TezaursJSONError("Kļūda: serveris neatgrieza derīgu JSON!")
        except requests.exceptions.RequestException as e:
            raise TezaursNetworkError(f"Tīkla kļūda: {e}")

        
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

        try:
            response = requests.get(url)
            if(format == 'xml'):
                result = xmltodict.parse(response.text)  
            else:
                return response.json()
            return result

        except json.JSONDecodeError:
            raise TezaursJSONError("Kļūda: serveris neatgrieza derīgu JSON!")
        except requests.exceptions.RequestException as e:
            raise TezaursNetworkError(f"Tīkla kļūda: {e}")


    def inflections(self, word: str, paradigm: Optional[Literal['noun-4f', 'verb-1']] = None, stems: Tuple[str, str, str] = None) -> List[Dict]:
        url = f'{self.url}/v1/inflections/{word}'
        if paradigm is not None:
            url += f'?paradigm={paradigm}'
            if stems is not None:
                url += f'&stem1={stems[0]}&stem2={stems[1]}&stem3={stems[2]}'

        try:
            response = requests.get(url)
            return response.json()

        except json.JSONDecodeError:
            raise TezaursJSONError("Kļūda: serveris neatgrieza derīgu JSON!")
        except requests.exceptions.RequestException as e:
            raise TezaursNetworkError(f"Tīkla kļūda: {e}")

    def normalize(self, phrase: str, category: Optional[Literal['person', 'org', 'loc']] = None) -> List[Dict]:
        phrase.strip("%20")
        url = f'{self.url}/normalize_phrase/{phrase}'
        if category is not None:
            url += f"?category={category}"
    
        try:
            response = requests.get(url)
            return response.text
    
        except json.JSONDecodeError:
            raise TezaursJSONError("Kļūda: serveris neatgrieza derīgu JSON!")
        except requests.exceptions.RequestException as e:
            raise TezaursNetworkError(f"Tīkla kļūda: {e}")

    def suitable_paradigm(self, word: str) -> List[Dict]:
        url = f'{self.url}/suitable_paradigm/{word}'
        
        try:
            response = requests.get(url)
            return response.json()
        
        except json.JSONDecodeError:
            raise TezaursJSONError("Kļūda: serveris neatgrieza derīgu JSON!")
        except requests.exceptions.RequestException as e:
            raise TezaursNetworkError(f"Tīkla kļūda: {e}")

    def morphotagger(self, phrase: str) -> List[Dict]:
        url = f'{self.url}/morphotagger/{phrase}'

        try:
            response = requests.get(url)
            return response.json()

        except json.JSONDecodeError:
            raise TezaursJSONError("Kļūda: serveris neatgrieza derīgu JSON!")
        except requests.exceptions.RequestException as e:
            raise TezaursNetworkError(f"Tīkla kļūda: {e}")

    def __str__(self):
        return f'[{self.url}] version {self.version}'