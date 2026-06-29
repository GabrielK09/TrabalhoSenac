from validator import validator
from controller.category_controller import category_controller

def collect_product_data() -> dict:
    product_data = {}

    name = input("Digite o nome do produto: ")
    while not validator.validate_filed("name", name):
        name = input("Digite o nome do produto: ")

    category_id = int(input("Digite o ID da categoria do produto (digite 0 para não informar): "))

    category_data = None
    if category_id != 0:
        while not validator.validate_filed("category_id", category_id):
            category_id = int(input("Digite o ID da categoria do produto: "))

        category_data = category_controller.find_category(category_id)
        if not validator.validate_filed("category_line", category_data["line"]):
            print("A categoria não existe, confirme se a categoria existe")
            return

    unity = input("Digite a unidade do produto: ")
    while not validator.validate_filed("unity", unity):
        unity = input("Digite a unidade do produto: ")

    cust = float(input("Digite o preço de custo do produto: "))
    while not validator.validate_filed("cust", cust):
        cust = float(input("Digite o preço de custo do produto: "))

    price = float(input("Digite o preço de venda do produto: "))
    while not validator.validate_filed("price", price):
        price = float(input("Digite o preço de venda do produto: "))
    
    while cust > price:
        cust = float(input("Digite o preço de custo do produto: "))
        while not validator.validate_filed("cust", cust):
            cust = float(input("Digite o preço de custo do produto: "))

        price = float(input("Digite o preço de venda do produto: "))
        while not validator.validate_filed("price", price):
            price = float(input("Digite o preço de venda do produto: "))
    
    amount = float(input("Digite a qtde do produto: "))
    while not validator.validate_filed("amount", amount):
        amount = float(input("Digite a qtde do produto: "))

    product_data["name"] = name
    product_data["category"] = category_data["category"].split("|")[1].strip() if category_data != None else "Sem categoria"
    product_data["unity"] = unity
    product_data["cust"] = cust
    product_data["price"] = price
    product_data["amount"] = amount

    return product_data

def collect_category_data() -> dict:
    category_data = {}

    name = input("Digite o nome da categoria: ")
    while not validator.validate_filed("name", name):
        name = input("Digite o nome da categoria: ")

    category_data["name"] = name
    return category_data

def descrontruct_name(data: dict) -> dict:
    new_data = {}
    
    if "product" in data:
        id, name, category, unity, cust, price, amount = data["product"].split("|")                                          
        new_data["id"] = id
        new_data["name"] = name
        new_data["category"] = category
        new_data["unity"] = unity
        new_data["cust"] = cust
        new_data["price"] = price
        new_data["amount"] = amount
    elif "supplier" in data:
        id, name, cnpj, street, city, uf, active = data["supplier"].split("|")
        new_data["id"] = id
        new_data["name"] = name
        new_data["cnpj"] = cnpj
        new_data["street"] = street
        new_data["city"] = city
        new_data["uf"] = uf
    
    return new_data