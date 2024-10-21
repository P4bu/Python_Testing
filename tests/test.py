# Codigo que ira a produccion
def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0

def calculate_total_with_single_product():
    products = [
        {
            'name': 'notebook',
            'price': 5
        }
    ]
    assert calculate_total(products) == 5   

def calculate_total_with_multiple_product():
    products = [
        {
            'name': 'notebook',
            'price': 20
        },
        {
            'name': 'pantalla',
            'price': 15
        },
        {
            'name': 'mouse',
            'price': 10
        }
    ]
    assert calculate_total(products) == 45
    print('Pasa la prueba')   

if __name__ == '__main__':
    test_calculate_total_with_empty_list()
    calculate_total_with_single_product()
    calculate_total_with_multiple_product()