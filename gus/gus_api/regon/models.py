from typing import Optional, Any, Annotated, Union
from datetime import datetime, date
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber, PhoneNumberValidator

PhoneNumberType = Annotated[
    Union[str,PhoneNumber],
    PhoneNumberValidator(default_region="PL", number_format="E164")]

class BaseReport(ABC):
    __schema__:str= None

    @classmethod
    def field_map(cls, api_result:dict[str,Any])->dict[str,Any]:
        for old_key, new_key in cls.mapper():
            api_result[new_key] = api_result.pop(old_key, None)
        return cls(**api_result)

    @abstractmethod
    def mapper(cls)->list[tuple[str,str]]:
        pass

    @property
    def schema(self)->str:
        '''
        schemas property returns list of schemas described by class
        '''
        return self.__schema__
    
    @schema.setter
    def schema(self, value:str):
        self.__schema__ = value



class CompanyId(BaseModel):
    regon:Optional[str]= Field(min_length=9, max_length=14)
    typ:Optional[str]= None
    silos_id:Optional[int]= None

class Company(BaseModel, BaseReport):
    __schema__:str = ''

    regon:str = Field(min_length=9, max_length=14)
    nip:Optional[str] = Field(pattern=r'[\d]{10}')
    nip_status:Optional[str] = Field(max_length=12)
    name:str = Field(max_length=2000)
    region:Optional[str]= None
    district:Optional[str]= None
    commune:Optional[str]= None
    city:Optional[str]= None
    postal_code:Optional[str] = Field(max_length=12)
    street:str
    street_no:Optional[str]= None
    flat_no:Optional[str]= None
    type:str = Field(max_length=2)
    silos_id:Optional[int]= None
    date_end_of_activity:Optional[date]= None
    postal_location:Optional[str]= None


    @classmethod
    def mapper(cls)->list[tuple[str,str]]:
        keys = [
            ('Regon','regon'),
            ('Nip','nip'),
            ('statusNip','nip_status'),
            ('Nazwa','name'),
            ('Wojewodztwo','region'),
            ('Powiat','district'),
            ('Gmina','commune'),
            ('Miejscowosc','city'),
            ('KodPocztowy','postal_code'),
            ('Ulica','street'),
            ('NrNieruchomosci','street_no'),
            ('NrLokalu','local_no'),
            ('Typ','type'),
            ('SilosID','silos_id'),
            ('DataZakonczeniaDzialalnosci','date_of_termination_of_business_activity'),
            ('MiejscowoscPoczty','post')
        ]
        return keys


class GeneralData(BaseModel):
    # BIR11OsFizycznaDaneOgolne

    regon9:str= Field(min_length=9, max_length=9)
    nip:str= Field(min_lenth=10, max_length=10)
    nip_status:str= Field(min_length=12, max_length=12)
    first_name:Optional[str]= None 
    middle_name:Optional[str]= None
    surname:Optional[str]= None
    date_register:Optional[date]= None
    date_change:Optional[date]= None
    date_deletion_from_evidence:Optional[date]
    basic_legal_form_code:str
    special_legal_form_code:str
    form_of_financing_code:str
    form_of_ownership_code:str
    basic_legal_form_name:str
    special_legal_form_name:str
    form_of_financing_name:str
    form_of_ownership_name:str
    acitvity_ceidg:Optional[int]= None
    activity_agricultural:Optional[int]= None
    activity_other:Optional[int]= None
    activity_ended_before_20141108:Optional[int]= None
    local_units_number:Optional[int]= None



