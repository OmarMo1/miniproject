import xmltodict, requests

auth_details = ('mohamed.omar@student.hu.nl', 'zQYfnb1XEgH7eMqdfCi6k1rZ-GjRD70Nwy2_GZdSxRiccCrmQCahpQ')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=gouda'
response = requests.get(api_url, auth=auth_details)
#print(response.text)

def openen():
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)

    with open('vertrektijden.xml', 'r') as myXMLFile:
        content = xmltodict.parse(myXMLFile.read())
        for line in content['ActueleVertrekTijden']['VertrekkendeTrein']:
            print(line['RitNummer'])
            print(line['TreinSoort'])
openen()
