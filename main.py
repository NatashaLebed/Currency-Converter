import requests
import json

currency = input().lower()
r = requests.get('http://www.floatrates.com/daily/' + currency + '.json')
curr_rates = json.loads(r.content)

cache = {}
if "usd" in curr_rates:
    cache["usd"] = curr_rates["usd"]["rate"]
if "eur" in curr_rates:
    cache["eur"] = curr_rates["eur"]["rate"]

while True:
    curr_receive = input().lower()
    if curr_receive == '':
        break

    money = float(input())
    print("Checking the cache...")
    if curr_receive in cache:
        print('Oh! It is in the cache!')
    else:
        print("Sorry, but it is not in the cache!")
        cache[curr_receive] = curr_rates[curr_receive]["rate"]

    x = money * cache[curr_receive]
    print(f'You received {x} {curr_receive.upper()}.')
