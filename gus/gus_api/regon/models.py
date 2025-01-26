from typing import Optional, Any
from datetime import datetime

from pydantic import BaseModel

class Report(BaseModel):
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
    typ:str
    status_nip:Optional[str] = None
    date_of_termination_of_business_activity:Optional[datetime] = None


    @staticmethod
    def field_map(api_result:dict[str,Any])->dict[str,Any]:
        """
        Method change names of data keys.
        """
        api_result['name'] = api_result.pop('nazwa',None)
        api_result['postal_code'] = api_result.pop('kod_pocztowy',None)
        api_result['city'] = api_result.pop('miejscowosc',None)
        api_result['post'] = api_result.pop('miejscowosc_poczty',None)
        api_result['region'] = api_result.pop('wojewodztwo',None)
        api_result['district'] = api_result.pop('powiat',None)
        api_result['commune'] = api_result.pop('gmina',None)
        api_result['street'] = api_result.pop('ulica',None)
        api_result['street_no'] = api_result.pop('nr_nieruchomosci',None)
        api_result['local_no'] = api_result.pop('nr_lokalu',None)
        api_result['date_of_termination_of_business_activity'] = api_result.pop('data_zakonczenia_dzialalnosci',None)
        #TODO: set date of termination do datetime format

        return api_result
    

    
class ReportNaturlPersonGeneral(BaseModel):
    # BIR11OsFizycznaDaneOgolne
    
    @staticmethod
    def field_map(api_result:dict[str,Any])->dict[str,Any]:
        keys = [
            ('regon9','fiz_regon9'),
            ('nip','fiz_nip'),
            ('status_nip', 'fiz_statusNip'),
        ]
        for new_key, old_key in keys:
            api_result[new_key] = api_result.pop(old_key, None)
        
        return api_result


class ReportIndividualActivityCEIDG(BaseModel):
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

