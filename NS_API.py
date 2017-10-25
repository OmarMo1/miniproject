import xmltodict, requests
from datetime import datetime
from datetime import timezone

beginstation = 'Amsterdam'
eindstation = 'Rotterdam'

#print(response.text)

def request(beginstation, eindstation):
    # auth_details = ('mohamed.omar@student.hu.nl', 'zQYfnb1XEgH7eMqdfCi6k1rZ-GjRD70Nwy2_GZdSxRiccCrmQCahpQ')
    # api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + beginstation
    # response = requests.get(api_url, auth=auth_details)
    # with open('vertrektijden.xml', 'w') as myXMLFile:
    #     myXMLFile.write(response.text)

    auth_detailss = ('mohamed.omar@student.hu.nl', 'zQYfnb1XEgH7eMqdfCi6k1rZ-GjRD70Nwy2_GZdSxRiccCrmQCahpQ')
    api_urls = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation='+beginstation+'&toStation='+eindstation
    response = requests.get(api_urls, auth=auth_detailss)
    with open('treinplanner.xml', 'w') as treinplannerFile:
        treinplannerFile.write(response.text)

request(beginstation, eindstation)


def vertrektijden():
    with open('treinplanner.xml', 'r') as treinplannerFile:
        content = xmltodict.parse(treinplannerFile.read())
        for line in content['ReisMogelijkheden']['ReisMogelijkheid']:
            vertrektijd = datetime.strptime(line['ActueleVertrekTijd'], '%Y-%m-%dT%H:%M:%S%z')
            vertrektijd = '{:02d}:{:02d}'.format(vertrektijd.hour, vertrektijd.minute)
            nu = datetime.now()
            nu = nu.replace(tzinfo=timezone.utc)
            nu = '{:02d}:{:02d}'.format(nu.hour, nu.minute)

            if vertrektijd > nu:
                return vertrektijd

vertrektijd = vertrektijden()

def spoor(vertrektijd):
    with open('treinplanner.xml', 'r') as treinplannerFile:
        content = xmltodict.parse(treinplannerFile.read())
        for line in content['ReisMogelijkheden']['ReisMogelijkheid']:
            if vertrektijd in line['ActueleVertrekTijd'][11:19]:
                return line['ReisDeel']['ReisStop'][0]['Spoor']['#text']

def aankomst(vertrektijd):
    with open('treinplanner.xml', 'r') as treinplannerFile:
        content = xmltodict.parse(treinplannerFile.read())
        for line in content['ReisMogelijkheden']['ReisMogelijkheid']:
            if vertrektijd in line['ActueleVertrekTijd'][11:19]:
                return line['ActueleAankomstTijd'][11:16]

def reistijd(vertrektijd):
    with open('treinplanner.xml', 'r') as treinplannerFile:
        content = xmltodict.parse(treinplannerFile.read())
        for line in content['ReisMogelijkheden']['ReisMogelijkheid']:
            if vertrektijd in line['ActueleVertrekTijd'][11:19]:
                return line['ActueleReisTijd']

#
# # nu = datetime.now()
# # nu.replace(tzinfo=timezone.utc)
# # print(nu.replace(tzinfo=timezone.utc).isoformat())
# print(vertrektijden())
# print(spoor(vertrektijd))
# print(aankomst(vertrektijd))
# print(reistijd(vertrektijd))








# def request1(eindstation):
#     with open('vertrektijden.xml', 'r') as myXMLFile:
#         content = xmltodict.parse(myXMLFile.read())
#         for line in content['ActueleVertrekTijden']['VertrekkendeTrein']:
#             for key, value in line.items():
#                 if key == 'RouteTekst' or key =='EindBestemming':
#                     if eindstation in value:
#                         value1 = line
#
#     for key, value in value1.items():
#         if key == 'VertrekTijd':
#             print(value[11:19])
#         if key == 'TreinSoort':
#             treinsoort = value
#
#         if key == 'EindBestemming':
#             eindbestemming = value
#
#     print(treinsoort)
#     print(eindbestemming)




