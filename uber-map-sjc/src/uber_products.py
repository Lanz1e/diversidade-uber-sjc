# coding=utf-8
from uber_rides.session import Session
from uber_rides.client import UberRidesClient

from config.uber_config import UberToken

session = Session(server_token=UberToken) # Fazer autenticação do APP
client = UberRidesClient(session) # Criar sessão

response = client.get_products(-23.224743, -45.791103)
products = response.json.get('products')
for product in products:
    print product['short_description'],':', product['product_id']
