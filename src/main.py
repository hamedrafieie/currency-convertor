import requests


def get_exchange_rate(base_currnecy, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/597b977f4e7a3ca4a8a633e1/latest/{base_currnecy}"
    response = requests.get(url)
    rate = response.json()['conversion_rates'][target_currency]
    return rate

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