class Activity(BaseModel):
    # BIR11OsFizycznaDzialalnoscCeidg
    # BIR11OsFizycznaDzialalnoscPozostala
    # BIR11OsFizycznaDzialalnoscRolnicza
    # BIR11OsFizycznaDzialalnoscSkreslonaDo20141108
    # BIR11OsPrawna
    # BIR11OsPrawnaListaJednLokalnych
    # BIR11JednLokalnaOsFizycznej
    # BIR11JednLokalnaOsPrawnej

    __schemas__ = None

    regon9:Optional[str]= Field(min_length=9, max_length=9)
    regon14:Optional[str]= Field(min_length=14, max_length=14)
    nip:Optional[str]= Field(min_length=10, max_length=10)
    nip_status:Optional[str]= Field(max_length=12)
    name:str
    short_name:str = Field(max_length=256)
    date_creation:Optional[date]= None
    date_commencement_of_business:Optional[date]= None
    date_register:Optional[date]= None
    date_termination_of_activity:Optional[date]= None
    date_resumption:Optional[date]= None
    date_change:Optional[date]= None
    date_termination_of_business_activity:Optional[date]= None
    date_deletion_from_evidence:Optional[date]= None
    date_bancrupcy_judgement:Optional[date]= None
    date_completion_of_bancrupcy_procedings:Optional[date]= None
    country_code:Optional[str]= None
    region_code:Optional[str]= None
    district_code:Optional[str]= None
    comune_code:Optional[str]= None
    postal_code:Optional[str]= None
    post_office_location_code:Optional[str]= None
    city_code:Optional[str]= None
    street_code:Optional[str]= None
    street_no:Optional[str]= None
    float_no:Optional[str]= None
    secondary_location:Optional[str]= None
    phone:Optional[PhoneNumberType]= None
    phone_internal:Optional[str]= None
    fax:Optional[PhoneNumberType]= None
    email:Optional[EmailStr]= None
    homepage:Optional[str]= None
    country:Optional[str]= None
    region:Optional[str]= None
    district:Optional[str]= None
    commune_name:Optional[str]= None
    city:Optional[str]= None
    post_office_location_name:Optional[str]= None
    street:Optional[str]= None
    date_evidence:Optional[date]= None
    date_deletion_from_evidence:Optional[str]= None
    evidence_number:Optional[str]= None
    evidence_type_code:Optional[str]= None
    registration_authority_code:Optional[str]= Field(max_length=9)
    register_type_code:Optional[str]= Field(max_length=3)
    register_type_name:Optional[str]= None
    activity_not_started:Optional[str]= None
    basic_legal_form_code:Optional[str]= None
    special_legal_form_code:Optional[str]= None
    form_of_financing_code:Optional[str]= None
    form_of_ownership_code:Optional[str]= None
    fouding_authority_code:Optional[str]= None
    basic_legal_form_name:Optional[str]= None
    special_legal_form_name:Optional[str]= None
    form_of_financing_name:Optional[str]= None
    form_of_ownership_name:Optional[str]= None
    founding_authority_name:Optional[str]= None
    registration_authority_name:Optional[str]= None
    evidence_type_name:Optional[str]= None
    local_units_number:Optional[str]= None
    silos_id:Optional[int]= None
    silos_name:Optional[str]= None
    

class Pkd(BaseModel):
    # BIR11OsFizycznaPkd
    # BIR11JednLokalnaOsFizycznejPkd
    # BIR11JednLokalnaOsPrawnejPkd

    __schemas__ = None

    pkd_code:Optional[str]= Field(max_length=5)
    pkd_name:Optional[str]= None
    pkd_dominant:Optional[str]= None
    silos_id:Optional[int]= None
    silos_name:Optional[str]= Field(max_length=10)
    date_deletion_from_evidence:Optional[date]= None

class ShareHolder(BaseModel):
    # BIR11OsPrawnaSpCywilnaWspolnicy
    share_holder:Optional[str]= None
    first_name:Optional[str]= None
    middle_name:Optional[str]= None
    surname:Optional[str]= None
    name:Optional[str]= None

class CompanyType(BaseModel):
    # BIR11TypPodmiotu

    type:str


class Report(BaseModel, BaseReport):
    # BIR11DaneSzukajPodmioty
    nip:str
    regon:str
    name:str
    postal_code:str
    postal:Optional[str] = None
    city:str
    region:str
    district:str
    commune:str
    street:str
    street_no:Optional[str] = None
    local_no:Optional[str] = None
    silos_id:int
    type:str
    status_nip:Optional[str] = None
    date_of_termination_of_business_activity:Optional[datetime] = None

    @classmethod
    def mapper(cls)->list[tuple[str,str]]:
        keys = [
            ('Regon','regon'),
            ('Nip','nip'),
            ('statusNip','status_nip'),
            ('Nazwa','name'),
            ('Wojewodztwo','region'),
            ('Powiat','district'),
            ('Gmina','commune'),
            ('Miejscowosc','city'),
            ('KodPocztowy','postal_code'),
            ('Ulica','street'),
            ('NrNieruchomosci','street_no'),
            ('NrLokalu','local_no'),
            ('Typ','type'),
            ('SilosID','silos_id'),
            ('DataZakonczeniaDzialalnosci','date_of_termination_of_business_activity'),
            ('MiejscowoscPoczty','post')
        ]
        return keys

    