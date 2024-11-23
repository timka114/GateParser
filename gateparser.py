import json
import requests
import time

host = "https://api.gateio.ws"
prefix = "/api/v4"
headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

url = '/spot/tickers'

query_param = 'currency_pair=BTC_USDT'
query_param2 = 'currency_pair=ETH_USDT'
query_param3 = 'currency_pair=SOL_USDT'

last_BTC_price = 0
last_ETH_price = 0
last_SOL_price = 0
while True:
    r = requests.get(host + prefix + url + "?" + query_param, headers=headers)
    r2 = requests.get(host + prefix + url + "?" + query_param2, headers=headers)
    r3 = requests.get(host + prefix + url + "?" + query_param3, headers=headers)
    try:
        r.raise_for_status()
        if r.status_code == 200:

            BTC_data = r.json()[0]
            ETH_data = r2.json()[0]
            SOL_data = r3.json()[0]

            # BTC
            BTC_name = BTC_data['currency_pair']
            BTC_price = BTC_data['last']

            if BTC_price != last_BTC_price:
                last_BTC_price = BTC_price
                print(f"{BTC_name} {BTC_price}")
            
            # ETH
            ETH_name = ETH_data['currency_pair']
            ETH_price = ETH_data['last']

            if ETH_price != last_ETH_price:
                last_ETH_price = ETH_price
                print(f"{ETH_name} {ETH_price}")
            
            # SOL
            SOL_name = SOL_data['currency_pair']
            SOL_price = SOL_data['last']

            if SOL_price != last_SOL_price:
                last_SOL_price = SOL_price
                print(f"{SOL_name} {SOL_price}")
        
        
        elif r.status_code == 429:
            print("Превышен лимит запросов к API GATE")
        else:
            print(f"Ошибка: статус-код {r.status_code}")
        time.sleep(2)
    except requests.HTTPError as error:
        print(f"Произошла ошибка {error}")
    print("\n")


