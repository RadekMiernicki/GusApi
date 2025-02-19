from gus.gusapi import GUS, ApiAtr, ReportTypes
import zeep

report_types = ReportTypes()
api_atr = ApiAtr()
gus = GUS(api_atr = api_atr)

serc = type(gus.service) == zeep.proxy.ServiceProxy

# print(gus.client.wsdl.bindings)
# print(gus.client.transport)



response = gus.search(nip='5261040828')
# response = gus.full_report(regon='00033150100000')
response = gus.full_report(regon='00033150100000', report_type=report_types.P)
print(response)
headers = gus._get_headers(nip='5261040828', report_type=report_types.P)
print(headers)
data = response.get('root').get('dane')

# print(f"NIP: {data.get('praw_nip')}")
# print(f"Nazwa: {data.get('praw_nazwa')}")
# print(f"Kraj siedziby: {data.get('praw_adSiedzKraj_Symbol')}")
# # for key in headers:
# #     print(' - ',key)

# # for header in headers:
# #     print('-', header)

# r = gus._get_details(nip='5170359458')
# print(r)

