def tax(price):
    return price * 0.05

def including_tax(price):
    return price + tax(input_price)

input_price = int(input("enter the price of a product"))
print("The price of the product is ${}".format(input_price))
print("The tax of the product is ${}".format(tax(input_price)))
print("After including the tax, the price of the product is ${}".format(including_tax(input_price)))