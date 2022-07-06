def display_menu():
    print('{:*^30}'.format(' Menu '))
    print('1. List of grocery items by category')
    print('2. List of grocery items in alphabetical order')
    print('3. List of items in ascending price')
    print('4. View items in shopping cart')
    print('5. Remove item from shopping cart')
    print('6. Check-out')
    print("")

product={'Milk': [2.30, 'Dairy'],
         'Butter': [4.50, 'Dairy'],
         'Eggs': [3.40, 'Dairy'],
         'Cheese slices': [3.15, 'Dairy'],
         'Creamer': [1.40, 'Dairy'],
         'Tomato': [1.45, 'Canned']
         }

shopping_cart={}

print("{:15s}| {:<8s}| {:s}".format('Item', 'Category', 'Price'))
print("-"*33)
for key in product:
    category=product[key]
    if 'Dairy' in category:
        print("{:15s}| {:<8s}| ${:.2f}".format(key, product[key][1], product[key][0]*1.07))
while(True):
    order = str(input('What would you like to order? '))
    if order not in product:
        print('Please enter valid item')
        continue
    else:
        quantity=str(input('How many of this item do you want to order? '))
        shopping_cart[order]=product[order]
        shopping_cart[order].append(quantity)
        break
print(shopping_cart)







