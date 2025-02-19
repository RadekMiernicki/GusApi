import logging
from typing import Optional

from lxml import objectify
from lxml.etree import XMLSyntaxError

from requests import Session
from zeep import Client as ZeepClient
from zeep import Transport

#TODO: add logger

from .const import (
    WSDL, ENDPOINT,
    WSDL_SANDBOX, ENDPOINT_SANDBOX,
    APIKEY_SANDBOX,
    DETAILED_REPORT_NAMES_BY_TYPE,
    PKD_REPORT_TYPE
)
from .exceptions import EmptyResponse, UnexpectedResponse, RegonAPIError

class Client:

    headers = {}

    def __init__(self, api_key:Optional[str] = None):

        wsdl = WSDL if api_key else WSDL_SANDBOX
        self.endpoint = ENDPOINT if api_key else ENDPOINT_SANDBOX
        self.api_key = api_key or APIKEY_SANDBOX

        transport = Transport(session=Session())
        transport.session.headers = self.headers
        self.client = ZeepClient(wsdl, transport=transport)
        self.service=None

    def _call(self, action:str, *args, **kwargs)->str:
        if not self.service:
            self.service = self.client.create_service(
                "{http://tempuri.org/}e3", self.endpoint
            )
            self.headers.update({"sid": self._login()})
        service = getattr(self.service, action)
        return service(*args, **kwargs)

    def _login(self)->str:
        return self._call("Zaloguj", self.api_key)
    
    def search(self, *, 
               nip:Optional[str]=None, 
               regon:Optional[str]=None,
               krs:Optional[str]=None)->str:
        if not any([nip, regon, krs]):
            raise AttributeError(
                "At least one parameter (nip, regon, krs) is required."
            )
        if nip:
            search_params = {"Nip":nip}
        elif regon:
            search_params = {"Regon":regon}
        else:
            search_params = {"Krs":krs}
        return self.validate_result(self._call("DaneSzukajPodmioty", search_params))
    
    def get_full_report(
            self, regon:str, company_type:str, silos_id:Optional[int]=None
        )->str:
        report_name = DETAILED_REPORT_NAMES_BY_TYPE.get(company_type)
        if isinstance(report_name, dict):
            report_name = report_name(silos_id)
        return self.validate_result(
            self._call("DanePobierzPelnyRaport", regon, report_name)
            )
        
    def get_pkd_report(self, regon:str, company_type:str)->str:
        report_type = (
            PKD_REPORT_TYPE[company_type]
            if company_type in PKD_REPORT_TYPE
            else PKD_REPORT_TYPE["F"]
        )
        return self.validate_result(self._call("DanePobierzPelnyRaport", regon, report_type))

    @staticmethod
    def validate_result(result:str)->str:
        if not result:
            raise EmptyResponse()
        try:
            result_object = objectify.fromstring(result)

        except XMLSyntaxError:
            raise  UnexpectedResponse(f"Unexpected response: {result}")
        
        if not hasattr(result_object, "dane"):
            raise UnexpectedResponse(f"Unexpected response: {result}")
        
        if hasattr(result_object.dane, 'ErrorCode'):
            raise RegonAPIError(result_object.dane.ErrorMessageEn, result_object.dane.ErrorCode)
        
        return result
