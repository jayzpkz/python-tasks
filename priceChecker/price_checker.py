from typing import List

def priceCheck(products: List[str], productPrices: List[float], productSold: List[str], soldPrice: List[float]):
    '''
    There is a shop with old-style cash registers. Rather than scanning items and pulling the price from a
    database, the price of each item is typed in manually. This method sometimes leads to errors. Given a
    list of items and their correct prices, compare the prices to those entered when each item was sold.
    Determine the number of errors in selling prices
    '''
    if type(products) is not list or type(productPrices) is not list or type(productSold) is not list or type(soldPrice) is not list:
        raise TypeError("All passed arguments must be of type list")
    
    if len(products) == 0 or len(productPrices) == 0 or len(productSold) == 0 or len(soldPrice) == 0:
        raise ValueError("One or more of the passed arguments must contain at least one element")
    
    if len(products) > 99 or len(productPrices) > 99 or len(productSold) > 99 or len(soldPrice) > 99:
        raise OverflowError("One or more of the passed arguments must contain too many elements")
    
    if len(products) != len(productPrices) or len(productSold) != len(soldPrice):
        raise ValueError("One or more of the following pair of lists does not have equal number of elements: products and productPrices or productSold and soldPrice")
    
    for product in productSold:
        if product not in products:
            raise ValueError("It is not possible to sell a product that does not exist in the products list")
    
    for price in productPrices:
        if price < 1.0:
            raise ValueError("product price must be at least 1.0")
        
    for price in soldPrice:
        if price > 100000.0:
            raise ValueError("product price can not be greater than 100,000.00")
     
    errors = []
    
    for n in range(len(products)):
        currentProduct = products[n]
        productTypeSaleNum = 0
        for m in range(len(productSold)):
            currentSoldProduct = productSold[m]
            if(currentProduct == currentSoldProduct):
                productTypeSaleNum += 1
                if(productPrices[n] != soldPrice[m]):
                    saleError = (currentSoldProduct, soldPrice[m], productTypeSaleNum)
                    errors.append(saleError)
                    
    result = len(errors)
    
    # in case prints are needed
    # ---- start ----
    if(result == 0):
        print("All sales were at the correct prices.");
    elif(result == 1):
        print("The sale of " + errors[0][0] + " was at the wrong price. So, the number of sale prices that were entered incorrectly is: 1");
    elif(result > 1):
        items = []
        for item in errors:
            items.append(item[0])
        productsToPrint = " and ".join(items);
        print("The sales of " + productsToPrint + " were at the wrong prices. So, the number of sale prices that were entered incorrectly is: " + str(len(errors)));
    # ---- end ----
                    
    return result

# testing the prints
products = ['rice', 'sugar', 'wheat', 'cheese']
productPrices = [16.89, 56.92, 20.89, 345.99]
productSold = ['rice', 'cheese']
soldPrice = [18.99, 400.89]

testResult = priceCheck(products, productPrices, productSold, soldPrice)
