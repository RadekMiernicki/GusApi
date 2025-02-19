import re
from pathlib import Path

file_path = 'gus/gus_api/regon/doc/Bir11ResultsAsSqlTables.sql.txt'
with open(file_path, 'r') as f:
    text = f.read()
    ddl = text.split(';')
ddl = [statement.strip() for statement in ddl]

schemas = {}
for declaration in ddl[1:]:
    if declaration != '':
        schema=re.findall(r'DECLARE\s\[(.*)\]\s', declaration)[0]
        fields=re.findall(r'\[(.*)\]\s\[', declaration)
        schemas[schema] = fields

schemas['BIR11DaneSzukajPodmioty'] = [
    'Regon','Nip','StatusNip','Nazwa','Wojewodztwo','Powiat',
    'Gmina','Miejscowosc','KodPocztowy','Ulica','NrNieruchomosci',
    'NrLokalu','Typ','SilosID','DataZakonczeniaDzialalnosci',
    'MiejscowoscPoczty'
]

keys = [
    ('Nip', 'nip'),
    ('DataZakonczeniaDzialalnosci', 'date_end_of_activity'),
    ('Gmina', 'commune'),
    ('StatusNip', 'nip_status'),
    ('Ulica', 'street'),
    ('KodPocztowy', 'postal_code'),
    ('SilosID', 'silos_id'),
    ('Nazwa', 'name'),
    ('MiejscowoscPoczty', 'postal_location'),
    ('Wojewodztwo', 'region'),
    ('Regon', 'regon'),
    ('Typ', 'type'),
    ('NrNieruchomosci', 'street_no'),
    ('Powiat', 'district'),
    ('NrLokalu', 'flat_no'),
    ('Miejscowosc', 'city'),
    ('adSiedzGmina_Nazwa', 'commune_name'),
    ('adSiedzGmina_Symbol', 'commune_code'),
    ('adSiedzKodPocztowy', 'postal_code'),
    ('adSiedzKraj_Nazwa', 'country'),
    ('adSiedzKraj_Symbol', 'country_code'),
    ('adSiedzMiejscowoscPoczty_Nazwa', 'post_office_location_name'),
    ('adSiedzMiejscowoscPoczty_Symbol', 'post_office_location_code'),
    ('adSiedzMiejscowosc_Nazwa', 'city'),
    ('adSiedzMiejscowosc_Symbol', 'city_code'),
    ('adSiedzNietypoweMiejsceLokalizacji', 'secondary_location'),
    ('adSiedzNumerLokalu', 'flat_no'),
    ('adSiedzNumerNieruchomosci', 'street_no'),
    ('adSiedzPowiat_Nazwa', 'district'),
    ('adSiedzPowiat_Symbol', 'district_code'),
    ('adSiedzUlica_Nazwa', 'street'),
    ('adSiedzUlica_Symbol', 'street_code'),
    ('adSiedzWojewodztwo_Nazwa', 'region'),
    ('adSiedzWojewodztwo_Symbol', 'region_code'),
    ('adresEmail', 'email'),
    ('adresEmail2', 'secondary_email'),
    ('adresStronyinternetowej', 'homepage'),
    ('dataOrzeczeniaOUpadlosci', 'date_bancrupcy_judgment'),
    ('dataPowstania', 'date_creation'),
    ('dataRozpoczeciaDzialalnosci', 'date_commencement_of_business'),
    ('dataSkresleniaDzialalanosciZRegon', 'date_deletion_from_evidence'),
    ('dataSkresleniaDzialalnosciZRegon', 'date_deletion_from_evidence'),
    ('dataSkresleniaPodmiotuZRegon', 'date_deletion_from_evidence'),
    ('dataSkresleniaZRegon', 'date_deletion_from_evidence'),
    ('dataSkresleniaZRejestruEwidencji', 'date_deletion_from_evidence'),
    ('dataWpisuDoRegon', 'date_register'),
    ('dataWpisuDoRejestruEwidencji', 'date_ewidence'),
    ('dataWpisuDzialalnosciDoRegon', 'date_register'),
    ('dataWpisuPodmiotuDoRegon', 'date_register'),
    ('dataWznowieniaDzialalnosci', 'date_resumption'),
    ('dataZaistnieniaZmiany', 'date_change'),
    ('dataZaistnieniaZmianyDzialalnosci', 'date_change'),
    ('dataZakonczeniaDzialalnosci', 'date_termination_of_business_activity'),
    ('dataZakonczeniaPostepowaniaUpadlosciowego', 'date_completion_of_bancrupcy_procedings'),
    ('dataZawieszeniaDzialalnosci', 'date_termination_of activity'),
    ('dzialalnoscCeidg', 'activity_ceidg'),
    ('dzialalnoscPozostala', 'activity_other'),
    ('dzialalnoscRolnicza', 'activity_agricultural'),
    ('dzialalnoscSkreslonaDo20141108', 'activity_ended_before_20141108'),
    ('firmaNazwa', 'name'),
    ('formaFinansowania_Nazwa', 'form_of_financing_name'),
    ('formaFinansowania_Symbol', 'form_of_financing_code'),
    ('formaWlasnosci_Nazwa', 'form_of_ownership_name'),
    ('formaWlasnosci_Symbol', 'form_of_ownership_code'),
    ('imie1', 'first_name'),
    ('imie2', 'middle_name'),
    ('imieDrugie', 'middle_name'),
    ('imiePierwsze', 'first_name'),
    ('liczbaJednLokalnych', 'local_units_number'),
    ('nazwa', 'name'),
    ('nazwaSkrocona', 'short_name'),
    ('nazwisko', 'surname'),
    ('nip', 'nip'),
    ('numerFaksu', 'fax'),
    ('numerTelefonu', 'phone'),
    ('numerWRejestrzeEwidencji', 'evidence_number'),
    ('numerWewnetrznyTelefonu', 'phone_internal'),
    ('numerWrejestrzeEwidencji', 'evidence_number'),
    ('numerwRejestrzeEwidencji', 'evidence_number'),
    ('organRejestrowy_Nazwa', 'registration_authority_name'),
    ('OrganRejestrowy_Nazwa', 'registration_authority_name'),
    ('organRejestrowy_Symbol', 'registration_authority_code'),
    ('OrganRejestrowy_Symbol', 'registration_authority_code'),
    ('organZalozycielski_Nazwa', 'founding_authority_name'),
    ('OrganZalozycielski_Nazwa', 'founding_authority_name'),
    ('organZalozycielski_Symbol', 'founding_authority_code'),
    ('OrganZalozycielski_Symbol', 'founding_authority_code'),
    ('pkdKod', 'pkd_code'),
    ('pkdNazwa', 'pkd_name'),
    ('pkdPrzewazajace', 'pkd_dominant'),
    ('pkd_Kod', 'pkd_code'),
    ('pkd_Nazwa', 'pkd_name'),
    ('pkd_Przewazajace', 'pkd_dominant'),
    ('podstawowaFormaPrawna_Nazwa', 'basic_legal_form_name'),
    ('podstawowaFormaPrawna_Symbol', 'basic_legal_form_code'),
    ('regon14', 'regon14'),
    ('regon9', 'regon9'),
    ('regonWspolnikSpolki', 'share_holder'),
    ('rodzajRejestruEwidencji_Nazwa', 'evidence_type_name'),
    ('RodzajRejestruEwidencji_Nazwa', 'evidence_type_name'),
    ('RodzajRejestru_Nazwa', 'register_type_name'),
    ('rodzajRejestruEwidencji_Symbol', 'evidence_type_code'),
    ('RodzajRejestruEwidencji_Symbol', 'evidence_type_code'),
    ('RodzajRejestru_Symbol', 'register_type_code'),
    ('silosID', 'silos_id'),
    ('silos_Nazwa', 'silos_name'),
    ('silos_Symbol', 'silos_name'),
    ('Silos_Symbol', 'silos_name'),
    ('statusNip', 'nip_status'),
    ('szczegolnaFormaPrawna_Nazwa', 'special_legal_form_name'),
    ('szczegolnaFormaPrawna_Symbol', 'special_legal_form_code'),
    ('NiePodjetoDzialalnosci', 'activity_not_started')
]

keys = {k:v for k,v in keys}

pattern = r'^(?:[a-zA-Z]*_)(.*)'
for schema in schemas:
    print(schema)
    if schema not in ['BIR11DaneSzukajPodmioty','BIR11TypPodmiotu']:
        tags = {t:keys.get(re.findall(pattern,t)[0]) for t in schemas[schema]}
    else:
        tags = {t:keys.get(t) for t in schemas[schema]}
    schemas[schema] = tags

    
import pickle

with open('./gus/gus_api/regon/doc/tags.pkl','wb') as f:
    pickle.dump(schemas, f)

schema_name = 'BIR11TypPodmiotu'
print(f'Schema name: {schema_name}\n')
print(schemas.get(schema_name).values())