
## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used by creating a Product class that keeps related data, such as productName, price, and quantity, together in one object. These properties can be kept private and accessed or changed through methods such as getPrice(), getQuantity(), and updateStock(). This protects the product data from being changed incorrectly and keeps the program organized.

### 2. Abstraction
Abstraction allows the sari-sari store program to hide complicated details and show only the operations that users need. For example, a Product class may provide an addStock() or sellProduct() method without requiring the user to know exactly how the quantity is updated internally. This makes the system easier to use and reduces unnecessary complexity.

### 3. Inheritance
Inheritance can be used if the store has different types of products that share common information. For example, a general Product class can contain the product name, price, and stock, while classes such as FoodProduct and DrinkProduct can inherit these properties and add their own specific information. This reduces repeated code and makes the program easier to expand.

### 4. Polymorphism
Polymorphism allows different types of products to respond differently to the same method. For example, both FoodProduct and DrinkProduct could have a displayInfo() method, but each class could display its product information in a different way. This allows the inventory system to work with different product types through a common interface while still allowing each type to have its own behavior.

```python
class FoodProduct:
    def display_info(self):
        return "Food product: Canned Goods"
class DrinkProduct:
    def display_info(self):
        return "Drink product: Soft Drink"

def product_info_test(product_object):
    print(product_object.display_info())

product_info_test(FoodProduct())   #Outputs: Food product: Canned Goods
product_info_test(DrinkProduct())  #Outputs: Drink product: Soft Drink
```

## Reflection
Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It keeps important product information such as price and quantity protected inside the Product object and allows changes through controlled methods. This helps prevent incorrect changes to stock and keeps the program organized. Encapsulation also makes the inventory system easier to maintain as the number of products increases.
