recipes = {}

with open('recipes.txt.', 'rt', encoding='utf8') as file:
    for a in file:
        recipe_name = a.strip()
        cook_book = {'name': recipe_name, 'ingredients': []}
        ingredients_quantity = file.readline()
        for i in range(int(ingredients_quantity)):
            ing = file.redline()
            ingredients_name, quantity, measure = ing.strip().split(' | ')
            cook_book['ingredients'].append({'ingredient_name': ingredients_name, 'quantity': quantity, 'measure': measure})
        blank_line = file.readline()
        recipes.append()
print(cook_book)
