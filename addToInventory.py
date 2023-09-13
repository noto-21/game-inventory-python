import os
import platform
import re

plural = re.compile(r'[sS]$|[eE][sS]$|[iI][eE][sS]$')  # Regex for plural words

def clear():  # For clearing console
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def display(disp, disp_mssg, shop=False):
    print(disp_mssg)  # Print custom title
    item_total = 0
    for k, v in disp.items():
        if shop:
            print(f'({str(v["amount"])}) {k.title()} -> {str(v["price"])} coin(s)')  # Print items + prices
            item_total += v['amount']
        else:
            print(f'({str(v)}) {k.title()}')  # Print inventory items
            item_total += v
    print(f"Item Count: {str(item_total)}")  # Print total items


def add(inv, added_items = list()):
    if type(added_items) == list:
        for adding in added_items:
            if adding.lower() not in str(inv.keys()).lower():
                inv.setdefault(adding, 1)  # New item
            else:
                inv[adding] += 1  # Existing item
    else:
        if added_items.lower() not in str(inv.keys()).lower():
            inv.setdefault(added_items, 1)  # New item
        else:
            inv[added_items] += 1  # Existing item

    return inv


def transaction(inv, shop, item):
    inv = add(inv, item.lower())  # Add
    inv['gold coin'] -= shop[item.lower()]['price']  # Exchange currency
    shop[item.lower()]['amount'] -= 1  # Remove item
    return '\n"Thanks!"\n'  # Return message


inventory = {'gold coin': 0, 'rope': 1}  # Initialize
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'gold coin', 'gold coin', 'gold coin']
inventory = add(inventory, dragonLoot)  # Add dragon's loot to inventory

shop_items = {'health potion': {'amount': 3, 'price': 3}, 'magika potion': {'amount': 5, 'price': 1},
              'sexy hat': {'amount': 1, 'price': 3}, 'dagger': {'amount': 1, 'price': 2}}  # Initialize shop

clear()

print("""You have defeated the dragon!

As you begin your journey home, you happen across a wandering shopkeeper...

"Would you care to buy some items from my store?"
""")
while True:
    display(shop_items, "Stock:", True)
    print('-----------------------')
    display(inventory, "Inventory:")
    choice = input('\nBuy what? (\'X\' to cancel): ').lower()
    if choice == 'X'.lower():  # End
        break
    elif choice.lower() not in str(shop_items.keys()).lower():  # Item not in shop
        clear()
        print(f'\n"Hmm... don\'t think I have {"a" if plural.search(choice) is None else "any"} {choice.title()}..."\n')
    elif shop_items[choice.lower()]['amount'] == 0:  # Item exists in shop but is depleted
        clear()
        print('\n"Sorry, I\'m all out of those!  Try again soon?..."\n')
    elif inventory['gold coin'] == 0 or shop_items[choice.lower()]['price'] > inventory['gold coin']:  # No coin :(
        clear()
        print('\n"Hey, not cool!  Come back with some coin."\n')
    else:  # 'Base case'
        clear()
        print(transaction(inventory, shop_items, choice))  # Transaction

clear()
print("""
"Later, Traveller!"

You resume your journey...""")
