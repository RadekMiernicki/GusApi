## GUS

[GUS (Główny Urząd Statystyczny) REGON](https://wyszukiwarkaregon.stat.gov.pl/appBIR/index.aspx) Internet Database client which allows to get detailed information about company based on NIP, Regon, or KRS number.

__It requires an API key to the [BIR1 service](http://bip.stat.gov.pl/dzialalnosc-statystyki-publicznej/rejestr-regon/interfejsyapi/)__

### Quickstart

Install the package via pip:

```
pip install api_gus
```

### Usage

Returns the business address

```
from gus import GUS

gus = GUS(api_key='my_api_key')
gus.get_address(nip='1112223344')
```

output:

'''
{
    'name': 'REGON SYSTEMS SPÓŁKA AKCYJNA',
    'street_address': 'ul. Tęczowa 14',
    'postal_code': '35-322',
    'city': 'Rzeszów'
}
'''

Returns PKD codes

```
gus.get_pkd(nip='1112223344')
```

output:

```
[
    {
        'code': '6201Z',
        'name': 'DZIAŁALNOŚĆ ZWIĄZANA Z OPROGRAMOWANIEM',
        'main': True
    },
    {
        'code': '6312Z':
        'name': 'DZIAŁALNOŚĆ PORTALI INTERNETOWYCH',
        'main': False
    },
    ...
]
```

Returns all data from BIR1 service

```
gus.search(nip='1112223344')
```

output:
```
{
    'adsiedzkraj_symbol': 'PL',
    'datazawieszeniadzialalnosci': '',
    'jednosteklokalnych': '0',
    'rodzajrejestruewidencji_symbol': '138',
    'adkorulica_nazwa': '',
    ...
    'adkorpowiat_symbol': '63',
    'datawpisudoregon': '2012-06-01',
    'rodzajrejestruewidencji_nazwa': 'REJESTR PRZEDSIĘBIORCÓW',
    'adsiedznumernieruchomosci': '14',
    'adkorkodpocztowy': '35322',
    'adsiedzkraj_nazwa': 'POLSKA',
    'adsiedzulica_symbol': '10013',
    'adsiedzkodpocztowy': '35322',
}
```

Sandbox mode testing:

```
from gus import GUS

gus = GUS(sandbox=True)
gus.get_address(nip='1112223344')
```

