from typing import Optional, Any
from datetime import datetime
from abc import ABC, abstractmethod

from pydantic import BaseModel, Field

class BaseReport(ABC):

    @classmethod
    def field_map(cls, api_result:dict[str,Any])->dict[str,Any]:
        for old_key, new_key in cls.mapper():
            api_result[new_key] = api_result.pop(old_key, None)
        return cls(**api_result)

    @abstractmethod
    def mapper(cls)->list[tuple[str,str]]:
        pass

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

    

    
class ReportNaturlPersonGeneral(BaseModel, BaseReport):
    # BIR11OsFizycznaDaneOgolne
    regon9:str =  Field(str, max_length=9, min_length=9)
    nip:str = Field(str, max_digits=14, min_length=14)
    status_nip:str
    surname:str
    first_name:str
    last_name:str
    middle_name:Optional[str] = None


    def mapper(cls)->list[tuple[str,str]]:
        keys = [
            ('fiz_regon9','regon9'),
            ('fiz_nip','nip'),
            ('fiz_statusNip','status_nip'),
            ('fiz_nazwisko','surname'),
            ('fiz_imie1', 'first_name'),
            ('fiz_imie2','middle_name'),
            ('fiz_dataWpisuPodmotuDoRegon', 'date_register'),
            ('fiz_dataZaistnieniaZmiany','date_update'),
            ('fiz_dataSklresleniaPodmiotuZRegon','date_remove'),
            ('fiz_podstawowaFormaPrawna_Symbol'),
            ('fiz_szczegolnaFormaPrawna_Symbol'),
            ('fiz_formaFinansowania_Symbol'),
            ('fiz_formaWlasnosci_Symbol'),
            ('fiz_podstawowaFormaPrawna_Nazwa'),
            ('fiz_szczegolnaFormaPrawna_Nazwa'),
            ('fiz_formaFinansowania_Nazwa'),
            ('fiz_formaWlasnosi_Nazwa'),
            ('fiz_dzialalnoscCeidg'),
            ('fiz_dzialalnoscRolnicza'),
            ('fiz_dzialalnoscPozostala'),
            ('fiz_dzialalnoscSkreslonaDo20141108'),
            ('fiz_liczbaJednLokalnych')
        ]
        return keys


class ReportIndividualActivityCeidg(BaseModel, BaseReport):
    # BIR11OsFizycznaDzialalnoscCeidg
    pass


class ReportIndividualActivityOther(BaseModel):
    # BIR11OsFizycznaDzialalnoscPozostala]
    pass

class ReportIndividualAgriculturalActivity(BaseModel):
    # BIR11OsFizycznaDzialalnoscRolnicza
    pass 

class ReportIndividualActvityBefore20141108(BaseModel):
    # BIR11OsFizycznaDzialalnoscSkreslonaDo20141108
    pass
    
class ReportNaturalPersonListLocalUnits(BaseModel):
    # BIR11OsFizycznaListaJednLokalnych
    pass

class ReportNaturalPersonPKD(BaseModel):
    # BIR11OsFizycznaPkd
    pass

class ReportCorporateEntity(): # LegalPerson
    # BIR11OsPrawna
    pass

class ReportCorporateEntityListLocalUnits(BaseModel):
    # BIR11OsPrawnaListaJednLokalnych
    pass

class ReportCorporateEntityPKD(BaseModel):
    # BIR11OsPrawnaPkd
    pass

class ReportCorporateEntityShareHolders(BaseModel):
    # BIR11OsPrawnaSpCywilnaWspolnicy
    pass


class ReportIndividualLcocalUnit(BaseModel):
    # BIR11JednLokalnaOsFizycznej
    pass

class ReportIndividualLovalUnitPKD(BaseModel):
    # BIR11JednLokalnaOsFizycznejPkd
    pass

class ReportCorporateEntityLocalUnit(BaseModel):
    # BIR11JednLokalnaOsPrawnej
    pass

class ReportCorporateEntityLocalUnitPKD(BaseModel):
    # BIR11JednLokalnaOsPrawnejPkd
    pass

class ReportEntityType(BaseModel):
    # BIR11TypPodmiotu
    pass




class Address(BaseModel):
    pass

class PKD(BaseModel):
    pass

