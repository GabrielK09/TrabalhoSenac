from validator import validator
from controller.supplier_controller.req_api import *
from brutils import format_cnpj

file_path = 'supplier.csv'

def generate_code() -> int:
    with open(file_path, 'r', encoding="cp1252") as file:
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
    return f"{code}|{name}|{cnpj}|{street}|{city}|{uf}"

def save_in_file(product: str) -> None:
    with open(file_path, 'a', encoding="cp1252") as file:
        file.write(product  + "\n")

    print("Fornecedor cadastrado com sucesso!")

def find_supplier(supplier_id: int) -> dict:
    with open(file_path, 'r', encoding="cp1252") as file:
        is_first_row = True
    
        for i, line in enumerate(file):
            if is_first_row == True:
                is_first_row = not is_first_row
                continue
            
            id, name, cnpj, street, city, uf = line.split("|")

            if int(id) == supplier_id:    
                return {"line": i, "supplier": build_supplier(id, name, cnpj, street, city, uf)}

        return {"line": 0, "supplier": None}
    
def register_new_supplier():
    cnpj = input("Digite o CNPJ do fornecedor: ")

    while not validator.validate_filed("cnpj", cnpj):
        cnpj = input("Digite o CNPJ do fornecedor: ")

    data = fetch_cnpj(cnpj)
    cnpj = format_cnpj(re.sub(r'[^\w\s]', '', cnpj))

    if data["alias"] == None:
        data["alias"] = data["company"]["name"]

    address = None
    if data["address"] == None:
        address["address"]["street"] = "Não informado"
        address["address"]["city"] = "Não informado"
        address["address"]["state"] = "Não informado"
    else:
        address = data["address"]

    save_in_file(build_supplier(generate_code(), data["alias"], cnpj, address["street"], address["city"], address["state"]))

def get_all():
    print("Lista de fornecedores")
    with open(file_path, 'r', encoding="cp1252") as suppliers:
        is_first_row = True
        for supplier in suppliers:
            if is_first_row == True:
                print(supplier)
                is_first_row = not is_first_row
                continue
            
            id, name, cnpj, street, city, uf = supplier.split("|")
            
            print(build_supplier(id, name, cnpj, street, city, uf))