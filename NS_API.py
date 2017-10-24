import xmltodict, requests

# beginstation = 'gouda'
eindstation = 'Utrecht'

#print(response.text)

def request(beginstation):
    auth_details = ('mohamed.omar@student.hu.nl', 'zQYfnb1XEgH7eMqdfCi6k1rZ-GjRD70Nwy2_GZdSxRiccCrmQCahpQ')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + beginstation
    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)

with open('vertrektijden.xml', 'r') as myXMLFile:
    content = xmltodict.parse(myXMLFile.read())
    for line in content['ActueleVertrekTijden']['VertrekkendeTrein']:
        for key, value in line.items():
            if key == 'RouteTekst' or key =='EindBestemming':
                if eindstation in value:
                    value1= line
    print(value1)

request(beginstation='gouda')
