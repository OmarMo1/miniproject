import xmltodict, requests
from datetime import datetime
from datetime import timezone
import re

beginstation = 'gouda'
eindstation = 'Rotterdam'

def request_vertrektijd(beginstation):
    auth_details = ('mohamed.omar@student.hu.nl', 'zQYfnb1XEgH7eMqdfCi6k1rZ-GjRD70Nwy2_GZdSxRiccCrmQCahpQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + beginstation
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as vertrekFile:
        vertrekFile.write(response.text)

    auth_details = ('mohamed.omar@student.hu.nl', 'zQYfnb1XEgH7eMqdfCi6k1rZ-GjRD70Nwy2_GZdSxRiccCrmQCahpQ')
    api_url = 'http://webservices.ns.nl/ns-api-storingen?station=' + beginstation
    response = requests.get(api_url, auth=auth_details)
    with open('storingen.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)

def request(beginstation, eindstation):
    auth_details = ('mohamed.omar@student.hu.nl', 'zQYfnb1XEgH7eMqdfCi6k1rZ-GjRD70Nwy2_GZdSxRiccCrmQCahpQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + beginstation
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as vertrekFile:
        vertrekFile.write(response.text)

    auth_detailss = ('mohamed.omar@student.hu.nl', 'zQYfnb1XEgH7eMqdfCi6k1rZ-GjRD70Nwy2_GZdSxRiccCrmQCahpQ')
    api_urls = 'http://webservices.ns.nl/ns-api-treinplanner?fromStation='+beginstation+'&toStation='+eindstation
    response = requests.get(api_urls, auth=auth_detailss)
    with open('treinplanner.xml', 'w') as treinplannerFile:
        treinplannerFile.write(response.text)

request(beginstation, eindstation)
request_vertrektijd(beginstation)

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
                x = line['ReisDeel']
                if isinstance(x, dict):
                    return x['ReisStop'][0]['Spoor']['#text']
                elif isinstance(x, list):
                    return x[0]['ReisStop'][0]['Spoor']['#text']




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

def wijzigingspoor(vertrektijd):
    with open('treinplanner.xml', 'r') as treinplannerFile:
        content = xmltodict.parse(treinplannerFile.read())
        for line in content['ReisMogelijkheden']['ReisMogelijkheid']:
            if vertrektijd in line['ActueleVertrekTijd'][11:19]:
                x = line['ReisDeel']
                return x['ReisStop'][0]['Spoor']['@wijziging']


def status(vertrektijd):
    with open('treinplanner.xml', 'r') as treinplannerFile:
        content = xmltodict.parse(treinplannerFile.read())
        for line in content['ReisMogelijkheden']['ReisMogelijkheid']:
            if vertrektijd in line['ActueleVertrekTijd'][11:19]:
                return line['Status']

def naam_beginstation(vertrektijd):
    with open('treinplanner.xml', 'r') as treinplannerFile:
        content = xmltodict.parse(treinplannerFile.read())
        for line in content['ReisMogelijkheden']['ReisMogelijkheid']:
            if vertrektijd in line['ActueleVertrekTijd'][11:19]:
                x = line['ReisDeel']
                if isinstance(x, dict):
                    return x['ReisStop'][0]['Naam']
                elif isinstance(x, list):

                    return x[0]['ReisStop'][0]['Naam']

def storing():
    with open('storingen.xml', 'r') as storingenFile:
        content = xmltodict.parse(storingenFile.read())
        data = ''
        if content['Storingen']['Ongepland']:
            try:
                if content['Storingen']['Ongepland']['Storing']:
                    for line in content['Storingen']['Ongepland']['Storing']:
                        data += 'Reden: '+line['Reden']+'\n'+line['Bericht']+'\n'
                    return data
            except TypeError:
                data = content['Storingen']['Ongepland']['Storing']['Bericht']
                return data

        else:
            data = 'Er zijn geen ongeplande storingen'
            return data




data = storing()


def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)


# print(striphtml(data))
