# Tezaurs API Wrapper

Tezaurs API Wrapper ir Python bibliotēka, kas ļauj ērti piekļūt [Tezaurs.lv](https://tezaurs.lv/) latviešu valodas vārdnīcas datubāzei caur API. Šī bibliotēka atvieglo vārdu, to nozīmju un tulkojumu meklēšanu, kā arī integrāciju latviešu valodas lietojumos.

## Iespējas

- Meklēt vārdus, to nozīmes un tulkojumus no Tezaurs.lv datubāzes
- Vienkārša piekļuve vārdnīcas ierakstiem
- API pieprasījumu un atbilžu apstrāde ar kļūdu apstrādi
- Paplašināma dažādiem pielietojumiem

## Uzstādīšana

Klonējiet šo repozitoriju un instalējiet atkarības:

```bash
git clone https://github.com/nrenars/tezaurs-api-wrapper.git
cd tezaurs-api-wrapper
pip install -r requirements.txt
```

## Lietošana

Vienkāršs piemērs, kā izmantot API wrapperi Python valodā:

```python
from tezaurs_api_wrapper import TezaursAPI

tezaurs = TezaursAPI()

rezultats = tezaurs.search('vārds')
print(rezultats)
```

### API Metodes

- `search(word: str) -> dict`  
  Meklē vārdu Tezaurs.lv vārdnīcā
- `get_definition(word_id: str) -> dict`  
  Atgriež konkrētā vārda nozīmes
- `get_translation(word: str, target_lang: str) -> dict`  
  Atgriež vārda tulkojumu uz norādīto valodu

## Konfigurācija

Dažām metodēm var būt nepieciešama API atslēga. Lūdzu, skatiet [Tezaurs.lv API dokumentāciju](https://tezaurs.lv/api), lai iegūtu vairāk informācijas.

API atslēgas iestatīšana:

```python
tezaurs = TezaursAPI(api_key='JŪSU_API_ATSLĒGA')
```

## Iesaistīšanās

Priecāsimies par jebkādu ieguldījumu! Atveriet issue vai iesniedziet pull request.

1. Forkojiet repozitoriju
2. Izveidojiet savu branch (`git checkout -b feature/manas-izmainas`)
3. Veiciet izmaiņas un commitojiet (`git commit -am 'Pievienots jauns funkcionalitāte'`)
4. Push uz savu branch (`git push origin feature/manas-izmainas`)
5. Atveriet pull request

## Licence

Projekts ir licencēts saskaņā ar MIT licenci. Skatiet [LICENSE](LICENSE) failu.

## Resursi

- [Tezaurs.lv](https://tezaurs.lv/)
- [Tezaurs.lv API dokumentācija](https://tezaurs.lv/api)
- [Issue sekcija](https://github.com/nrenars/tezaurs-api-wrapper/issues)

---

_Šis projekts nav saistīts ar Tezaurs.lv._
