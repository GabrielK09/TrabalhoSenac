from validator import validator
from controller.supplier_controller.req_api import *

file_path = 'supplier.csv'

def generate_code() -> int:
    with open(file_path, 'r') as file:
        is_first_row = True
        last_code = 0

        for line in file:
            if is_first_row == True:
                is_first_row = not is_first_row
                continue

            data = line.split("|")

            last_code = data[0]

        return int(last_code) + 1
    
def build_supplier(code, name, cnpj, street, city, uf) -> str:
    return f"{code}|{name}|{cnpj}|{street}|{city}|{uf}|{True}"

def save_in_file(product: str) -> None:
    with open(file_path, 'a') as file:
        file.write(product  + "\n")

    print("Fornecedor cadastrado com sucesso!")

def find_supplier(supplier_id: int) -> dict:
    with open(file_path, 'r') as file:
        is_first_row = True
    
        for i, line in enumerate(file):
            if is_first_row == True:
                is_first_row = not is_first_row
                continue
            
            id, name, cnpj, street, city, uf, active = line.split("|")

            if int(id) == supplier_id:    
                return {"line": i, "supplier": build_supplier(id, name, cnpj, street, city, uf)}

        return {"line": 0, "supplier": None}
    
def register_new_supplier():
    cnpj = input("Digite o CNPJ do fornecedor: ")
    while not validator.validate_filed("cnpj", cnpj):
        cnpj = input("Digite o CNPJ do fornecedor: ")

    data = fetch_cnpj(cnpj)

    address = data["address"]
    save_in_file(build_supplier(generate_code(), data["alias"], cnpj, address["street"], address["city"], address["state"]))

def get_all():
    print("Lista de fornecedores")
    with open(file_path, 'r') as suppliers:
        is_first_row = True
        for supplier in suppliers:
            if is_first_row == True:
                is_first_row = not is_first_row
                continue
            
            id, name, cnpj, street, city, uf, active = supplier.split("|")
            
            print(build_supplier(id, name, cnpj, street, city, uf))