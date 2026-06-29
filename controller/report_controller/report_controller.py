productsfpath = 'products.csv'
movementsfpath = 'movements.csv'
#-----------------------------------------------------------------------
def stockcheck():
    with open(productsfpath, 'r', encoding="cp1252") as file:
        for line in file.readlines()[1:]:
            divide = line.strip().split('|')
            divideT = float(divide[6])
            product = divide[1]
            if divideT <= 5:

                print(f'{product} está com estoque baixo, cuidado!')
#-----------------------------------------------------------------------
def stockplus():
    total_cost_value = 0.0
    total_sale_value = 0.0
    with open(productsfpath, 'r', encoding="cp1252") as file:
        for line in file.readlines()[1:]:
            divide = line.strip().split('|')
            cost_value = float(divide[4])
            sale_value = float(divide[5])
            total_cost_value += cost_value
            total_sale_value += sale_value

        print(f'valor avaliado total do estoque com base no preço de custo: {total_cost_value}')
        print(f'valor avaliado total do estoque com base no preço de venda: {total_sale_value}')
        print(f'valor avaliado total do estoque com base nos valores a cima somados: {total_cost_value + total_sale_value}')
#-----------------------------------------------------------------------
def mvp():
    product = []
    products_cost = []
    products_sale = []
    with open(productsfpath, 'r', encoding="cp1252") as file:
        for line in file.readlines()[1:]:
            divide = line.strip().split('|')
            product.append(divide[1])
            products_cost.append(float(divide[4]))
            products_sale.append(float(divide[5]))
            maxps = max(products_sale)
            maxpc = max(products_cost)
            products_name_sale = product[products_sale.index(maxps)]
            products_name_cost = product[products_cost.index(maxpc)]

        print(f'Produto com maior valor de venda: {products_name_sale} - R${max(products_sale)}')
        print(f'Produto com maior valor de custo: {products_name_cost} - R${max(products_cost)}')

#-----------------------------------------------------------------------
def report_movements_by_category() -> None:
    product_category = {}
    with open(productsfpath, 'r', encoding="cp1252") as products:
        is_first_row = True

        for product in products:
            if is_first_row == True:
                is_first_row = not is_first_row
                continue

            id, name, category, unity, cust, price, amount = product.split("|")
            product_category[id] = category

    report = {}

    with open('movements.csv', 'r', encoding="cp1252") as movements:
        for movement in movements:
            movement = movement.strip()
            if not movement:
                continue

            label, supplier_info, product_info, amount, value, date = movement.split("|")

            product_id = product_info.split("-")[0]
            amount = float(amount)
            value = float(value.replace("R$", ""))

            category = product_category.get(product_id, "sem categoria")

            if category not in report:
                report[category] = {
                    "entry_value": 0, "expense_value": 0,
                    "entry_amount": 0, "expense_amount": 0
                }

            if label == "Entrada":
                report[category]["entry_value"] += value
                report[category]["entry_amount"] += amount
            else:
                report[category]["expense_value"] += value
                report[category]["expense_amount"] += amount

    print("Relatório de Entradas e Saídas por Categoria")
    for category, data in report.items():
        print(f"Categoria: {category}")
        print(f"  Entradas: {data['entry_amount']:.0f} unidades")
        print(f"  Saídas:   R$ {data['expense_value']:.2f}  |  {data['expense_amount']:.0f} unidades")
        print()
#-----------------------------------------------------------------------
def report_movements():
    with open(movementsfpath, 'r', encoding="cp1252") as file:
        for line in file.readlines():
            line = line.strip()
            if not line:
                continue
            else:

                print(line)