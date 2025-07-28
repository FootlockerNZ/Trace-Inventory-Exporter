import requests
import csv
import random
import json
import sys
from datetime import datetime



def getConfig():
    print('Geting config...')

    try:
        file = open('config.json')
        config = json.loads(file.read())
        file.close()
        return config
    except Exception as e:
        print('Failed to load config. Error: '+str(e))
        input()
        sys.exit()


def login():
    print('Logging in...')
    
    params = {
        'key': 'AIzaSyBH1NS5RuSMLekpp-SUrQCVa-cDbErzpo4',
    }

    json_data = {
        'email': config['email'],
        'password': config['password'],
        'returnSecureToken': True,
        'tenantId': storeId,
    }

    response = requests.post(
        'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword',
        params=params,
        headers=HEADERS,
        json=json_data,
    )

    return response.json()['idToken']

def getId():
    print('Getting auth...')

    params = {
        'key': 'AIzaSyBH1NS5RuSMLekpp-SUrQCVa-cDbErzpo4',
    }

    json_data = {
        'idToken': idToken,
    }

    r = requests.post(
        'https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo',
        params=params,
        headers=HEADERS,
        json=json_data,
    )

    return r.json()['users'][0]['localId']


def getAccount():
    print('Getting account...')

    r = requests.get(
        'https://fulltrace-server.onrender.com/api/consigners/UcLYhTOHNvWa8BJPCkdL0wofo892',
        headers=HEADERS
    )
    
    return str(r.json()['data']['id'])



def getInventory():
    print("Getting inventory...")

    params = {
        'printed': '',
        'status': '',
        'option1Value': 'undefined',
        'option2Value': 'undefined',
        'option3Value': 'undefined',
        'category': '',
        'consigner': consignerId,
        'sortOption': 'newestUpdated',
        'location': '',
        'search': '',
    }

    r = requests.get(
        'https://fulltrace-server.onrender.com/api/inventories', 
        params=params, 
        headers=HEADERS
    )

    return r.json()['data']['inventories']
    

def writeFile():
    current_date = datetime.now().strftime('%Y-%m-%d')
    file_name = f'History/{str(random.randint(0,999))}-{store}-inventory-{current_date}.csv'
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['status', 'title', 'size', 'price'])
        for i in inventory:
            writer.writerow([i['status'], i['product']['title'], i['option1Value'], i['price']])

    print(f"Inventory written to: {file_name.split('\\')[-1]}")




config = getConfig()


TENANTS = [
    {"store": "imyourwardrobe.com", "id": "ImYourWardrobe-oq9h0"},
    {"store": "cjkicksnz.com", "id": "cjkicks-h9zbu"},
    {"store": "kickitnz.com", "id": "kickitnz-3b4oy"},
    {"store": "basement.nz", "id": "andrew-33oy2"},
    {"store": "priorstoreofficial.com", "id": "Prior-nzuut"},
    {"store": "bigboisneakers.com", "id":"bigdawg-jeec0"}
]


while True:
    HEADERS = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }

    print()
    print()
    print('Select store to export consignment inventory')
    print('--------------------------------------------')
    print()

    for i in range(len(TENANTS)):
        print(f'[{str(i+1)}] {TENANTS[i]['store']}')

    print()
    option = int(input('Enter store number (e.g 1 = imyourwardrobe.com): '))
    store = TENANTS[option-1]['store']
    storeId = TENANTS[option-1]['id']
    print()
    print()

    print(f'Getting inventory for store: {store}...')

    idToken = login()
    HEADERS['authorization'] = 'Bearer '+ idToken
    localId = getId()
    consignerId = getAccount()
    inventory = getInventory()
    writeFile()

