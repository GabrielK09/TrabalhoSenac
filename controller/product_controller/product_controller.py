from validator import validator
from controller.supplier_controller import supplier_controller
from helpers import helpers
from datetime import datetime

import math

file_path = 'products.csv'

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
    
def build_product(id, name, category, unity, cust, price, amount) -> str:
    return f"{id}|{name}|{category}|{unity}|{cust}|{price}|{amount}"

def save_in_file(product: str) -> None:
    with open(file_path, 'a') as file:
        file.write(product  + "\n")

    print("Produto cadastrado com sucesso!")

def find_product(product_id: int) -> dict:
    with open(file_path, 'r') as file:
        is_first_row = True
    
        for i, line in enumerate(file):
            if is_first_row == True:
                is_first_row = not is_first_row
                continue
            
            id, name, category, unity, cust, price, amount = line.split("|")

            if int(id) == product_id:    
                return {"line": i, "product": build_product(id, name, category, unity, cust, price, amount)}

        return {"line": 0, "product": None}

def register_new_product():
    collected_product_data = helpers.collect_product_data()

    save_in_file(
        build_product(
            generate_code(), 
            collected_product_data["name"], 
            collected_product_data["category"], 
            collected_product_data["unity"], 
            collected_product_data["cust"], 
            collected_product_data["price"], 
            collected_product_data["amount"]
        )
    )

def handle_update():
    print(15*"----")
    get_all()
    print(15*"----")
    
    product_id = int(input("Digite o código do produto: "))

    while not validator.validate_filed("product_id", product_id):
        product_id = int(input("Digite o código do produto: "))

    product_data = find_product(product_id)

    if product_data["line"] == 0:
        print("Produto não localizado")

    descrontructed_product_name = helpers.descrontruct_name(product_data)

    collected_product_data = helpers.collect_product_data()

    product = build_product(
        descrontructed_product_name["id"],
        collected_product_data["name"], 
        collected_product_data["category"], 
        collected_product_data["unity"], 
        collected_product_data["cust"], 
        collected_product_data["price"], 
        collected_product_data["amount"]
    )
    
    update_product(product, product_data["line"])

def update_product(product: str, line: int):
    with open(file_path, 'r') as file:
        lines =  file.readlines()

    lines[line] = product + "\n"

    with open(file_path, 'w') as file:
        file.writelines(lines)

    print("Produto alterado com sucesso!")

def register_movement(movement_type: str):
    print(movement_type)
    print(15*"----")
    supplier_controller.get_all()
    print(15*"----")

    supplier_id = int(input("Digite o código do fornecedor: "))
    while not validator.validate_filed("supplier_id", supplier_id):
        supplier_id = int(input("Digite o código do fornecedor: "))

    supplier_data = supplier_controller.find_supplier(supplier_id)

    if supplier_data["line"] == 0:
        print("Fornecedor não localizado")
        return
    
    descrontructed_supplier_name = helpers.descrontruct_name(supplier_data)

    print(15*"----")
    get_all()
    print(15*"----")

    product_id = int(input("Digite o código do produto: "))
    while not validator.validate_filed("product_id", product_id):
        product_id = int(input("Digite o código do produto: "))

    product_data = find_product(product_id)

    if product_data["line"] == 0:
        print("Produto não localizado")
        return

    amount = float(input(f"Digite a qtde {'entrada' if movement_type == 'entry' else 'saída'} do produto: "))

    while not validator.validate_filed("amount", amount):
        amount = float(input("Digite a qtde saída do produto: "))

    if movement_type != 'entry':
        price = float(input(f"Digite o valor da {'entrada' if movement_type == 'entry' else 'saída'} do produto: "))
        while not validator.validate_filed("price", price):
            price = float(input(f"Digite o valor da {'entrada' if movement_type == 'entry' else 'saída'} do produto: "))

    # id|name|category|unity|cust|price|amount
    descrontructed_product_name = helpers.descrontruct_name(product_data)
    
    new_amount = 0
     
    match movement_type:
        case 'entry':
            new_amount = float(descrontructed_product_name["amount"]) + amount

        case 'expense':
            new_amount = float(descrontructed_product_name["amount"]) - amount
        
        case _:
            new_amount = amount

    product = build_product(
        descrontructed_product_name["id"],
        descrontructed_product_name["name"],
        descrontructed_product_name["category"],
        descrontructed_product_name["unity"],
        descrontructed_product_name["cust"],
        descrontructed_product_name["price"],
        new_amount
    )

    update_product(product, product_data["line"])    

    date_movement = datetime.now()

    label = "Entrada" if movement_type == 'entry' else "Saída"
    register = f"{label}|{descrontructed_supplier_name["id"]}-{descrontructed_supplier_name["name"]}|{descrontructed_product_name["id"]}-{descrontructed_product_name["name"]}|{amount}" + f"|R${math.ceil(float(amount) * price)}"+ f"|{date_movement}"

    with open('movements.csv', 'a') as movements: 
        movements.write(register)
    
    print("Movimentação cadastrada com sucesso!")

def get_all():
    print("Lista de produtos")
    with open(file_path, 'r') as products:
        is_first_row = True
        for product in products:
            if is_first_row == True:
                is_first_row = not is_first_row
                continue
            
            id, name, category, unity, cust, price, amount = product.split("|")
            
            print(build_product(id, name, category, unity, cust, price, amount))
    