from price_checker import priceCheck
import pytest

def test_priceCheck_few_wrong_prices():
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese']
    soldPrice = [18.99, 400.89]

    testResult = priceCheck(products, productPrices, productSold, soldPrice)
    assert(testResult == 2)
    
def test_priceCheck_one_wrong_price():
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese']
    soldPrice = [16.89, 400.89]

    testResult = priceCheck(products, productPrices, productSold, soldPrice)
    assert(testResult == 1)
    
def test_priceCheck_no_wrong_prices():
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese']
    soldPrice = [16.89, 345.99]

    testResult = priceCheck(products, productPrices, productSold, soldPrice)
    assert(testResult == 0)
    
def test_priceCheck_products_does_not_contain_sold_product():
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese', 'salt']
    soldPrice = [16.89, 345.99, 50.12]

    with pytest.raises(ValueError):
        priceCheck(products, productPrices, productSold, soldPrice)
        
def test_priceCheck_one_pair_of_lists_lengths_is_not_equal():
    # first pair
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [16.89, 56.92, 20.89, 345.99]
    # second pair
    productSold = ['rice', 'cheese']
    soldPrice = [16.89, 345.99, 50.12]

    with pytest.raises(ValueError):
        priceCheck(products, productPrices, productSold, soldPrice)
        
def test_priceCheck_one_or_more_of_the_arguments_length_is_zero():
    products = []
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese']
    soldPrice = [16.89, 345.99]

    with pytest.raises(ValueError):
        priceCheck(products, productPrices, productSold, soldPrice)
        
def test_priceCheck_one_or_more_of_the_arguments_is_not_list():
    products = None
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese']
    soldPrice = [16.89, 345.99]

    with pytest.raises(TypeError):
        priceCheck(products, productPrices, productSold, soldPrice)
        
def test_priceCheck_one_or_more_of_the_arguments_length_overflows():
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = []
    for i in range(100):
        productPrices.append("string");
    productSold = ['rice', 'cheese']
    soldPrice = [16.89, 345.99]

    with pytest.raises(OverflowError):
        priceCheck(products, productPrices, productSold, soldPrice)
        
def test_priceCheck_product_prices_less_than_one():
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [1, 0.99, 1, 1]
    productSold = ['rice', 'cheese']
    soldPrice = [18.99, 400.89]

    with pytest.raises(ValueError):
        priceCheck(products, productPrices, productSold, soldPrice)
        
def test_priceCheck_sold_price_greater_than_100_000():
    products = ['rice', 'sugar', 'wheat', 'cheese']
    productPrices = [16.89, 56.92, 20.89, 345.99]
    productSold = ['rice', 'cheese']
    soldPrice = [180000.99, 400.89]

    with pytest.raises(ValueError):
        priceCheck(products, productPrices, productSold, soldPrice)
        