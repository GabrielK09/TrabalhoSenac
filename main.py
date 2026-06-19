from validator import validator
from controller.product_controller import product_controller
from controller.supplier_controller import supplier_controller
from controller.category_controller import category_controller
from controller.report_controller import report_controller

def main():
    running = True

    while running:
        print(15*"----")
        print("1 - Produtos")
        print("2 - Fornecedores")
        print("3 - Categorias")
        print("4 - Relatórios")
        print("0 - Sair")
        main_op = input("")

        while not validator.validate_filed("main_op", main_op): 
            main_op = input("Selecione uma opção: ") 
        
        match main_op:
            case "1":
                while True:
                    print("1 - Registar novo produto")
                    print("2 - Listar produtos")
                    print("3 - Editar produto")
                    print("4 - Registrar saída produto")
                    print("5 - Registrar entrada produto")
                    print("0 - Sair")
                    product_op = input("")

                    while not validator.validate_filed("product_op", product_op): 
                        product_op = input("Selecione uma opção: ") 

                    match product_op:
                        case "1":
                            product_controller.register_new_product()

                        case "2":
                            product_controller.get_all()
                            
                        case "3":
                            product_controller.handle_update()

                        case "4":
                            product_controller.register_movement('expense')

                        case "5":
                            product_controller.register_movement('entry')

                        case "6":
                            supplier_controller.register_new_supplier()
                            
                        case "0":
                            print("Voltando ...")
                            break

            case "2":
                while True:
                    print("1 - Listar fornecedores")      
                    print("2 - Registrar fornecedor")      
                    print("0 - Voltar")
                    suppiler_op = input("")

                    while not validator.validate_filed("suppiler_op", suppiler_op): 
                        suppiler_op = input("Selecione uma opção: ") 

                    match suppiler_op:
                        case "1":
                            print(15*"----")
                            supplier_controller.get_all()
                            print(15*"----")

                        case "2":
                            supplier_controller.register_new_supplier()

                        case "0":
                            print("Voltando ...")
                            break

            case "3":
                while True:
                    print("1 - Registrar categoria")
                    print("2 - Registrar categoria")
                    print("0 - Voltar")
                    category_op = input("")

                    while not validator.validate_filed("category_op", category_op): 
                        category_op = input("Selecione uma opção: ") 

                    match category_op:
                        case "1":
                            print(15*"----")
                            category_controller.get_all()
                            print(15*"----")

                        case "2":
                            category_controller.register_new_category()

                        case "0":
                            print("Voltando ...")
                            break
            case "4":
                report_controller.report()

if __name__ == "__main__":
    main()