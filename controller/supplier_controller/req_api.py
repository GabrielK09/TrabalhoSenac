import requests
import re

def fetch_cnpj(cnpj: str) -> dict:
    cnpj = re.sub(r'[^\w\s]', '', cnpj)

    return requests.get(f"https://open.cnpja.com/office/{cnpj}").json()    