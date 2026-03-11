def add_ingredient(inventory, ingredient, amount):
    if ingredient in inventory:
        inventory[ingredient] += amount
    else:
        inventory[ingredient] = amount


# successfully brewed potion is added to inventory
def brew_potion(inventory, recipes, potion_name):
    if not (potion_name in recipes):
        return 0
    flag = 1
    for i in recipes[potion_name].keys():
        if not (i in inventory):
            flag = 0
            break
        if inventory[i] < recipes[potion_name][i]:
            flag = 0
            break
    if flag:
        for i in recipes[potion_name].keys():
            inventory[i] -= recipes[potion_name][i]
            if inventory[i] == 0:
                inventory.pop(i)
        if potion_name in inventory:
            inventory[potion_name] += 1
        else:
            inventory[potion_name] = 1
        return 1
    else:
        return 0
