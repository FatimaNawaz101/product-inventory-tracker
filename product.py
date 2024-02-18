class Product:
    def __init__(self,product_name:str,product_code:int,product_current_stock:int,product_sale_price:float,product_manufacture_cost:float,product_monthly_production:int):
         self.setproduct_name(product_name)
         self.setproduct_code(product_code)
         self.setproduct_current_stock(product_current_stock)
         self.setproduct_sale_price(product_sale_price)
         self.monthly_units_manufactured=[]
         self.monthly_units_sold=[]
         
    def setproduct_name(self,name):
        self.product_name=name

    def setproduct_code(self,code):
        self.product_code=code

    def setproduct_current_stock(self,current_stock):
        self.product_current_stock=current_stock

    def setproduct_sale_price(self,sale_price):
        self.product_sale_price=sale_price

    def setproduct_manufacture_cost(self,manufacture_cost):
        self.product_manufacture_cost=manufacture_cost

    def setproduct_monthly_production(self,monthly_production):
        self.product_monthly_production=monthly_production

    def getproduct_name(self):
        return self.product_name
    
    def getproduct_code(self):
        return self.product_code
    
    def getproduct_current_stock(self):
        return self.product_current_stock
    
    def getproduct_sale_price(self):
        return self.product_sale_price
    
    def getproduct_manufacture_cost(self):
        return self.product_manufacture_cost
    
    def getproduct_monthly_production(self):
        return self.product_monthly_production 

    def setunits_purchased_in_month(self,month,units):
        if month<1 or month>12:
            raise Exception("The provided month is not valid; enter a value between 1 and 12 ")
        self.monthly_units_manufactured.append(units)

    def getunits_purchased_in_month(self,month):
        return self.monthly_units_manufactured[month-1]
    
    def setunits_sold_in_month(self,month,units):
        if month<1 or month>12:
            raise Exception("The provided month is not valid; enter a value between 1 and 12 ")
        self.monthly_units_sold.append(units)
        
    def getunits_sold_in_month(self,month):
        return self.monthly_units_sold[month-1]
    
    def view_units_in_month(self,month,units):
        if month <1 or month>12:
            purchased_units=self.monthly_units_manufactured[month-1]
            sold_units=self.monthly_units_sold[month-1]
            raise Exception("The provided month is not valid; enter a value between 1 and 12 ")
        return print(f"In month {month}, units purchased were {purchased_units} and units sold were {sold_units}")
    

          