from helpers import helpers

file_path = 'categories.csv'

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
    
def save_in_file(product: str) -> None:
    with open(file_path, 'a') as file:
        file.write(product  + "\n")

    print("Categoria cadastrada com sucesso!")
    
def build_category(id, name) -> str:
    return f"{id}|{name}"

def get_all():
    print("Lista de categorias")
    with open(file_path, 'r') as categories:
        is_first_row = True
        for category in categories:
            if is_first_row == True:
                is_first_row = not is_first_row
                continue
            
            id, name = category.split("|")
            
            print(build_category(id, name))
    
def find_category(category_id: int) -> dict:
    with open(file_path, 'r') as file:
        is_first_row = True
    
        for i, line in enumerate(file):
            if is_first_row == True:
                is_first_row = not is_first_row
                continue
            
            id, name = line.split("|")

            if int(id) == category_id:    
                return {"line": i, "category": build_category(id, name)}

        return {"line": 0, "category": None}

def register_new_category():
    collected_category_data = helpers.collect_category_data()

    save_in_file(
        build_category(
            generate_code(), 
            collected_category_data["name"]
        )
    )