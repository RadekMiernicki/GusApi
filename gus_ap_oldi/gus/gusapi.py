from dataclasses import dataclass

from requests import Session
from zeep import Client, Transport
import xmltodict
import yaml

sandbox = True

from os import getcwd

print(f'gusapi cwd: {getcwd()}')

with open ('./args.yml', 'r') as f:
    r = f.read()
    const = yaml.load(r,yaml.SafeLoader)
    __version__  = const['version']

if sandbox:
    const = const['sandbox']


@dataclass
class ApiAtr:
    WDSL:str = const['WSDL']
    ENDPOINT:str = const['ENDPOINT']
    API_KEY:str = const['API_KEY']

@dataclass
class ReportTypes:
    LF:str ='PublDaneRaportLokalnaFizycznej'
    P: str ='PublDaneRaportPrawna'
    LP:str ='PublDaneRaportLokalnaPrawnej'
    F1:str ='PublDaneRaportDzialalnoscFizycznejCeidg'
    F2:str ='PublDaneRaportDzialalnoscFizycznejRolnicza'
    F3:str ='PublDaneRaportDzialalnoscFizycznejPozostala'
    F4:str ='PublDaneRaportDzialalnoscFizycznejWKrupgn'
    pkdF:str= 'PublDaneRaportDzialalnosciFizycznej'
    pkdP:str= 'PublDaneRaportDzialalnosciPrawnej'


class GUS:

    login:str = 'Zaloguj'
    logout:str ='Wyloguj'
    search_by_id:str = 'DaneSzukaj'
    fullreport:str='DanePobierzPelnyRaport'

    def __init__(self, wdsl:str = None, endpoint:str = None, api_key:str = None, 
                    api_atr: ApiAtr = None, version:str = None):
        if not any([all([wdsl, endpoint, api_key]), api_atr]):
            raise AttributeError ('Api key is required.')

        self.api_key = api_key or api_atr.API_KEY
        self.wdsl = wdsl or api_atr.WDSL
        self.endpoint = endpoint or api_atr.ENDPOINT
        self.headers = {'User-Agent':'PGZ_GUS/%s'%version}

        transport = Transport(session=Session())
        transport.session.headers = self.headers
        self.client = Client(self.wdsl, transport=transport)
        self.binding_name = self.client.wsdl.bindings.keys()
        self.service = self.client.create_service('{http://tempuri.org/}e3', self.endpoint)
        self.headers.update({'sid':self._service(self.login, self.api_key)})

    def _service(self, action, *args, **kwargs):
        service = getattr(self.service, action)
        return service(*args, **kwargs)

    def _get_details(self, nip: str=None, krs: str=None, regon: str=None, *args, **kwargs):
        """
        doc string
        """
        if not any([nip, krs, regon]):
            raise AttributeError('At least one parameter (nip, regon, krs) is required.')
        search_params = {p:v for p,v in {'Regon':regon, 'Nip':nip, 'Krs':krs}.items() if v is not None}

        return self._service(self.search_by_id, search_params)

    def search(self, *args, **kwargs) -> dict[str,str]:
        """
        function search GUS db 
        """
        details = self._get_details( *args, **kwargs)
        data = xmltodict.parse(details)

        return data.get('root').get('dane')

    def _get_regon(self, *args, **kwargs):
        regon = kwargs.get('regon')
        if not regon:
            regon = self.search(*args, **kwargs).get('Regon')
        return regon

    def _get_full_details(self, *args, **kwargs):
        """
        doc string
        """
        regon = self._get_regon(*args, **kwargs)
        return self._service(self.fullreport, regon, kwargs.get('report_type'))

    def _get_headers(self, *args, **kwargs):
        details = self._get_full_details(*args, **kwargs)
        data = xmltodict.parse(details)
        headers = data.get('root').get('dane').keys()
        headers = [k.split('_')[1] for k in headers]
        return headers

    def full_report(self, *args, **kwargs):
        """
        doc string
        """
        details = self._get_full_details(*args, **kwargs)
        if details:
            return xmltodict.parse(details)

        return None
        
        

if __name__ == '__main__':

    print(__name__,':', __version__)

    api_atr = ApiAtr()
    gus = GUS(api_atr=api_atr)

    print(gus.headers)
    print(gus.api_key)
    print(gus.binding_name)
    # print(gus.client)