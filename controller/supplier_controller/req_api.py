import requests

def fetch_cnpj(cnpj: str) -> dict:
    return requests.get(f"https://open.cnpja.com/office/{cnpj}").json()    