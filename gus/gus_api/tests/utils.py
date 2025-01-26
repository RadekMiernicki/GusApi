from typing import Any

def check_structure_base_data(data:dict[str,Any]):
    assert sorted(list(data.keys())) == [
        "data_zakonczenia_dzialalnosci", "gmina", "kod_pocztowy",
        "miejscowosc", "nazwa", "nip", "nr_lokalu",
        "nr_nieruchomosci", "powiat"," regon", "silos_id",
        "status_nip", "typ", "ulica", "wojewodztwo"
    ]

def check_structure_address(address):
    assert sorted(list(address)) == [
        "adres", "gmina", "kod_pocztowy", "miejscowosc",
        "nr_lokalu", "nr_nieruchomosci", "powiat", "ulica", "wojewodztwo"
    ]

def check_structure_pkd(pkd):
    assert sorted(list(pkd)) == ['kod','nazwa','przewazajaca']

def check_structure_contact(contact):
    assert sorted(list(contact)) == [
        "email", "nr_faksu","nr_telefonu","nr_wewnetrzny_telefonu","www"
    ]

def check_structure_report_f1(details):
    pass

def check_structure_report_f2(details):
    pass

def check_structure_report_f3(details):
    pass

def check_structure_report_p(details):
    pass

def check_structure_report_lf(details):
    pass

def check_structure_report_lp(details):
    pass

