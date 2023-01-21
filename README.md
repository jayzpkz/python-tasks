# Price Check

There is a shop with old-style cash registers. Rather than scanning items and pulling the price from a <br>
database, the price of each item is typed in manually. This method sometimes leads to errors. Given a <br>
list of items and their correct prices, compare the prices to those entered when each item was sold. <br>
Determine the number of errors in selling prices.

### Example

<code>
products = ['eggs', 'milk', 'cheese']
productPrices = [2.89, 3.29, 5.79]
productSold = ['eggs', 'eggs', 'cheese', 'milk']
soldPrice = [2.89, 2.99, 5.97, 3.29]
</code>

![image](https://user-images.githubusercontent.com/57365299/213872349-ed26d5c0-9241-41d0-955f-4f07490bae9a.png)

The second sale of eggs has a wrong price, as does the sale of cheese. There are 2 errors in pricing.

### Function Description

Write the body of the function `priceCheck` and the test for this function in one of the recommended
languages.
The function should have the following parameters: <br>
● string products[n]: each products[i] is the name of an item for sale <br>
● string productPrices[n]: each productPrices[i] is the price of products[i] <br>
● string productSold[m]: each productSold[j] is the name of a product sold <br>
● float soldPrice[m]: each soldPrice[j] contains the sale price recorded for productSold[j]. <br>
and return: <br>
● int: the number of sale prices that were entered incorrectly <br>

### Constraints

● 1 ≤ n ≤ 99 <br>
● 1 ≤ m ≤ 99 <br>
● productPrices[i] ∈ products[n], where 0 ≤ i < m <br>
● 1.00 ≤ productPrices[i], soldPrice[j] ≤ 100000.00, where 0 ≤ i < n, and 0 ≤ j < m

### Example of Function Call

<code>
priceCheck(
products=['rice', 'sugar', 'wheat', 'cheese'],
productPrices=[16.89, 56.92, 20.89, 345.99],
productSold=['rice', 'cheese'],
soldPrice=[18.99, 400.89]
) => 2
</code>

The sales of rice and cheese were at the wrong prices. So, the number of sale prices that were entered
incorrectly is 2:

![image](https://user-images.githubusercontent.com/57365299/213872467-6013a131-74df-4d52-b3d8-483a9ec0a582.png)


