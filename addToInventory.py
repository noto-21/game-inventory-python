def display_inventory(inv, inv_message):  # For showing an inventory
    print(inv_message)  # Print custom Inventory title
    item_total = 0
    for k, v in inv.items():
        print('(' + str(v) + ') ' + ' ' + k.title())  # Print inventory items
        item_total += v
    print("Item Count: " + str(item_total))


def display_shop(sho, sho_message):  # For displaying shops
    print(sho_message)  # Print custom Shop title
    item_total = 0
    for k, v in sho.items():
        print('(' + str(v['amount']) + ')  ' + k.title() + ' -> ' + str(v['price']) + ' coin(s)')  # Print items +
        # prices
        item_total += v['amount']
    print("Item Count: " + str(item_total))


def add_group(inv, added_items):  # Batch adding to inventory (Lists, etc.)
    for adding in added_items:
        if adding.lower() not in str(inv.keys()).lower():
            inv.setdefault(adding, 1)  # New item
        else:
            inv[adding] += 1  # Existing item

    return inv


def add(inv, adding):  # Single item add
    if adding.lower() not in str(inv.keys()).lower():
        inv.setdefault(adding, 1)  # New item
    else:
        inv[adding] += 1  # Existing item

    return inv


inventory = {'gold coin': 0, 'rope': 1}  # Initialize
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'gold coin', 'gold coin', 'gold coin']
inventory = add_group(inventory, dragonLoot)  # Add dragon's loot to inventory

shop_items = {'health potion': {'amount': 3, 'price': 3}, 'magika potion': {'amount': 5, 'price': 1},
              'sexy hat': {'amount': 1, 'price': 3}, 'dagger': {'amount': 1, 'price': 2}}  # Initialize shop
print("""You have defeated the dragon!

As you begin your journey home, you happen across a wandering shopkeeper...

"Would you care to buy some items from my store?"
""")
while True:
    display_shop(shop_items, "Stock:")
    print('-----------------------')
    display_inventory(inventory, "Inventory:")
    choice = input('\nBuy what? (\'X\' to cancel): ').lower()
    if choice == 'X'.lower():  # End
        break
    elif choice.lower() not in str(shop_items.keys()).lower():  # Item not in shop
        print('\n"Hmm... don\'t think I have one of those..."\n')
    elif shop_items[choice.lower()]['amount'] == 0:  # Item exists in shop but is depleted
        print('\n"Sorry, I\'m all out of those!  Try again soon?..."\n')
    elif inventory['gold coin'] == 0 or shop_items[choice.lower()]['price'] > inventory['gold coin']:  # No coin :(
        print('\n"Hey, not cool!  Come back with some coin."\n')
    else:  # 'Base case'
        inventory = add(inventory, choice.lower())  # Add
        inventory['gold coin'] -= shop_items[choice.lower()]['price']  # Exchange currency
        shop_items[choice.lower()]['amount'] -= 1  # Remove item
        print('\n"Thanks!"\n')

print("""
"Later, Traveller!"

You resume your journey...""")
