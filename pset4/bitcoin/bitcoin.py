import sys
import requests
import json

def main():
    bitcoin = get_coin()
    request_coin(bitcoin)

def get_coin():
    #print(sys.argv)
    if len(sys.argv) == 2:
        try:
            if float(sys.argv[1]):
                return sys.argv[1]
        except ValueError:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

def request_coin(coin):
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()
    usd = data["bpi"]["USD"]["rate_float"]
    result = float(usd) * float(coin)
    print(f"${result:,.4f}")

main()
