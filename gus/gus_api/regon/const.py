WSDL = "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-prod.wsdl"
WSDL12 = ""
ENDPOINT = "https://wyszukiwarkaregon.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc"
WSDL_SANDBOX = "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/wsdl/UslugaBIRzewnPubl-ver11-test.wsdl"
ENDPOINT_SANDBOX = "https://wyszukiwarkaregontest.stat.gov.pl/wsBIR/UslugaBIRzewnPubl.svc"
APIKEY_SANDBOX = "abcde12345abcde12345"

DETAILED_REPORT_NAMES_BY_TYPE = {
    # podmiot osoby fizycznej prowadzącej działalność gospodarczą
    "F": {
        # działalność podlegającą wpisowi do CEIDG
        "1": "BIR11OsFizycznaDzialalnoscCeidg",
        # działalność rolnicza (gospodarstwo rolne, działy specjaln eprodukcji rolnej)
        "2": "BIR11OsFizycznaDzialalnoscRolnicza",
        # działalność inna (komornik, notariusz, agroturystyka – o ile nie wpisane do CEIDG)
        "3": "BIR11OsFizycznaDzialalnoscPozostala",
        # działalność skreślona z rejestru REGON przed datą 08.11.2014 (w poprzednim systemie inform.)
        "4": "BIR11OsFizycznaDzialalnoscSkreslonaDo20141108",
    },
    # jednostka lokalna podmiotu osoby fizycznej
    "LF": "BIR11JednLokalnaOsFizycznej",
    # osoba prawna oraz jednostka organizacyjna niemająca osobowości prawnej
    # ma przypisaną wartość SilosID równą 6 - w dokumentacji opisana jako - wartość techniczna,
    # bez znaczenia merytorycznego; istnieje wyłącznie dla zachowania spójności struktury
    "P": "BIR11OsPrawna",
    # jednostka lokalna osoby prawnej
    "LP": "BIR11JednLokalnaOsPrawnej",
}

PKD_REPORT_TYPE = {
    "F": "PublDaneRaportDzialalnosciFizycznej",
    "P": "PublDaneRaportDzialalnosciPrawnej",
}
