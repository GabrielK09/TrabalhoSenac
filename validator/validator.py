import re

options = (
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "0",
)

def validate_filed(field, value) -> bool:
    match field:
        case "name":
            if value == "":
                return False
            return True
        
        case "category_id":
            if value <= 0:
                return False
            return True
        
        case "category_line":
            if value <= 0:
                return False
            return True
        
        case "unity":
            if value == "":
                return False
            return True
        
        case "cust":
            if value <= 0:
                return False
            return True
        
        case "price":
            if value <= 0:
                return False
            return True
        
        case "amount":
            if value <= 0:
                return False
            return True
        
        case "product_id":
            if value <= 0:
                return False
            return True
        
        case "supplier_id":
            if value <= 0:
                return False
            return True
        
        case "cnpj":
            if value == "":
                return False

            
            elif len(re.sub(r'[^\w\s]', '', value)) > 14:
                return False   
            
            return True

        case "op":
            if value == 0:
                return False
            
            elif value not in options:
                return False
            
            return True
        
        case "main_op":
            if value == 0:
                return False
            
            elif value not in options:
                return False
            
            return True
        
        case "product_op":
            if value == 0:
                return False
            
            elif value not in options:
                return False
            
            return True
        
        case "suppiler_op":
            if value == 0:
                return False
            
            elif value not in options:
                return False
            
            return True
        
        case "category_op":
            if value == 0:
                return False
            
            elif value not in options:
                return False
            
            return True
        
        case "report_op":
            if value == 0:
                return False
            
            elif value not in options:
                return False
            
            return True