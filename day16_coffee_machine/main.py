from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


#
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk" : 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# This function updates our ingredients by taking in our resources (resources_input) and then subtracting what we used to make our beverage (beverage_input)
# def update_resources(resource_input, beverage_input):
#   resource_input["water"] -= MENU[beverage_input]["ingredients"]["water"]
#   resource_input["milk"] -= MENU[beverage_input]["ingredients"]["milk"]
#   resource_input["coffee"] -= MENU[beverage_input]["ingredients"]["coffee"]
#   return resource_input
#
#
# def resource_check(resource_input):
#   if resource_input["water"] < 0:
#     print('You don\'t have enough water.')
#     return False
#   elif resource_input["milk"] < 0:
#     print('You don\'t have enough milk.')
#     return False
#   elif resource_input["coffee"] < 0:
#     print('You don\'t have enough coffee.')
#     return False
#   else:
#     return True
#
#
# def money_calculator(num_quarters, num_dimes,  num_nickles, num_pennies):
#   quarters_total = num_quarters * 0.25
#   dimes_total = num_dimes * 0.10
#   nickles_total = num_nickles * 0.05
#   pennies_total= num_pennies * 0.01
#   money_total = quarters_total + dimes_total + nickles_total + pennies_total
#   return money_total

#
# resources_enough = True
# money = 0

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()

taking_orders = True

while taking_orders == True:
  order = input( 'What would you like? (' + menu.get_items()  + 'report): ' )
  if order == 'report':
    coffeemaker.report()
  else:
    beverage = menu.find_drink(order)
    if coffeemaker.is_resource_sufficient(beverage) == True:
      if moneymachine.make_payment(beverage.cost) == True:
        coffeemaker.make_coffee(beverage)







