# create class and initialize with attributes
# create objects & set attributes

class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = 'False'

burgers = Restaurant()
burgers.name = "Chris's Burgers"
burgers.category = "Fast Food"
burgers.rating = 4.5
burgers.delivery = 'True'

print(vars(burgers))

fastfood = Restaurant()
fastfood.name = "Jane's"
fastfood.category = "Fast Food"
fastfood.rating = 4.0
fastfood.delivery = 'True'

print(vars(fastfood))

italian = Restaurant()
italian.name = "Luigi's"
italian.category = "Italian"
italian.rating = 4.1
italian.delivery = 'True'

print(vars(italian))