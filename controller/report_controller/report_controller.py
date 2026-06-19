products_file_path = 'products.csv'

MIN_STOCK = 3
def get_max_price() -> str:
    with open(products_file_path, 'r') as products:
        is_first_row = True
        max_price = 0
    
        for product in products:
            if is_first_row == True:
                is_first_row = not is_first_row
                continue

            id, name, category, unity, cust, price, amount = product.split("|")

            price = float(price)

            if price > max_price:
                max_price = price            
        print(f"Produto: {id}-{name} tem o maior preço do estoque: R$ {max_price}")

def critical_amount() -> float:
    with open(products_file_path, 'r') as products:
        is_first_row = True
    
        for product in products:
            if is_first_row == True:
                is_first_row = not is_first_row
                continue

        id, name, category, unity, cust, price, amount = product.split("|")

        amount = float(amount)

        if amount <= MIN_STOCK:
            print(f"Produto: {id}-{name} está com quantidade crítica em estoque: {amount}")

def total_in_stock() -> float:
    with open(products_file_path, 'r') as products:
        is_first_row = True
        total_amount_in_stock = 0
        total_price_in_stock = 0
    
        for product in products:
            if is_first_row == True:
                is_first_row = not is_first_row
                continue

        id, name, category, unity, cust, price, amount = product.split("|")

        amount = float(amount)
        cust = float(cust)
        price = float(price)

        total_amount_in_stock += amount
        total_price_in_stock = cust * price
        print("Valor total em estoque: R$", total_price_in_stock)
        print("Quantidade total em estoque: ", total_amount_in_stock)

def report():
    print(15*"----")
    get_max_price()
    critical_amount()
    total_in_stock()
    print(15*"----")