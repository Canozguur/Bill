price_of_product_list = {"cigarette":20.0,
                         "milk":5.0,
                         "choclate":1.25}

# ups tairs write product and price of product


class Bill:
    def __init__(self,name,surname ,bill):
        self.name = name
        self.surname = surname
        self.bill = dict(bill)

    def calculate(self):
        print("Name :"," "*16,f"{str(self.name).upper()}")
        print("Surname :", " "*13,f"{str(self.surname).upper()}\\n\n")
        all_price = 0
        for product, num in zip(self.bill.keys(),self.bill.values()):
            price = price_of_product_list.get(product)
            price = price * num
            all_price = price + all_price
            num_of_char = len(product) + len(str(num))
            print(f"Product Name : {product}({num}) ","-"*(20-num_of_char),f"{price}TL")
        print(" "*45)
        print("Total Price :","-"*25,f"{all_price} TL")
        print("-"*45)

        
# down stairs write product name and how many user bought it . 
user_stuff = {"cigarette":2,
            "choclate":4}

user = Bill("Can","Ozgur",user_stuff)
user.calculate()
