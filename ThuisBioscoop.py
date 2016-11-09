"""
Start van het project Thuisbioscoop
Projectgroep 3 klas V1M
"""

import time
import urllib.request
import xmltodict

def openAPI():
    datumVandaag = time.strftime("%d-%m-%Y")
    APIlink = 'http://api.filmtotaal.nl/filmsoptv.xml?apikey=zky5pqtra4entxe7lk3agqqtk8snjgry&dag=' + str(
        datumVandaag) + '&sorteer=0'
    response = urllib.request.urlopen(APIlink).read()
    xmldictionary = xmltodict.parse(response)
    return xmldictionary

filmsVandaag = openAPI()

print(filmsVandaag)
