from product import Product
product=Product("product_name","product_code","product_current_stock","product_sale_price","product_manufacture_cost","product_monthly_production")
print("Welcome to programming principles sample product inventory")
product.setproduct_code(int(input("Please enter the product code: ")))
product.setproduct_name(input("Please enter the product name: "))
product.setproduct_current_stock(int(input("Please enter the product current stock: ")))
product.setproduct_sale_price(float(input("Please enter the product sale price: ")))
product.setproduct_manufacture_cost(float(input("Please enter the product manufacturing cost: ")))
product.setproduct_monthly_production(int(input("Please enter the estimated monthly production: ")))

#to view the monthly units purchased and sold
for month in range(1, 13):
    purchased = int(input(f"Enter units purchased in month {month}: "))
    sold = int(input(f"Enter units sold in month {month}: "))
    product.setunits_purchased_in_month(month, purchased)
    product.setunits_sold_in_month(month, sold)
    
class Application:
    def __init__(self, product):
        self.productObj = product

    def showMenuOptions(self):
        print("1. Enter units manufactured in a month")
        print("2. Enter units sold in a month")
        print("3. View product details")
        print("4. View units manufactured in a month")
        print("5. View units sold in a month")
        print("6. Generate stock statement")
        print("0. Exit")
        choice = int(input("Enter your choice: "))
        return choice
    
    def generate_stock_statement(self):
        while True:
            choice = self.showMenuOptions()
            if choice == 1:
                month = int(input("Enter month number (1-12): "))
                units = int(input("Enter units manufactured: "))
                self.productObj.setunits_purchased_in_month(month, units)
            elif choice == 2:
                month = int(input("Enter month number (1-12): "))
                units = int(input("Enter units sold: "))
                self.productObj.setunits_sold_in_month(month, units)
            elif choice == 3:
                print("Product Details:")
                print(f"Product Code: {self.productObj.getproduct_code()}")
                print(f"Product Name: {self.productObj.getproduct_name()}")
                print(f"Sale Price: ${self.productObj.getproduct_sale_price()}")
                print(f"Manufacture Cost: ${self.productObj.getproduct_manufacture_cost()}")
                print(f"Current Stock: {self.productObj.getproduct_current_stock()}")
            elif choice == 4:
                month = int(input("Enter month number (1-12): "))
                print(f"Units Manufactured in Month {month}: {self.productObj.getunits_purchased_in_month(month)}")
            elif choice == 5:
                month = int(input("Enter month number (1-12): "))
                print(f"Units Sold in Month {month}: {self.productObj.getunits_sold_in_month(month)}")
            elif choice == 6:
                total_units_sold = sum(self.productObj.monthly_units_sold)
                total_units_manufactured = sum(self.productObj.monthly_units_manufactured)
                total_revenue = total_units_sold * self.productObj.getproduct_sale_price()
                total_cost = total_units_manufactured * self.productObj.getproduct_manufacture_cost()
                net_profit = total_revenue - total_cost
                print("Stock Statement:")
                print(f"Product Code: {self.productObj.getproduct_code()}")
                print(f"Product Name: {self.productObj.getproduct_name()}")
                print(f"Total Units Sold: {total_units_sold}")
                print(f"Total Units Manufactured: {total_units_manufactured}")
                print(f"Net Profit: ${net_profit}")
            elif choice == 0:
                print("Exit")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

product = Product("product_name", 0, 0, 0.00, 0.00, 0, 0)
app = Application(product)
app.generate_stock_statement()
 




