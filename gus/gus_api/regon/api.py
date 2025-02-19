import logging
import re
import pickle
from pathlib import Path
from typing import Any, Optional, Callable

from lxml import objectify
from lxml.objectify import ObjectifiedElement

from .client import Client
from .models import Company, CompanyId, Pkd

with open('./gus/gus_api/regon/doc/tags.pkl','rb') as f:
    tags = pickle.load(f)

class RegonAPI:

    def __init__(self, api_key:Optional[str] = None):
        self._client = Client(api_key=api_key)

    def _format(self, result:ObjectifiedElement, remove_prefix:bool = False)->dict[str,Any]:
        formatted_result = {}
        for field in result.getchildren():
            name = field.tag
            if remove_prefix:
                name = self._remove_prefix(name)
            # name = self._underscore(name)
            formatted_result[name] = field.text
        return formatted_result

    @staticmethod
    def _remove_prefix(name:str)->str:
        return name.split("_",1)[1]
    
    @staticmethod
    def _underscore(word:str)->str:
        """
        Make an underscored, lowercase form from the expression in the string.
        """

        word = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", word)
        word = re.sub(r"([a-z\d])([A-Z])", r"\1_\2", word)
        word = word.replace("-", "_")
        return word.lower()
    
    def find_by(
            self, nip:Optional[str] = None, regon:Optional[str] = None, krs:Optional[str] = None
        )-> list[dict[str,Any]]:
        result = self._client.search(nip=nip, regon=regon, krs=krs)
        result = [self._format(r) for r in objectify.fromstring(result).dane]
        return Company.field_map(result[0])
    
    def get_full_report(self, company_data:CompanyId)->list[dict[str,Any]]:
        try:
            result = self._client.get_full_report(
                regon=company_data.regon,
                company_type= company_data.typ,
                silos_id=company_data.silos_id,
            )
        except KeyError:
            raise ValueError(
                "The company_data parameter should be single item of result of method 'find_by'."
            )
        return self._format(objectify.fromstring(result).dane, remove_prefix=False)
    
    def get_pkd(self, company:CompanyId)->list[dict[str,Any]]:
        match company.typ:
            case "F":
                schema= "BIR11OsFizycznaPkd"
            case "P":
                schema= "BIR11OsPrawnaPkd"
            case _:
                raise ValueError(f'Company typ must be P or F')

        tag_mapper = tags.get(schema)
 
        try:
            result = self._client.get_pkd_report(
                regon=company.regon, company_type=company.typ
            )
        except KeyError:
            raise ValueError(
                "The company_data parameter should be single item of result of method 'find_by'"
            )
        response =  [
            {tag_mapper.get(k):v for k,v in self._format(item).items()}
            for item in objectify.fromstring(result).dane
            ]
        return [Pkd(**r) for r in response]
    
    def get_address(self, company_data:dict[str,Any])->dict[str,Any]:
        try:
            address = f"{company_data['ulica']} {company_data['nr_nieruchomosci']}"
            if company_data['nr_lokalu']:
                address += f"/{company_data['nr_lokalu']}"

            return {
                "ulica":company_data['ulica'],
                "nr_nieruchomosci":company_data['nr_nieruchomosci'],
                "nr_lokalu":company_data['nr_lokalu'],
                "adres":address,
                "kod_pocztowy":company_data['kod_pocztowy'],
                "miejscowosc":company_data['miejscowosc'],
                "gmina":company_data['gmina'],
                "powiat":company_data['powiat'],
                "wojewodztwo":company_data['wojewodztwo'],
            }

        except KeyError:
            raise ValueError("The company_data parameter should be single item")

    def get_contact(self, full_report_data:dict[str,Any])->dict[str,Any]:
        if not ("regon9" in full_report_data or "region14" in full_report_data):
            raise ValueError(
                "The full_report_data parameter should be single item."
            )
        
        return {
            'nr_telefonu':full_report_data.get('numer_telefonu'),
            'nr_wewnetrzny_telefonu':full_report_data.get('numer_wewnetrzny_telefonu'),
            'nr_faksu':full_report_data.get('numer_faksu'),
            'email':full_report_data.get('adres_email'),
            'www':full_report_data.get('adres_stronyinternetowej'),
        }