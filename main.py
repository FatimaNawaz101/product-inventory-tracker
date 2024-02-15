from product import Product
product=Product("product_name","product_code","product_current_stock","product_sale_price","product_manufacture_cost","product_monthly_production")
print("Welcome to programming principles sample product inventory")
product.setproduct_code(int(input("Please enter the product code: ")))
product.setproduct_name(input("Please enter the product name: "))
product.setproduct_current_stock(int(input("Please enter the product current stock: ")))
product.setproduct_sale_price(float(input("Please enter the product sale price: ")))
product.setproduct_manufacture_cost(float(input("Please enter the product manufacturing cost: ")))
product.setproduct_monthly_production(int(input("Please enter the estimated monthly production: ")))
