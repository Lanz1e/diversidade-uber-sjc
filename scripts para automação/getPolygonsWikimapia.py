# -*- coding: utf-8 -*-
#rodar c py2
import urllib
import requests

key = 'AQUI VAI A SUA KEY DO WIKIMAPIA, HERE GOES YOUR WIKIMAPIA API KEY'

while 1==1:
    text2=raw_input('Nome: ')
    text=str(input('ID: '))
    '''response = urllib.urlretrieve('http://api.wikimapia.org/?function=object&id='+text+'&key='+key+'&format=kml',''+text2+'.kml')
    result = requests.get('http://api.wikimapia.org/?function=object&id='+text+'&key='+key+'&format=kml')
    print result.content'''

    url = 'http://api.wikimapia.org/?function=object&id='+text+'&key='+key+'&format=kml'
    response = requests.get(url)
    print(response.content)
    if response.status_code == 200:
        with open(text2+'.kml', 'wb') as f:
            f.write(response.content)
            
    print('--------------------------------------------------------------------------------------')
    print('copiado')
